#-------------------------------------------------------------------------------
# Name:        JUEGO DE LOTERIA
# Purpose:
#
# Author:      javier
#
# Created:     06/11/2021
# Copyright:   (c) javier 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import randint
import sys
print ("               JUEGO DE LOTERIA")
print ("*" * 70)
print ("")


#ELEGIMOS JUGAR O SALIR
opcion = ""
while opcion != "b":
    print ("........  ESCOGE UNA OPCIÓN  ........ ")
    print ("            a ) JUGAR")
    print ("            b ) SALIR")
    opcion = input("TECLEA UNA DE LAS OPCIONES Y PULSA ENTER\n")
    if opcion == "a" or opcion == "A":
        print ("INTRODUCE LOS NÚMEROS DEL 1 AL 49")
        print ("." * 70)

        #PRIMERO INTRODUCIMOS LOS NÚMEROS

        def mi_combinación():
            while True:
                try:
                    num1 = int(input("INTRODUCE EL PRIMER NÚMERO: "))
                    num2 = int(input("INTRODUCE EL SEGUNDO NÚMERO: "))
                    num3 = int(input("INTRODUCE EL TERCER NÚMERO: "))
                    num4 = int(input("INTRODUCE EL CUARTO NÚMERO: "))
                    num5 = int(input("INTRODUCE EL QUINTO NÚMERO: "))
                    num6 = int(input("INTRODUCE EL COMPLEMENTARIO: "))
                    break
                except ValueError:
                    print (":" * 70)
                    print ("DEBE INTRODUCIR UN NÚMERO")
                    print (":" * 70)

            mis_números = [num1, num2, num3, num4, num5, num6]
            mis_números.sort()
            print ("." * 70)
            print ("ESTA ES MI COMBINACIÓN: ",mis_números)
            return mis_números


        números = mi_combinación()

        #SE COMPRUEBAN LOS POSIBLES ERRORES EN LOS NÚMEROS INTRODUCIDOS Y SI HAY, SE VUELVE A EJECUTAR LA FUNCIÓN mi_combinación
        for N in range(len(números)):
            if números[N] > 49 or números[N] < 1 or números.count(números[N]) > 1:
                print ("0" * 40)
                print ("EL NÚMERO {} NO ES CORRECTO.".format(números[N]))
                print ("0" * 40)
                números = mi_combinación()

        #AHORA EJECUTAMOS UNA COMBINACIÓN AL AZAR CON BUCLE DE 6 TANDAS EN UNA FUNCIÓN
        print ("." * 70)

        def Combinación():
            num = []
            tandas = 0
            Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
            19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
            38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

            while tandas < 6:
                elegir = randint(1, len(Lista)- 1)
                N = Lista[elegir]
                Lista.remove(N)
                num.append(N)
                tandas += 1
                num.sort()     #ordena la lista de menor a mayor
            return num

        #COMPARAMOS NUESTRA COMBINACIÓN CON LAS COMBINACIONES ALEATORIAS
        def comparar(C, N):
            lista_final = []
            print (C)

            for item in range(len(N)):
                for comparar in range (len(C)):
                    if N[item] == C[comparar]:
                        lista_final.append(N[item])

            return lista_final


        #SE COMPARAN TODAS LAS COMBINACIONES EN UN BUCLE WHILE
        rondas = 0
        while rondas < 5:
            comb = Combinación()
            resultado = comparar(comb, números)
            if len(resultado) > 0:
                aciertos = len(resultado)
                if len(resultado) == 1:
                    print ("TIENES UN ACIERTO EN EL NÚMERO: ", resultado)
                    print ("-" * 60)
                else:
                    print ("TIENES {} ACIERTOS Y TUS NÚMEROS SON {}: ".format(aciertos, resultado))
                    print ("-" * 60)
            else:
                print ("NO HAS ACERTADO NINGUNO")
                print ("-" * 60)
            rondas += 1

        print ("-" * 60)
    if opcion == "b" or opcion == "B":
        print ("------- GRACIAS POR USAR EL PROGRAMA. -------")
print ("         --------- ADIÓS ;) -----------")
print ("?" * 60)


while True:
    try:
        cerrar = (input("PARA CERRAR EL PROGRAMA PULSA S\n"))
        if cerrar == "s" or cerrar == "S":
            break
    except:
        print ("DEBES TECLEAR S PARA SALIR")
sys.exit()
input()