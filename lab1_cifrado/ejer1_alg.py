#NO ESTÁ DEL TODO CORRECTO

mensaje = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE"
frecuencias = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
frecCast = [('e',16.78),('a',11.96),('o',8.69),('l',8.37),('s',7.88),('n',7.01),('d',6.87),('r',4.94),('u',4.8),('i',4.15),('t',3.31),('c',2.92),('p',2.776),('m',2.12),('y',1.54),('q',1.53),('b',0.92),('h',0.89),('g',0.73),('f',0.52),('v',0.39),('j',0.3),('ñ',0.29),('z',0.15),('x',0.06),('k',0),('w',0)]

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

def obtenerMaxs():
    lista = list(frecuencias.items())
    lista.sort(key=lambda frec: frec[1], reverse=True)
    return lista


def reemplazar(lista):
    mensaje1=mensaje
    validado=False
    elem2=0

    for elem in lista:
        validado=False
        while(validado==False):
            mensaje1=mensaje1.replace(elem[0],frecCast[elem2][0])
            print("Se ha sustituido la '" + elem[0] + "' por la '" + frecCast[elem2][0] + "'")
            print(" ")
            print(mensaje1)
            print(" ")
            validation = input("[Y/N] estáś de acuerdo? ")
            if validation=='Y':
                validado=True                

            elem2+=1
    
        print(" ")
        print("***********************************************************************************")
    
    #print(mensaje1)



obtenerFrecuencias()
reemplazar(obtenerMaxs())
            

