#Exercicio de entrar un numero y parrar el programo cuando eun numero se repite 

#thislist =["apple", "banana", "cherry"]
#if "apple" in thislist:
#    print("Yes, `apple´ is in the fruits en la lista")


lista_numero = list()
n=int(input("entra un numero"))

# hacemos un bucle que registra el numero en una lista y verifica que el numero ne se duplica

while n not in lista_numero:
        lista_numero.append(n)
        n=int(input("entra de nuevo un numero"))
print("el programo se termino")

#otra exemplo 
#Crea una lista vaci­a
lista=[]
#Inicializa la variable
repetido=False
#Bucle hasta introducir un numero repetido
while not repetido:
     numero = int(input("introduce un numero"))
     if numero not in lista:
         lista.append(numero)
     else:
          repetido=True
#Imprime la lista
print(lista)