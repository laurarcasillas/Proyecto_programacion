#Modulo prosite
import re
from Bio.ExPASy import Prosite,Prodoc

def blast_prosite(querys,blast_filtrado,multifasta):
    """Funcion para extraer nombre+secuencia de los hits de blast
    querys=archivo que contiene las querys
    blast_filtrado=archivo con las secuencias que se ha filtrado en blast
    multifasta=archivo filtro.fasta que se obtuvo en genbank
    """
    #abre el archivo que contiene las querys
    abre_query=open(querys,"r")
    nombres_query=[]
    for x in abre_query:#almaceno los nombres de las query en la lista nombres_query
        if x[0]==">":
            nombres_query.append(x[1:len(x)-1])
    abre_query.close()

    nombres1=blast_filtrado["Nombre_subject"].unique()#se obtienen los nombres de los subjects obtenidos en blast

    nombres2=[item for item in nombres1 if item not in nombres_query]#se seleccionan los nombres que no son las querys
    
    nombres2.sort()#se ordenan
    nombres=nombres_query+nombres2#se le añaden al inicio los nombres de las query a los subjects ordenados
    
    with open (multifasta,mode="r") as f:#abrimos el archivo multifasta
        filtrado=open("filtro.fasta", "w")#abrimos el archivo donde se encuentran filtrados los resultaods de blast
        
        #Contador para determinar si se encuentra en una linea con el nombre (>) o con la secuencia
        n=0
        #Contador para recorrer la lista con los nombres de las querys
        cuenta=0
        for linea in f:
            #Forma el archivo multifasta con el nombre de cada proteina seguido de su secuencia
            #obtenidos en el archivo que ha sido filtrado de blast
            if cuenta==(len(nombres)):
                break
            if linea[1:(len(linea)-1)]==nombres[cuenta]:
                filtrado.write(linea)
                n+=1
            elif n==1 and linea[0]!=">":

                filtrado.write(linea)
                cuenta+=1
                n=0
            else:
                n=0
        filtrado.close()
        f.close()
        
    return filtrado


def encuentra(filtrado):
    """Funcion para extraer las listas con las diferentes caracteristicas que queremos
    obtener para la formacion del archivo prosite, parseando tanto .doc como .dat para obtenerla
    """
    #lista con los patrones a buscar en el archivo "filtro.fasta"
    patrones=[]
    #lista de los nombres de los dominios en prosite
    nombres_prosite=[]
    #lista de la descripcion
    descripcion=[]
    #lista de los accession
    accesion=[]
    handle = open("prosite.dat","r")
    records = Prosite.parse(handle)
    for record in records:
        patrones.append(record.pattern)
        nombres_prosite.append(record.name)
        accesion.append(record.accession)
        descripcion.append(record.description)
    handle.close()
  
    #Modificacion de la lista patrones para buscarlo con re
    for numero in range(len(patrones)):
        if numero<=(len(patrones)-1):
            valor=patrones[numero][:-1]
   
            for letra in valor:
                if letra=="x" or letra=="X":
                    valor=valor.replace("x",".").replace("X",".")
                if letra=="{" or letra=="}":
                    valor=valor.replace("{","[^").replace("}","]")
                if letra=="(" or letra==")":
                    valor=valor.replace("(","{").replace(")","}")

                if letra=="-":
                    valor=valor.replace("-","")
                    patrones[numero]=valor
    return busca(filtrado,patrones,nombres_prosite,accesion,descripcion)

def busca(multifasta_filtrado,lista,nombres,accesion,descripcion):
    """Funcion que formara un diccionario que tendra como clave el patron y como valor una lista
    en la que se incluyen la linea del nombre del archivo multifasta con el que coincide buscando con re
    """
    #diccionario patron:linea con el nombre procedente del archivo multifasta con la que coincide
    matches=dict()
    for i,patron in enumerate(lista):
        with open (multifasta_filtrado,mode="r") as read:
            for x,linea in enumerate(read):
                if linea[0]!=">":
                    if re.search(patron,linea):
                        x-=1
                        if x in matches:
                            matches[x].append(i)
                        else:
                            matches[x]=[i]
            read.close()
    
    return escribe_archivo(multifasta_filtrado,lista,matches,nombres,accesion,descripcion)
    
def escribe_archivo(multifasta,lista,dicc,nombres,accesion,descripcion):
    """Funcion que almacenara en "Archivo_prosite" la informacion de cada una de las secuencias
    que se han filtrado en blast
    multifasta_filtrado=archivo obtenido en la primera funcion de este modulo
    lista=lista con los patrones
    dicc=diccionario creado patron:linea
    nombres= lista nombres de prosite
    accesion=lista con los accession de prosite
    descripcion=lista con las descripciones
    """
    lee=open(multifasta,"r")
    #diccionario texto del archivo .doc: referencias del archivo .doc
    referencias=dict()
    handle = open("prosite.doc", encoding="utf8",errors="ignore")
    records = Prodoc.parse(handle)
    for record in records:
        
        valor=record.prosite_refs
        texto=record.text
        referencias[texto]=valor
    

    with open ("Archivo_prosite",mode="w+") as escribir:#Archivo que se creara
        for x,linea in enumerate(lee):
            for i in dicc.keys():
                if x==i:
                    escribir.write(linea)
                    
                    for valor in dicc.values(): #recorre el diccionario por los valores
                        for posicion in valor: #saca el numero
                            for patron in range(len(lista)):#recorre la lista de los patrones
                                
                                if patron==posicion:
                                    if lista[patron]!="":#debido a que hay varios patrones vacios, cuyo resultado es ""
                                                            #asi solamente buscara patrones que tengan contenido
                                        escribir.write("El nombre es: "+nombres[patron]+"\n")
                                        escribir.write("El accession es: " +accesion[patron]+"\n")
                                        escribir.write("El patron es: "+lista[patron]+"\n")
                                        escribir.write("La descripción es: "+descripcion[patron]+"\n")
                                        for v in referencias.items():
                                            for i in v[1]:
                                                for x in i:
                                                    if x==accesion[patron]:
                                                        escribir.write("Información adicional: \n"+v[0])
                                                        #La siguiente linea nos permitira realizar la separacion de cada uno de los resultados
                                                        escribir.write("---------------------------------------------------------------------------------------------------------------------------------\n")
                else:
                    break
    lee.close()
    escribir.close()

    return


