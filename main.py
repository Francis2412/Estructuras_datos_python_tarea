import os
from tuplas import tuplas_ejer
from conjunto import conjunto_ejer
from diccionario import diccionario_ejer


def main():
    os.system("cls")
    print("************* MENU DE LOS EJERCICIOS **************")
    print("                                              ")
    print("1..........................Ejercicio de tuplas")
    print("2..........................Ejercicio de conjunto")
    print("3..........................Ejercicio de diccionario")
    print("                                              ")
    print("****************************************************")
    print("                                              ")
    opc = int(input("Ingrese el número del ejercicio que desea ejecutar: "))
    match opc:
        case 1:
            tuplas_ejer()
        case 2:
            conjunto_ejer()
        case 3:
            diccionario_ejer()
        
main()