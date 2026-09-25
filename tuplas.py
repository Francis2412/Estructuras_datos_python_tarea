#Las tuplas son estructuras de datos en Python que permiten almacenar múltiples elementos en 
#un solo objeto. A diferencia de las listas, las tuplas son inmutables, lo que significa
#que no pueden modificarse después de ser creadas. Esto las hace ideales para representar
#datos constantes o que no deben cambiar durante la ejecución del programa.
  
#Otro dato es que en las listas se usan [] y en las tuplas ()
import os
def tuplas_ejer():
    os.system("cls")
    
    nombre = input("Ingrese su 1er nombre: ")
    apellido = input("Ingrese su 1er apellido: ")
    nombre_completo=(nombre, apellido )
    print(f"Nombre del usuario: {nombre_completo[0]}")
    print(f"Apellido del usuario: {nombre_completo[1]}")

