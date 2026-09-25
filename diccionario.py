#un diccionario guarda información en forma de clave -> valor.
#Diccionario -> diccionario["clave"] para obtener el valor.
import os 
def diccionario_ejer():
    os.system("cls")
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    colorfav = input("Ingrese su color favorito: ")
    animafav = input("Ingrese su animal favorito: ")
    usuario ={
        "nombre": nombre,
        "edad": edad,
        "color favorito": colorfav,
        "animal favorito": animafav
        }
    
    info = input("¿Qué información desea saber sobre el usuario?: ")
    if info == "nombre":
        print(usuario["nombre"])
    elif info == "edad":
        print(usuario["edad"])
    elif info == "color favorito":
        print(usuario["color favorito"])
    elif info == "animal favorito":
        print(usuario["animal favorito"])
    else:
        print("información no registrada...")
