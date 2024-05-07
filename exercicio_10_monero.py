# creamos u programa que te permite de ver el contenido de tu monero gastar dinero y ingresar el monero


class Wallet():
    def __init__(self):
        self.estado = 0
    def ingresar_wallet(self):
        ingresar=int(input("dime cuantos dinero quieres ingresar?"))
        self.estado=ingresar
        return print("Estado de mi wallet esta: ", self.estado)
    def gastar_dinero(self):
        while True:
            gastar=int(input("dime cuanto quieres gastar?"))
            if gastar>self.estado:
                print("siento perro no tienes suficiente dinero")
            else:
                self.estado=self.estado-gastar
                break
        return self.estado

mi_wallet=Wallet() 
mi_wallet.ingresar_wallet()
mi_wallet.gastar_dinero()  

#Ejemplo de uso 

#SOLUCIÓN PROPUESTA:

class Monedero:
    def __init__(self):
        self.saldo = 0

    def gastar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo-cantidad
            return f"Has gastado {cantidad} euros. Saldo restante: {self.saldo} euros."
        else:
            return "No hay suficiente saldo en el monedero."

    def ingresar_dinero(self, cantidad):
        self.saldo = self.saldo+cantidad
        return f"Has ingresado {cantidad} euros. Saldo total: {self.saldo} euros."

#funciones de utilidad
def preguntaint(texto):
    while True:
        try:
            respuesta=int(input(texto))
            break
        except:
            print("entrada Ã©rronea. Teclee un entero")
    return respuesta
    
    # Ejemplo de uso
billetera=Monedero()
opc=0
while opc!=4:
    print("1-ingresar dinero")
    print("2-retirar dinero")
    print("3-ver saldo")
    print("4-salir")
    opc=preguntaint("ingrese la opcion deseada")
    if opc==1:
            importe=preguntaint("cantidad a ingresar: ")
            print(billetera.ingresar_dinero(importe))
    elif opc==2:
            importe=preguntaint("cantidad a retirar: ")
            print(billetera.gastar_dinero(importe))
    elif opc==3:
            print("el salddo disponible es: ",billetera.saldo)
    elif opc >4 or opc <1:
            print("opciÃ³n errÃ³nea, teclee opciÃ³n correcta")
print("programa finalizado")

billetera=Monedero()
opc=0

while opc!=4:
    print("1-Ingresar dinero")
    print("2-Retirar dinero")
    print("3-ver saldo")
    print("4-salir")
    opc=int(input("ingresw a opcion deseada"))
    if opc==1:
        importe=int(input("cantidad a ingresar: "))
        print(billetera.ingresar_dinero(importe))
    elif opc==2:
        importe=int(input("cantidad a retirar: "))
        print(billetera.gastar_dinero(importe))
    elif opc==3:
        print("el saldo disponible es ", billetera.saldo)
    elif opc>4 or opc<1:
        print("opcion erroneq, teclee opcion correcta")


#exemplo que no functiona::: a arreglar

class Wallet():
    

    def __init__(self):
        self.estado = 0
       
    def ingresar_wallet(self, candidad):
        self.estado=candidad+self.estado
        return print("Estado de mi wallet esta: ", self.estado)

    def gastar_dinero(self, candidad):
        self.estado=self.estado-candidad
        if candidad < self.estado:
            print("Siento, no puedes hacer este transaccion")
        else:
            return print("Estado de mi wallet esta: ", self.estado)

        

mi_wallet=Wallet() 

pregunta= int(input("si quieres ingresar, pulsa 1, si Quieres gastar pulse 2"))

if pregunta ==1:
    pregunta_2= int(input("dime cuantos quieres ingresar"))
    print(mi_wallet.ingresar_wallet(pregunta)) 
elif pregunta ==2:
    pregunta_2= int(input("dime cuantos quieres gastar"))
    print(mi_wallet.gastar_dinero(pregunta))
else:
    print("ingresa un numero correcto")
    pregunta= int(input("si quieres ingresar, pulsa 1, si Quieres gastar pulse 2"))

