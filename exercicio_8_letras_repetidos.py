
frase= input("dime un texto")
#creamos un dictionary vacio
letra_dict= dict()

#por cada letra (i) de la frase, 
for i in frase:
    #si la letra no esta en el dictionary entonces afecta un valor de 1
    if i not in letra_dict:
        letra_dict[i] = 1
    # si la letra esta en el dictionary entonces agrega 1 al su valor
    # si la lettre est dans le dictionnaire alors ajoute 1 a sa valeur 
    else:
        letra_dict[i] = letra_dict[i]+1

print(letra_dict)

#funcion

#Creamos una funcion y pasamos un argumento (comentario: frase)
def contador_letras(comentario):
#creamos un dictionary vacio
       letras_contenedor={}
#cada letras dentro el comentario
       for letras in comentario:
#por cada letra en el dictionary
             if letras in letras_contenedor:
                 letras_contenedor[letras] +=1
             else:
                   letras_contenedor[letras]=1
       return letras_contenedor

comentario = "esto es una cosa de prueba"
print(contador_letras(comentario))

#otra posobilidad con una funcion


def contador_letras(comentario):
       letras_contenedor={}
       for letras in comentario:
             if letras in letras_contenedor:
                 letras_contenedor[letras] +=1
             else:
                   letras_contenedor[letras]=1
       return letras_contenedor

comentario = "esto es una cosa de prueba"
print(contador_letras(comentario))

#otra posobilidad con una funcion

def pregunta(mensaje):
    var=input(mensaje)
    letras = {}
    for letra in var:
        if letra not in letras:
            letras[letra] = 1
        else:
            letras[letra] = letras[letra] + 1
    print(letras)
    
cadena=pregunta("Introduce un texto ")

#Programa que te permite de buscar una letra y saber cuanto hay repeticion


#contador de letras en un frase
cadena = input("Ingresa una frase: ")
n = input("Ingresa el caracter a buscar: ")
j = 0
for i in cadena:
    if n == i:
        j = j + 1

print(f"El caracter {n} se encuentra {j} veces")

#con el metodo count y la function char
frase = input("dime una frase")

#usamos el codigo ASCII
for i in range(65,122):
    #convertimos los nombres en letras
    letra=chr(i)
    #contamos el nombre de repeticion
    contador=frase.count(letra)
    #imprimimos solamente las letras que tiene un contador superior a 0
    if contador>0:
    #El "f" te permite de imprimir una variable dentro un cadena de texto
     print(f"la letra {letra} aparece {contador} veces")

#con el metodo get 
cadena_usuario = input("Introduce una cadena de texto:")
cadena_usuario = cadena_usuario.lower()
conteo_letras = {}
for letra in cadena_usuario:
    conteo_letras[letra] = conteo_letras.get(letra, 0) +1

print("Conteo de letras:")
for letra, conteo in conteo_letras.items():
    print(f"{letra}: {conteo}")

#metodo .items  te permite de imprimir todas las llaves o valores de un dictionary 
traductor={
    "casa":"house",
    "perro":"dog",
    "gato":"cat"
}
#crear 2 entradas para registrar en el dictionary y afectar la valor 
for palabra in range(3):
     c=input("dime la palabra en castellano")
     i=input("dime su traduccion")
     traductor[c]=i
for cast, ingles in traductor.items():
    print("castellano: ", cast)