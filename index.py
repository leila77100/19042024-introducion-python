# print("hola mundo")

# print(5+3)

#hacer una condicion
n=int(input("dime un numero"))
n2=int(input("dime otro numero"))
if n>n2:
    print("el mayor es",n)
if n2>n:
    print("el mayor es",n2)
    resultado=n+n2 
    print("la suma es", resultado)
else:
    print("losumerosson iguales")
 
#hacer una bucle 
acumulador = 0
n=int(input("dime un numero"))
while n!=0:
    acumulador =acumulador +n 
    print("llevas acumulado", acumulador)
    n=int(input("dime un numero"))
    print("se termino el programa")