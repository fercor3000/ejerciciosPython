import mysql.connector

class Registro_datos():
    def __init__(self):
        #Conexion con la base de datos, donde necesito los datos a continuacion
        self.conexion = mysql.connector.connect( # Importante tener importada la libreria de mysql.connector para poder conectarnos
            host='localhost',
            user='root',
            password='fercor11',
            port='3306',
            database='empleadospython'
        )

    # Para ejecutar sentencias SQL, siempre necesitamos un cursor

    def mostrar_empleados(self):
        try:
            mycursor = self.conexion.cursor()
            mycursor.execute('SELECT * FROM empleados') # Sentencia SQL
            registro = mycursor.fetchall()
            return registro
        except:
            print("ERROR: Error en MOSTRAR EMPLEADOS")

    def insertar_empleado(self, idempleado, nombre, apellido1, apellido2, dni, fecha_nacimiento, puesto_trabajo, sueldo, anios_antiguedad):
        try:
            mycursor = self.conexion.cursor()
            consulta = 'INSERT INTO empleados (idempleado, nombre, primerApellido, segundoApellido, dni, fechaNacimiento, puestoTrabajo, sueldo, aniosAntiguedad) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)' # Sentencia SQL
            emp_datos = (idempleado, nombre, apellido1, apellido2, dni, fecha_nacimiento, puesto_trabajo, sueldo, anios_antiguedad)
            mycursor.execute(consulta, emp_datos)
            self.conexion.commit()
            mycursor.close()  # Cerrar cursor

            return True
        except:
            print("ERROR: Error en INSERTAR EMPLEADO")
            return False

    def eliminar_empleado(self, idemp):
        try:
            mycursor = self.conexion.cursor()
            mycursor.execute('DELETE FROM empleados WHERE idempleado = ' + idemp) # Sentencia SQL
            self.conexion.commit()
            mycursor.close()  # Cerrar cursor
        except:
            print("ERROR: Error en ELIMINAR EMPLEADO")

    def buscar_empleado(self, nombre_emp):
        try:
            mycursor = self.conexion.cursor()
            mycursor.execute('SELECT * FROM empleados WHERE nombre = "' + nombre_emp + '"') # Sentencia SQL
            registro = mycursor.fetchall()
            mycursor.close()
            return registro
        except:
            print("ERROR: Error en BUSCAR EMPLEADO")

    def modificar_empleado(self, nuevoSueldo, idEmp):
        try:
            mycursor = self.conexion.cursor()
            mycursor.execute('UPDATE empleados SET sueldo = "' + str(nuevoSueldo) + '"' + 'WHERE idempleado = "' + str(idEmp) + '"') # Sentencia SQL
            self.conexion.commit()
            mycursor.close()  # Cerrar cursor
        except:
            print("ERROR: Error en MODIFICAR EMPLEADO")