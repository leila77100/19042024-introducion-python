class Monedero:
    def __init__(self):
        self.saldo = 100

    def gastar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo-cantidad
            return f"Has gastado {cantidad} euros. Saldo restante: {self.saldo} euros."
        else:
            return "No hay suficiente saldo en el monedero."
        
    def gastar_dinero_infantil(self, cantidad):
        if cantidad <= self.saldo and cantidad <=50:
            self.saldo = self.saldo-cantidad
            return f"Has gastado {cantidad} euros. Saldo restante: {self.saldo} euros."
        if cantidad>=50:
            return "No puedes gastar mas de 50 euros"
        else:
            return "No hay suficiente saldo en el monedero."

    def ingresar_dinero(self, cantidad):
        self.saldo = self.saldo+cantidad
        return f"Has ingresado {cantidad} euros. Saldo total: {self.saldo} euros."
    
mi_monedero = Monedero()

pregunta= int(input("pulse 1 si eres un adulto y 2 si eres un niño"))

while pregunta==1:
    pregunta_2= int(input("pulse 1 si quieres gastar y 2 si quieres ingresar"))
    if pregunta_2 ==1:
        candidad=int(input("cuanto quieres gastar?"))
        print(mi_monedero.gastar_dinero(candidad))
    else:
        candidad=int(input("cuanto quieres ingresar"))
        print(mi_monedero.ingresar_dinero(candidad))
if pregunta == 2:
    candidad=int(input("cuanto quieres gastar?"))
    print(mi_monedero.gastar_dinero_infantil(candidad))
