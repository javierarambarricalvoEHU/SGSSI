mensaje = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE"
frecuencias = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}

"""class letraFrec:
    def __init__(self, pLetra, pApariciones):
        self.letra = pLetra
        self.frec 
        self.numApariciones = pApariciones 

    def sumarApariciones(self):
        self.numApariciones = self.numApariciones +1
    
    def setNumApariciones(self, num):
        self.numApariciones = num

    def getLetra(self):
        return self.letra
"""

def obtenerFrecuencias():
    total = 0
    i = 0

    for j in mensaje:
        ascii = ord(mensaje[i])
        if (ascii <= 90 and ascii >= 65):
            frecuencias[mensaje[i]]+=1
            total+=1
        i+=1
    
    for j in frecuencias:
        frecuencias[j] = (frecuencias[j]/total)*100

    """for i in frecuencias:
        print(i)
        print(frecuencias[i])
    """

def obtenerMaxs():
    lista = list(frecuencias.items())
    lista.sort(key=lambda frec: frec[1], reverse=True)
    
    """
    max = 'A'
    max2 = 'B'
    aux = ''

    if frecuencias[max]<frecuencias[max2]:
        aux = max
        max = max2
        max2 = aux

    for i in frecuencias:
        if frecuencias[i]>frecuencias[max]:
            aux = max
            max = i
            max2 = aux
        elif frecuencias[i]>frecuencias[max2]:
            max2 = i
    """

    reemplazar(lista)

def reemplazar(lista):
    mensaje1 = mensaje.replace(lista[0][0],"e") #OK
    mensaje1 = mensaje1.replace(lista[1][0],"a") #OK
    
    mensaje1 = mensaje1.replace("T","l") #OK
    mensaje1 = mensaje1.replace("N","s") #OK
    mensaje1 = mensaje1.replace("A","d") #OK
    mensaje1 = mensaje1.replace("R","c") 
    mensaje1 = mensaje1.replace("J","n") #OK
    mensaje1 = mensaje1.replace("K","r") #OK 
    mensaje1 = mensaje1.replace("C","i") #OK 
    mensaje1 = mensaje1.replace("D","p") #OK 
    mensaje1 = mensaje1.replace("Z","u") #OK
    mensaje1 = mensaje1.replace("H","t") #OK
    mensaje1 = mensaje1.replace("U","g") #OK   
    mensaje1 = mensaje1.replace("I","o") #OK 
    mensaje1 = mensaje1.replace("O","f") #OK 
    mensaje1 = mensaje1.replace("S","q") #OK 
    mensaje1 = mensaje1.replace("P","m") #OK 
    mensaje1 = mensaje1.replace("Q","b") #OK 
    mensaje1 = mensaje1.replace("P","m") #OK 
    mensaje1 = mensaje1.replace("M","h") #OK 
    mensaje1 = mensaje1.replace("G","j") #OK 
    mensaje1 = mensaje1.replace("F","x") #OK 
    mensaje1 = mensaje1.replace("V","y") #OK 
    mensaje1 = mensaje1.replace("L","z") #OK 

    print(mensaje1)



obtenerFrecuencias()
obtenerMaxs()
            

