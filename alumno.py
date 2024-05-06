class Alumno:
    def __init__(self):
        self.nombre=""
        self.lista_notas={"matemáticas":[],"lengua":[]}

    def registrar_nota(self,asignatura,nota):
        if asignatura in self.lista_notas:
               self.lista_notas[asignatura].append(nota)
        

    def media_alumno(self,asignatura):
        media=0.0
        if asignatura in self.lista_notas and len(self.lista_notas[asignatura])>0:
                media=sum(self.lista_notas[asignatura])/len(self.lista_notas[asignatura])
        return round(media,2)

    def max_alumno(self,asignatura):
        maximo=0.0
        if asignatura in self.lista_notas and len(self.lista_notas[asignatura])>0:
           maximo= max(self.lista_notas[asignatura])
        return maximo

    def calificacion(self,asignatura):
        if asignatura in self.lista_notas and len(self.lista_notas[asignatura])>0:
            media=self.media_alumno(asignatura)
            calificacion=""
            if media==10:
                calificacion="matricula de honor"
            elif media >=9:
                calificacion="sobresaliente"
            elif media >=7:
                calificacion="notable"
            elif media >=6:
                calificacion="bien"
            elif media >=5:
                calificacion="suficiente"
            else:
                calificacion="insuficiente"
        else:
            calificacion="no se puede calificar"
        return calificacion


    


mialumno=Alumno()
nota=10
while nota!=-1:
    asignatura=input("dime la asignatura: ")
    nota=float(input("dime una nota del alumno"))
    if 0 <= nota <= 10:
        mialumno.registrar_nota(asignatura,nota)
for asignatura in mialumno.lista_notas:
    print("la media de las notas del alumno en la asignatura de",asignatura," es ",mialumno.media_alumno(asignatura))
    print("la calificación del alumno es ",mialumno.calificacion(asignatura))
    print("la máxima nota del alumno en la asignatura de",asignatura," es ",mialumno.max_alumno(asignatura))               

        


