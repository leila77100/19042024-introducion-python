# ----programacio orienta a objeto--------------------------------------------------------
# ejercicio  9 

# def abrir_puerta(id_puerta, estado, grados):
#     if estado(abierta):
#         return "la puerta ya estaba abierta","abierta",grados
#     else:
#         while grados <=90:
#             grados += 1
#         return "Puerta abierta","abierta",grados
    
# mi_puerta=1
# estado_puerta1= "cerrado"
# grados_perta1=0

# mensaje, estado_puerta1, grados_perta1= abrir_puerta(mi_puerta,estado_puerta1,grados_perta1)


# ---------------------------------------------------------

class Puerta():
    def __init__(self):
        self.estado=" cerrado"
        self.grados=0
    def abrir_puerta(self):
        if self.estado=="abierta":
            return "La puerta ya estaba abierta"
        else:
            while self.grados <= 90:
                    self.grados +=1
                    self.estado= "abierta"
            return "La puerta abierta"
    def estadopuerta(self):
         return str(self.estado)
        
mi_puerta= Puerta()
print(mi_puerta.abrir_puerta())
print(mi_puerta.estadopuerta())







