#iniciamos una clase modero que te permite de gastar y ingresar
#si es un menor de edad no se puede gastar mas que 50 euros 

class Monedero:
    def __init__(self):
        #iniciamos un saldo a 0
        self.saldo = 0
#metodo que permite de gastar dinero, pasamos el self para acceder al saldo, y candidad para ingresar una candidad 
    def gastar_dinero(self, cantidad):
        #si la candidad solicite esta inferior al saldo entonces el saldo = saldo menos candidad
        if cantidad <= self.saldo:
            self.saldo = self.saldo-cantidad
            return f"Has gastado {cantidad} euros. Saldo restante: {self.saldo} euros."
        else:
            return "No hay suficiente saldo en el monedero."
#metodo que te permite de gastar dinero en el caso de un menor de edad   
    def gastar_dinero_infantil(self, cantidad):
        if cantidad <= self.saldo and cantidad <=50:
            self.saldo = self.saldo-cantidad
            return f"Has gastado {cantidad} euros. Saldo restante: {self.saldo} euros."
        if cantidad>=50:
            return "No puedes gastar mas de 50 euros"
        else:
            return "No hay suficiente saldo en el monedero."
#metodo que te permite de ingresar dinero en el caso de un adulto
    def ingresar_dinero(self, cantidad):
        self.saldo = self.saldo+cantidad
        return f"Has ingresado {cantidad} euros. Saldo total: {self.saldo} euros."
    
mi_monedero = Monedero()

#ventana para preguntar el tipo de usuario
pregunta= int(input("pulse 1 si eres un adulto y 2 si eres un niño"))

#bucle si es un adulto
while pregunta==1:
    #registramos la opcion del usuario 
    pregunta_2= int(input("pulse 1 si quieres gastar y 2 si quieres ingresar"))
    #accion cuando el adulto quiere gastar
    if pregunta_2 ==1:
        candidad=int(input("cuanto quieres gastar?"))
        #enviamos la candidad a la funccion gastar_dinero
        print(mi_monedero.gastar_dinero(candidad))
    else:
        candidad=int(input("cuanto quieres ingresar"))
        #enviamos la candidad a la funccion ingresar_dinero
        print(mi_monedero.ingresar_dinero(candidad))
#el caso de un niño
if pregunta == 2:
    candidad=int(input("cuanto quieres gastar?"))
    #enviamos la candidad a la funccion gastar_dinero_infantil
    print(mi_monedero.gastar_dinero_infantil(candidad))
