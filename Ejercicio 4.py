class mochila ():
    def __init__ (self ):
        self.objetos = []
    def __str__ (self):
        return str(self.objetos)
    def __len__ (self):
        return len(self.objetos)
    def Hijo_sin_Amor (self, i=0):
        if i == len(self.objetos):
            return "No hay anillo de poder"
        elif self.objetos[i] == "anillo de poder":
            return "El anillo de poder está en la posición " + str(i+1) + " de la mochila"
        else:
            return self.Hijo_sin_Amor(i+1)
    def agregar_objeto (self, objeto):
        self.objetos.append(objeto)

mochila_Namor = mochila()
mochila_Namor.agregar_objeto("blaster")
mochila_Namor.agregar_objeto("anillo de poder")




print(mochila_Namor)
print(mochila_Namor.Hijo_sin_Amor())
 