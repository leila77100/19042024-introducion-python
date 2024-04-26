#Exercicio 2 imprimir los multiple de 3 de la lista
#Creamos 2 listas vacias, una por todos los numeros, la segunda por los numeros multiple de tres
lista = []
lista_multiple = []

#iteracion 5 veces 
for i in range(5):
    #solicitar un numero 5 veces
    n=int(input("dime un numero"))
      #si es un multiple de 3 se va dentro las 2 listas  
    if (n %3 == 0):
        lista.append(n)
        lista_multiple.append(n)
    #si no es un multiple de 3 se va dentro la lista entera
    elif (n%3 !=0) :
        lista.append(n)
print("la liste entera es ", lista)
print("la lista de multiple de 3 es", lista_multiple)

#otreo ejemplo

#Declarar la lista
numeros=[]
#Introducir los numeros en la lista
for x in range(6):
#Introducir por teclado cada numero
    numero =int(input("Ingresa un numero"))
#Anadir a la lista dicho numero
    numeros.append(numero)
#Recorrer la lista
for i in range(6):
#Dividir cada numero de la posicio i entre 3
     if numeros[i] % 3 == 0:
#Si el resto es 0 visualizar el numero
        print(numeros[i], " es multiplo de 3")

#otro ejemplo 
lista = []
lista_multiple = []

#iteracion 5 veces 
for i in range(5):
    #solicitar un numero 5 veces
    n=int(input("dime un numero"))
    lista.append(n)
      #si es un multiple de 3 se va dentro las 2 listas  
    if (n %3 == 0):
        lista_multiple.append(n)
print("la liste entera es ", lista)
print("la lista de multiple de 3 es", lista_multiple)

# ejemplo con una bucle for y numero, te permite de ir al elemento y no al indice de la lista 

# Crear una lista vacía para los numeros
numeros = []

# Pedir al usuario 6 números
for i in range(6):
     num = int(input("Introduce el número " + str(i+1) + ": "))
     numeros.append(num)

# Crear una lista vacía para almacenar los múltiplos de 3
multiplosdetres = []

# Comprobar cuáles son múltiplos de 3
for num in numeros:
  if num % 3 == 0:
        multiplosdetres.append(num)

# Mostrar los múltiplos de 3
print("Los números que son múltiplos de 3 son: ", multiplosdetres)
