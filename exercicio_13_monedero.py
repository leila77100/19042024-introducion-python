class Monedero:
    def __init__(self):
        self.saldo = 0
  
    
    def gastar_dinero(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo = self.saldo - cantidad
            return f"Has gastado {cantidad} euros. Saldo restante: {self.saldo} euros"
        else:
            return "No hay suficiente saldo en el monedero"
        
    def ingresar_dinero(self, cantidad):
        self.saldo=self.saldo = self.saldo+cantidad
        return f"Has ingresado {cantidad} euros. Saldo total: {self.saldo} euros"
    
class Monedero_infantil(Monedero):
    #creation d un constructeur pour la class enfant
    def __init__(self,lim=50):
        self.limite=lim
        super().__init__()
    
    def cambiar_limite(self,nuevo):
        self.limite=nuevo
        return f"se ha cambiado la limite a {self.limite} € "

  

    def gastar_dinero(self, cantidad):
        if cantidad>self.limite:
            return f"el importe del gasto no puede superar a  {self.limite} € "
        else:
            return super().gastar_dinero(cantidad)

        
tipo=int(input("tipo de monedero: 1-general, 2-infantil "))

if tipo==1:
    cartera=Monedero()
else:
    cartera=Monedero_infantil()
opcion=0
while opcion!=5:
    print("1- ingresar dinero")
    print("2- gastar dinero")
    print("3- ver saldo")
    #cindicion para saber cual es el nombre del objeto
    if isinstance(cartera, Monedero_infantil):
    #if cartera.__class__.__name__=="Monedero_infantil":
        print("4- limite de gasto")
        print("5- salir")
    else:
        print("4- salir")
    opcion =int(input("dime una opcion"))
    if opcion==1:
        cantidad=float(input("Ingrese la cantitad: "))
        print(cartera.ingresar_dinero(cantidad))
    elif opcion==2:
        cantidad=float(input("Gastar la cantitad: "))
        print(cartera.gastar_dinero(cantidad))
    elif opcion==3:
        print("su saldo es: ",cartera.saldo)
    elif opcion==4:
        try:
            nuevo_limite=float(input("introduzca el nuevo limite de gasto"))
            print(cartera.cambiar_limite(nuevo_limite))
        except:
            print("operacion no permitida")
    elif opcion==5:
        print("finalizacion del programa")
    else:
        print("opcion no disponible")
        