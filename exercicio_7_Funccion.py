
#hacemos una funccione con un parametro
def pregunta(mensaje):
    while True:
#abrimos una ventana con el mensaje del argumento de la funccion
        variable=input(mensaje)
#verificamos si la entrada es un numero , no se admite coma o punto 
        if variable.isdigit():
#convertimos en un digito con el int()
            numero=int(variable)
            break
        else:
            print("error: La entrada no se reconoce como numero")
    return numero
print("programa de prueba")
#creamos  variables con los 2 numeros del usuario
n1= pregunta("dime el primer numero")
n2= pregunta("dime el segundo numero")
#Multiplica el primer numero con el segundo
print("el resultado de la multiplicacion es ", n1*n2)