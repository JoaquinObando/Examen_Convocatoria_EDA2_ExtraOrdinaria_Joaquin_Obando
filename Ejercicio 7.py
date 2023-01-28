class arbol_huffman():
    def __init__(self, caracter,frecuencia,izq,der):
        self.caracter=caracter
        self.frecuencia=frecuencia
        self.izq=izq
        self.der=der
    def sub_izq (self):
        return self.izq
    def sub_der (self):
        return self.der
    def mayor (self,x):
        if self.frecuencia>x.frecuencia:
            return True
        elif self.frecuencia<x.frecuencia:
            return False
        elif self.caracter>x.caracter:
            return True
        elif self.caracter=="":
            return True
        elif x.caracter=="":
            return False
        else:
            return False
        
    def hoja (self):
        return self.izq == None and self.der==None
    
    def decodificar(self,mensaje):
        cadena=""
        i=0
        while i<len(mensaje):
            actual=self
            while i<len(mensaje):
                if actual.hoja():
                    break
                else:
                    if mensaje[i]=="0":
                        actual=actual.izq
                    else:
                        actual=actual.der 
                    i+=1
            cadena+=actual.caracter
           
        return cadena
    def generar (tabla):
        lista= []
        
        for i in tabla:
            a= arbol_huffman(i[0],i[1],None,None)
            iactual=len(lista)-1
            while iactual>=0 and a.mayor(lista[iactual]):
                iactual-=1
            lista.insert(iactual+1,a)
        
        while len(lista)>1:
            i=lista.pop()
            d=lista.pop()
            a=arbol_huffman("",i.frecuencia+d.frecuencia,i ,d)
            iactual=len(lista)-1
            while iactual>=0 and a.mayor(lista[iactual]):
                iactual-=1
            lista.insert(iactual+1,a)
        return lista[0]
    def tablaCodigos(self,c,t):
        if self.hoja():
            t[self.caracter]=c
        else:
            ci=c+"0"
            cd=c+"1"
            self.izq.tablaCodigos(ci,t)
            self.der.tablaCodigos(cd,t)
        return t
            

def main():
    tabla=[["A",0.2],["F",0.17],["1",0.13],["3",0.21],["0",0.05],["M",0.09],["T",0.15]]
    mensaje1="10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
    mensaje2="0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"
    arbol=arbol_huffman.generar(tabla)
    tablaHash={}  
    print (arbol.tablaCodigos("",tablaHash))
    cadena=""
    print (arbol.decodificar(mensaje1))
    print (arbol.decodificar(mensaje2))
if __name__ == "__main__":
    main()