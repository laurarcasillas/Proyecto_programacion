#Modulo Muscle
from subprocess import Popen, PIPE


def hacer_alineamiento(lista_nombres):
    """lista_nombres=lista que contiene los nombres de los archivos que se han generado en parsear
    archivos_muscle=lista con los nombres de los archivos obtenidos al alinear
    """
    
    archivos_muscle=[]
    for i in lista_nombres:
        alinea = ['muscle','-in',i,'-out',(i+"_alinea_muscle")]
        hacer=Popen(alinea,stdout = PIPE)
        hazlo=hacer.stdout.read()
        hacer.stdout.close()
        archivos_muscle.append(i+"_alinea_muscle")#El nombre del archivo del alineamiento será el obtenido
                                                #en parsear seguido _alinea_muscle
    
    return archivos_muscle

def hacer_arbol(alineamiento):
    """alineamiento=recibe la lista con los nombres de los archivos alineados en la función anterior
    archivos_arboles=lista con los nombres de los archivos con los árboles generados
    """

    archivos_arboles=[]

    for i in alineamiento:
        arbol=['muscle','-maketree','-in',i,'-out',(i+"_arbol.phy"),'-cluster','neighborjoining']
        hacer=Popen(arbol,stdout= PIPE)
        lectura=hacer.stdout.read()
        hacer.stdout.close()
        archivos_arboles.append(i+"_arbol.phy")#El nombre del archivo será igual al que tienen
                                                #+ _arbol.phy
    
    return archivos_arboles
