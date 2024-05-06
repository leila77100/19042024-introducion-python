#Exercicio para registrar la nota de los alumnos 

class Alumno:
    def __init__(self):
        self.alumnos = dict(
            nombre ="",
            apellido=""
        )
        self.material=dict(
            curso="",
            notas= []
        )
    
        
    def nuevo_alumno(self, nombre, apellido):
        self.alumnos["nombre"]=nombre
        self.alumnos["apellido"]=apellido
        print(self.alumnos)
        
    
    def nota(self, asignatura, nota):

        if asignatura in self.material[asignatura]:
             self.material[asignatura].append(nota)
        else:
             self.material[asignatura]=[nota]
        


lista_alumno=Alumno()

pregunta= input("press 1 si quieres añadir un nuevo alumno o 2 por añadir una nota" ) 
while pregunta == "1":
    pregunta = True
    lista_alumno.nuevo_alumno("leila", "sida")
    pregunta= input("press 1 si quieres añadir un nuevo alumno o 2 por añadir una nota" ) 


while pregunta== "2":
    pregunta = False
    lista_alumno.nota()
    pregunta= input("quieres entrar una nueva nota?pulsa 2" ) 

#otro ejemplo

class Alumno:
    def __init__(self):
        self.notas = []
    def registrar_nota(self,nota):
        self.notas.append(nota)
    def media_alumno(self):
            media = sum(self.notas) / len(self.notas)
            #Redondea números con 2 decimales
            return round(media, 2)
    def max_nota(self):
        #return max(self.notas)
        max = 0
        for x in self.notas:
            if max < x:
                max = x
        return max
alumno = Alumno()
i = 0
while i < 5:
        nota = float(input("Introduce la nota del alumno"))
        if 0 <= nota <= 10:
            alumno.registrar_nota(nota)
            i += 1
print("La media de las notas del alumno es: ", alumno.media_alumno())
print("La máxima nota del alumno es: ", alumno.max_nota())       
