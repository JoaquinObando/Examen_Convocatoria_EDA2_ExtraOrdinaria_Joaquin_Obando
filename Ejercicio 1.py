class Armaduras:

    def __init__(self,nombre, rango):
        self.nombre =  nombre
        self.rango = rango
        print("Armaduras creado con éxito")

    def calificacion(self):

        codigoFinal = self.nombre.split('-')

        codigoLegion = codigoFinal[0]
        print("Código Legión: ",codigoLegion)

        idCiherente = codigoFinal[1][0]
        print("ID Ciherente: ",  idCiherente)
        
        idSiglo = codigoFinal[1][1]
        print("ID SIglo: ",  idSiglo)

        numArmadura = codigoFinal[1][2]
        print("Número Armadura: ",  numArmadura)

        numEscuadra = codigoFinal[1][3]
        print("Num Escuadra: ",  numEscuadra)


lista = []


s = Armaduras("MK-8888",10)

x = Armaduras("BM-9876",21)

z = Armaduras("NJ-2587",35)


lista.append(s)
lista.append(x)
lista.append(z)

for st in lista:
    st.calificacion()
    print("\n")
