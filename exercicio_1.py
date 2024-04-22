#Realiza un programa en Python en el que se soliciten números por teclado hasta que la suma de todos ellos supere la cantidad de 50. En ese momento imprimirá la cantidad total acumulada y termina el programa.

contador = 0
i=int(input("dime un numero"))
while i!=50:
    contador = contador +i 
    print("llevas acumulado", contador, "empeza de nuevo")
    if (contador>50):
        print("se termino el programa")        
        break
    else:
        i=int(input("dime un numero"))



#Inicializamos la variable suma (acumulador)
suma = 0
#Mientras el numero sea menor o igual a 50
while suma <= 50:
    #Solicita un numero
    numero = int(input("Escribe un numero"))
    #Acumulamos los numeros introducidos en la variable suma
    suma = suma + numero
#Imprimir por pantalla mensaje de que ha superado los 50
print("El numero acumulado es ", suma, " y ha superado los 50")

#Ejercicio 2: completa el ejercicio anterior añadiendo la funcionalidad de que sólo acumule los números pares

contador = 0
i=int(input("dime un numero"))
while i!=50:
    contador = contador +i 
    print("llevas acumulado", contador, "empeza de nuevo")
    if (contador>50):
        print("se termino el programa")        
        break
    else:
        i=int(input("dime un numero"))


#exercicio de bucle for 

acumulador = 0
for x in range(6):
    n=int(input("dime un numero"))
    acumulador+=n
print("el valor acumulado es ", acumulador)

#saber cual es el numero mayor

array= []

n=int(input("dime un numero"))

for i in range(6):
    n=int(input("dime un numero"))
    
    if n >= max(array): 
        array.append(n) 
        print("el numero mas grande es ", n)


#Iniciar la variable donde se va a introducir el numero mayor
mayor=int(input("dime un numero"))
#Bucle donde se va a introducir los cinco numeros
for x in range(4):
      #introducir los cinco numeros
      n=int(input("dime un numero"))
      #Comparar numeros e introducir en la variable mayor el numero mayor
      if (mayor<n):
          mayor=n
# Visualizar el numero mayor
print("El numero mayor es  ",mayor)


# con la metodo max

acumulador =[]
for x in range(5):
      numero =int(input("Ingresa un número"))
      acumulador.append(numero)

print("El número mayor ingresado es: ",max(acumulador))