#un conjunto es una colección de elementos no ordenados
#Son  herterogéneos per solo con elementos inmutables
#Mutables
#Sin repeteción

#-> Un conjunto es una estructura que permite guardar varios elementos,
# pero sin repetirlos.
numero = int(input("Digite la cantidad de frutas que desea ingresar: "))
frutas = set()
for i in range (numero):
    fruta = input(f"Ingrese el nombre de la fruta #{i+1}: ") 
    frutas.add(fruta) #-> agregá fruta al conjunto frutas / agregar un elemento a un conjunto.

print(frutas)