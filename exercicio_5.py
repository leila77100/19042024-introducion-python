
#Realiza un script que genere apuestas de la lotería primitiva. La combinación estará formada por:
#Seis números aleatorios entre 1 y 49 (hay que controlar las posibles repeticiones)
#un número aleatorio entre 0 y 9 para el reintegro.
import random

lista = list()
lista_numero =[0,1,2,3,4,5,6,7,8,9]
numero_loteria = 50

# generer un nombre aleatoire 
numeros_aleatorios = random.randint(1,49)

#hacemos 6 repeticion
for i in range(6):
#Si el numero genere no esta en la lista añadir el numero
    if numeros_aleatorios not in lista:
        lista.append(numeros_aleatorios)
#si el numero esta en la lista y que la longitud de la lista es inferieur a 6 elementos añadir añadir un nuevo numero aleatorio
    if numeros_aleatorios in lista and len(lista) < 6:
        numeros_aleatorios = random.randint(1,49)
        lista.append(numeros_aleatorios)
 #bucle hasta que el numero corresponde a la lista_numero   
while numero_loteria not in lista_numero:
    numero_loteria= random.choice(lista)

print(lista)
print(numero_loteria)

#otre manera con la metodo sample

#genere  6 numeros aleatoire entre 1 et 50, se puede le hacer a partir de una lista de numero o letras
numeros = random.sample(range(1,50),6)
numeros.sort()
print(numeros)
reintegro=random.randint(0,9)
print(reintegro)

#usamos el conjutos, no tiene orden y no se puede poner 2 elementos identica

# es nesesario de declarar el conjunto con el set porque si es con {} el sistema interpreta que es un dictionario
comb=set()
while len(comb)< 6:
    aleatorio=random.randint(1,49)
    comb.add(aleatorio)
print("la combinacion aleatorio", comb)
reintegro=random.randint(0,9)
print("reintegro:", reintegro)