#Metodo diccionarios
#Es un objeto que tien una llave con una valor , el indicio es un texto car["modelo"]
#los diccionarios permiten utilizar una clave para declarar y acceder a un valor

thisdict ={
    "brand": "Ford",
    "model":"Mustang",
    "year": 1994
}

#imprime la volor gracias a la llave
print(thisdict["model"])
#elimina cualquier entrada
del(thisdict["brand"])
print(thisdict)
#Aparece {'model': 'Mustang', 'year': 1994}

#abre una ventana
clave=input("dime que quieres saber")
#hasta que la condicion se cumple la bucle funciona 
while clave not in thisdict:
    print("no conozco esa clave")
    clave=input("dime que quieres saber")
print(thisdict[clave])

#añadir una valor
thisdict["brand"] = "renault"
print(thisdict)
#affectar una lista a una llave
thisdict["model"]=[1,2,3,5,7,8]
#llamar el tercero elemento (7)
print(thisdict["model"][3])

#crear un constructeur 
thisdict = dict(
    brand= "Ford",
    model="Mustang",
    year= 1994
)
#metodo get()que te permite de buscar una clave, el segundo parametro te permite de dar un mensaje cuando el programo no encontro la clave
print(thisdict.get("brand", "no existe esa clave"))

#metodo keys() te permite de muestrar las claves disponible del dictionary
#para leer una lista dentro una ventana se puede poner str(lista)
print(thisdict.keys())

#te permite de parcurir la lista y te sale la llave con la valor
  
for x, y in thisdict.items():
    print(x," - ", y)