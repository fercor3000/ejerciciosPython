'''
7) Escriba un programa en python que me muestre por pantalla si un número es primo, y si no lo es que me escriba el número en factores primos, por ejemplo:

    20=2^2*5
'''

'''Lista de números primos entre 1 y 100: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 y 97.'''

num = int(input("Introduzca un numero:"))
listaP = list()
factoresPrimos = list()

if num > 0:
    esPrimo = True

    for i in range(2, num):
        if num % i == 0:
            listaP.append(i) # Meto en un array los numeros que son divisores del numero introducido
            esPrimo = False
    if num != 1:
        if esPrimo:
            print(num, "es un numero primo")
        else:
            divCheck = num # Meto el numero introducido en otra variable que modificaremos su contenido mas adelante
            for x in listaP: # Recorro el array introduciendo cada valor del array en x
                while divCheck % x == 0: # Hago un while donde mientras el resto sea cero, que siga el bucle
                    divCheck = divCheck/x # Divido el numero entre lo que tenga x, y el nuevo resultado lo introduzco a divCheck y sigo diviendo hasta que no se pueda dividir mas
                    factoresPrimos.append(x) # Meto los divisores en un nuevo array

            print(num, "= ", end="")
            for n in range(len(factoresPrimos)): #Solo no queda sacar el numero en factores primos por la consola
                if n != len(factoresPrimos) - 1:
                    print(factoresPrimos[n], "* ", end="")
                else:
                    print(factoresPrimos[n], end="")
    else:
        print(num, "NO es un numero primo")
else:
    print("Numero incorrecto, vuelva a intentarlo")