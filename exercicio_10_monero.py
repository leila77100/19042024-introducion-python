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
        pregunta=input("que quieres hacer, ingresar O gastar?")
        
        if pregunta == "ingresar":
            pregunta = True
            ingresar_wallet(self)
            
        if pregunta == "gastar":
            pregunta=False
            print("el estatut del cuenta esta:", self.estado)
            gastar_dinero(self)
            
def ingresar_wallet(self):
    ingresar=int(input("dime cuantos dinero quieres ingresar?"))
    self.estado=ingresar+self.estado
    return print("Estado de mi wallet esta: ", self.estado)

def gastar_dinero(self):
    gastar=int(input("dime cuanto quieres gastar?"))
    self.estado=self.estado-gastar
    while True:
        gastar=int(input("dime cuanto quieres gastar?"))
        if gastar >self.estado:
                print("siento perro no tienes suficiente dinero")
        else:
                self.estado=self.estado-gastar
        break
        return self.estado
        

mi_wallet=Wallet() 
mi_wallet.__init__()