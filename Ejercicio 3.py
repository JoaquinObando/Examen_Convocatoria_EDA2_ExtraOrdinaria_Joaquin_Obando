from datetime import datetime

class  ArtefactosValiosos:

    def __init__(self,peso,nombre,precio,fecha):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha = fecha
        print("Conserva creada con éxito")
    
    def __str__(self):
        return "Nombre: "+ self.nombre+", Peso: "+str(self.peso)+", Precio: "+str(self.precio)+", Fecha: "+self.fecha
    
x = ArtefactosValiosos(200, "A1", 18, "25/1/2023")
y = ArtefactosValiosos(368, "A2", 26, "21/4/2023")
z = ArtefactosValiosos(189, "A3", 48, "20/2/2023")

lista = []
lista.append(x)
lista.append(y)
lista.append(z)


lista.sort(key=lambda a:datetime.strptime(a.fecha, "%d/%m/%Y"))

for a in lista:
    print(a)

y.precio = 1700

for a in lista:
    print(a)

#Ordenado por fecha de caducidad