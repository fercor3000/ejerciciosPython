'''
Problema práctico: Se desea realizar una interfaz en python para el tratamiento de datos de los empleados de una empresa.
En esta empresa los datos se almacenan en una base de datos, se almacena, nombre, primer apellido, segundo apellido, DNI ,
fecha de nacimiento, puesto de trabajo, sueldo y años de antigüedad. La interfaz dispondrá de varios botones y Label, y
campos entry para introducir valores de entrada. Puede tener 3 botones, para insertar, borrar, modificar algún dato o datos,
y buscar empleado con posibles criterios de búsqueda, ya sea nombre, DNI, apellidos, etc.. y si hay más de uno con ese criterio
mostrarlo por pantalla. La librería que podéis usar para este problema es la de tkinter.
'''

from tkinter import *
from tkinter import Entry, Label, Frame, Tk, ttk, StringVar, messagebox # El ttk es como una extension del tkinter, que contiene elementos más bonitos esteticamente

from conexion import Registro_datos

class RegistroEmp():

    def __init__(self): #Constructor
        self.base_datos = Registro_datos()
        #Variable main = ventana
        main = Tk()
        #Tamanio de la ventana
        width = 920
        height = 460
        #Funcion para ajustar la ventana segun la pantalla
        screen_width = main.winfo_screenwidth()
        screen_height = main.winfo_screenmmheight()
        #Posicion en la pantalla
        x = (screen_width/2) - (width/2)
        y = screen_height
        #Aplicamos el tamanio a la ventana y la posicion
        #%d x %d + %d + %d = ancho x alto + x + y
        main.geometry('%dx%d+%d+%d' % (width, height, x, y))
        #Titulo de la ventana
        main.title("Modificar BBDD")
        #Self se usa porque sino no se puede usar la variable fuera del constructor
        #Con StringVar() declaramos variables de control de tipo String (nos permitirá usar get y ser más adelante)
        self.id = StringVar()
        self.nombre = StringVar()
        self.apellido1 = StringVar()
        self.apellido2 = StringVar()
        self.dni = StringVar()
        self.fecha_nacimiento = StringVar()
        self.puesto_trabajo = StringVar()
        self.sueldo = StringVar()
        self.anios_antiguedad = StringVar()

        self.filtro = StringVar()
        self.modificar = StringVar()

        #Todos nuestros frames iran dentro de main y dentros de estos frames iran los elementos, dividimos en grupos y organizamos la distribucion

        #### FRAME PRIMERO ####
        frame1 = Frame(main, bg="lightblue") #Los frames son cajas/recuadros donde meteremos los elementos en un grupo y moveremos ese frame donde queramos en nuestra ventana
        frame1.grid(columnspan=2, column=0, row=0)

        titulo1 = Label(frame1, text='Empleados Base de Datos', fg="black", font=("Verdana", 14)) #El label es para poner un texto/titulo
        titulo1.pack(side=TOP, padx=10, pady=10)

        frame1.pack(fill="x") #Si no usamos .pack el elemento no aparecerá en la ventana, hay que darle un tamaño y donde se ubicará

        #### FRAME SEGUNDO ####
        frame2 = Frame(main, pady=10)

        label1 = Label(frame2, text='ID', fg="black", font=("Verdana", 10)).grid(row=0, column=0)
        label2 = Label(frame2, text='Nombre', fg="black", font=("Verdana", 10)).grid(row=1, column=0)
        label3 = Label(frame2, text='Apellido1', fg="black", font=("Verdana", 10)).grid(row=2, column=0)
        label4 = Label(frame2, text='Apellido2', fg="black", font=("Verdana", 10)).grid(row=3, column=0)
        label5 = Label(frame2, text='Dni', fg="black", font=("Verdana", 10)).grid(row=4, column=0)
        label6 = Label(frame2, text='Fecha\nNacimiento', fg="black", font=("Verdana", 10)).grid(row=5, column=0)
        label7 = Label(frame2, text='Puesto\nTrabajo', fg="black", font=("Verdana", 10)).grid(row=6, column=0)
        label8 = Label(frame2, text='Sueldo', fg="black", font=("Verdana", 10)).grid(row=7, column=0)
        label9 = Label(frame2, text='Anios\nAntiguedad', fg="black", font=("Verdana", 10)).grid(row=8, column=0)

        Entry(frame2, textvariable=self.id, font=("Verdana", 10)).grid(row=0, column=1, pady=5) # Los Entry son campos donde el usuario puede escribir y el programa recoger lo escrito
        Entry(frame2, textvariable=self.nombre, font=("Verdana", 10)).grid(row=1, column=1, pady=5)
        Entry(frame2, textvariable=self.apellido1, font=("Verdana", 10)).grid(row=2, column=1, pady=5)
        Entry(frame2, textvariable=self.apellido2, font=("Verdana", 10)).grid(row=3, column=1, pady=5)
        Entry(frame2, textvariable=self.dni, font=("Verdana", 10)).grid(row=4, column=1, pady=5)
        Entry(frame2, textvariable=self.fecha_nacimiento, font=("Verdana", 10)).grid(row=5, column=1, pady=5)
        Entry(frame2, textvariable=self.puesto_trabajo, font=("Verdana", 10)).grid(row=6, column=1, pady=5)
        Entry(frame2, textvariable=self.sueldo, font=("Verdana", 10)).grid(row=7, column=1, pady=5)
        Entry(frame2, textvariable=self.anios_antiguedad, font=("Verdana", 10)).grid(row=8, column=1, pady=5)

        btnInsertar = ttk.Button(frame2, text="Insertar", command=self.insertar_empleado).grid(row=9, column=1, padx=1, pady=1) #Botones para que el usuario interactue con el programa
        btnVaciar = ttk.Button(frame2, text="Vaciar", command=self.vaciar_entrys).grid(row=10, column=1, padx=1, pady=1) # Botones para que el usuario interactue con el programa

        frame2.pack(side=LEFT, fill="y")

        #### FRAME TERCERO ####
        frame3 = Frame(main)

        self.tabla = ttk.Treeview(main, height=10, columns=('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8')) #Creacion de una tabla

        self.tabla.heading("#0", text="ID", anchor=CENTER,)
        self.tabla.heading("#1", text="Nombre", anchor=CENTER)
        self.tabla.heading("#2", text="Apellido1", anchor=CENTER)
        self.tabla.heading("#3", text="Apellido2", anchor=CENTER)
        self.tabla.heading("#4", text="Dni", anchor=CENTER)
        self.tabla.heading("#5", text="Fecha\nNacimiento", anchor=CENTER)
        self.tabla.heading("#6", text="Puesto\nTrabajo", anchor=CENTER)
        self.tabla.heading("#7", text="Sueldo", anchor=CENTER)
        self.tabla.heading("#8", text="Años\nAntiguedad", anchor=CENTER)

        self.tabla.column('#0', minwidth=20, width=70, anchor='center')
        self.tabla.column('#1', minwidth=20, width=70, anchor='center')
        self.tabla.column('#2', minwidth=20, width=70, anchor='center')
        self.tabla.column('#3', minwidth=20, width=70, anchor='center')
        self.tabla.column('#4', minwidth=20, width=70, anchor='center')
        self.tabla.column('#5', minwidth=20, width=70, anchor='center')
        self.tabla.column('#6', minwidth=20, width=70, anchor='center')
        self.tabla.column('#7', minwidth=20, width=70, anchor='center')
        self.tabla.column('#8', minwidth=20, width=70, anchor='center')

        self.tabla.pack(pady=20)

        frame3.pack(anchor=CENTER)

        #### FRAME CUARTO ####
        frame4 = Frame(main)
        # Para organizar los elementos en forma de filas y columnas existe el .grid
        btnBorrar = ttk.Button(frame4, text="Borrar", command=self.eliminar_fila).grid(row=0, column=0, padx=5, pady=10)
        btnModificar = ttk.Button(frame4, text="Modificar Sueldo", command=self.modificar_sueldo).grid(row=1, column=0, padx=5, pady=10)
        Entry(frame4, textvariable=self.modificar, font=("Verdana", 10)).grid(row=1, column=1, columnspan=3)
        btnBuscar = ttk.Button(frame4, text="Buscar Nombre", command=self.buscar_nombre_emp).grid(row=2, column=0, padx=5, pady=10)
        Entry(frame4, textvariable=self.filtro, font=("Verdana", 10)).grid(row=2, column=1, columnspan=3)
        btnMostrar = ttk.Button(frame4, text="Mostrar", command=self.mostrar_todo).grid(row=0, column=2, padx=5, pady=10)
        btnLimpiar = ttk.Button(frame4, text="Limpiar", command=self.limpiar_tabla).grid(row=0, column=3, padx=5, pady=10)

        frame4.pack(anchor=CENTER)

        #El .mainloop sirve para mantener la ventana principal main abierta hasta que el usuario la cierre
        main.mainloop()

    '''DIFERENTES FUNCIONES QUE USO'''

    #### MOSTRAR EN LA TABLA ####
    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())  #Borrar contenido de la tabla
        registro = self.base_datos.mostrar_empleados()  #Mete lo que devuelve mostrar_productos en la variable
        i = -1
        for dato in registro:
            i += 1
            self.tabla.insert('', i, text=registro[i][0:1], values=registro[i][1:9]) #Inserto los datos de cada registro dentro de la tabla y lo muestro

    ### VACIAR ENTRYS ###
    def vaciar_entrys(self):
        #Pongo todos los Entry vacios con el .set
        self.id.set("")
        self.nombre.set("")
        self.apellido1.set("")
        self.apellido2.set("")
        self.dni.set("")
        self.fecha_nacimiento.set("")
        self.puesto_trabajo.set("")
        self.sueldo.set("")
        self.anios_antiguedad.set("")

    ### INSERTAR EN LA TABLA E VACIAR CAJAS ###
    def insertar_empleado(self):
        checkCampos = True #Comprobar que no haya un campo mal introducido

        self.tabla.get_children()
        # Obtengo de los Entry lo que haya escrito el usuario
        id = self.id.get()
        nombre = self.nombre.get()
        apellido1 = self.apellido1.get()
        apellido2 = self.apellido2.get()
        dni = self.dni.get()
        fecha_nacimiento = self.fecha_nacimiento.get()
        puesto_trabajo = self.puesto_trabajo.get()
        sueldo = self.sueldo.get()
        anios_antiguedad = self.anios_antiguedad.get()
        datos = (nombre, apellido1, apellido2, dni, fecha_nacimiento, puesto_trabajo, sueldo, anios_antiguedad)

        if id and nombre and apellido1 and apellido2 and dni and fecha_nacimiento and puesto_trabajo and sueldo and anios_antiguedad != '': # Comprobar que no haya campos vacios
            self.base_datos.insertar_empleado(id, nombre, apellido1, apellido2, dni, fecha_nacimiento, puesto_trabajo, sueldo, anios_antiguedad)  # Llamo a otra funcion y le paso datos
            checkCampos = self.base_datos.insertar_empleado # Meto el boolean que me devuelve la funcion
            if checkCampos == True: # Si es TRUE, meto en la tabla sin problemas
                self.tabla.insert('', 0, text=id, values=datos) # Inserto en la tabla los datos nuevos
            else: # En caso contrario, informo al usuario de que algo hizo mal
                op = messagebox.showinfo("Cuidado", "Campos mal introducidos")


    ### ELIMINAR DE LA TABLA ###
    def eliminar_fila(self):
        fila = self.tabla.focus()  # Devuelve la tuple de la fila seleccionada de la tabla
        if len(fila) != 0: #Compruebo que el Entry no este vacio
            op = messagebox.askquestion("¿Eliminar?", "¿Estas seguro?") # Saco mensaje preguntando si esta seguro de eliminar
            if op == "yes": # Si pulsa "Si" continuo con la eliminacion
                self.base_datos.eliminar_empleado(self.tabla.item(fila)["text"])  # Obtengo el ID de la fila que tiene el foco y los paso como parametro a otra funcion
                self.tabla.delete(fila) # Borro esa fila de la tabla

    ### MODIFICAR SUELDO ###
    def modificar_sueldo(self):
        modi = self.modificar.get() # Obtengo el nuevo sueldo
        fila = self.tabla.focus()
        self.base_datos.modificar_empleado(modi, self.tabla.item(fila)["text"]) #Obtengo el ID de la fila que tiene el foco y lo paso como parametro a otra funcion

        self.mostrar_todo() # Llamo a esta funcion para refrescar los datos de la tabla

    ### BUSCAR EMPLEADO ###
    def buscar_nombre_emp(self):
        buscar_nombre = self.filtro.get()
        self.tabla.delete(*self.tabla.get_children())  # Borro_todo el contenido de la tabla
        registro = self.base_datos.buscar_empleado(buscar_nombre) #Meto el registro/s obtenido/s en una variable

        i = -1
        for dato in registro:
            i += 1
            self.tabla.insert('', i, text=registro[i][0:1], values=registro[i][1:9]) # Muestro ese registro/s que me ha devuelto la funcion

    #### LIMPIAR LA TABLA ####
    def limpiar_tabla(self):
        self.tabla.delete(*self.tabla.get_children()) # Borro_todo el contenido de la tabla
        registro = self.base_datos.mostrar_empleados() # Obtengo los registros de la tabla
        i = -1
        for dato in registro:
            i += 1
            self.tabla.insert('', i, values='') # Los pongo vacios

programa = RegistroEmp() # Inicio la clase
