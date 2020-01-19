#Parsear el archivo blast
import pandas as pd

def leer_blast(archivo_entrada,query):
    """archivo_entrada=Resultado_blast_completo (archivo obtenido en blast)
    query=archivo con las querys
    datos=archivo con los datos filtrados por id, e-value y cov.
    """
    datos=pd.read_csv(archivo_entrada,delimiter='\t')    
    
    #El usuario puede elegir si quiere filtrar o dejarlo con los valores predeterminados
    pregunta=input("¿Quiere introducir el porcentaje de filtrado para identidad, evalue y coverage?[S/N]: ")

    if pregunta=="S" or pregunta=="s":
        id=float(input("¿Cuál es el porcentaje de identidad por el que desea filtrar?: "))
        cov=float(input("¿Cuál es el valor de coverage por el que desea filtrar?: "))
        evalue=float(input("¿Cuál es el valor de Evalue por el que desea filtrar?: "))
    else:
        id=85
        cov=30
        evalue=1e-2

    def ordena(datos):
        """Funcion para ordenar los datos
        datos=archivo Resultado_blast_completo abierto con pandas
        """
        datos =datos[(datos['Identidad'] >=id) & (datos['Cobertura'] >= cov) & (datos['Evalue'] <= evalue)]
        return 
    
    ordena(datos)
    return datos

def seleccion(datos,multifasta,querys):
    """datos=archivo con los datos filtrados
    multifasta=Archivo_multifasta.fasta (archivo que generamos en genbank como subject)
    querys=archivo que contiene las querys
    """

    #Hacemos una lista con los nombres de las querys que están en el archivo
    nombres_query=[]
    with open (querys,mode="r") as f:
        for linea in f:
            if linea[0]==">":
                nombres_query.append(linea[1:len(linea)-1])
        f.close()

    #Obtenemos los nombres de las query y de los subject con los que ha hecho hit
    nombres2=datos["Nombre_subject"]
    nombres1=datos["Nombre_query"]
    nombres1=list(nombres1[1:])
    nombres2=list(nombres2[1:])
 
    seleccion={}#diccionario querys:hits blast
    #Parseamos las listas para obtener el nombre de la query como clave
    #y como valor una lista con los subjects con los que ha hecho hit
    for i in range(len(nombres1)): 
        for x in range(len(nombres_query)):
            if nombres_query[x]==nombres1[i]:
                clave=nombres_query[x]
                valor=nombres2[i]
                if clave in seleccion:
                    seleccion[clave].append(valor)
                else:
                    seleccion[clave]=[valor]
    #Elimino valores duplicados en los valores
    for k, v in seleccion.items():
        nuevo=[]
        for item in v:
            if item not in nuevo:
                nuevo.append(item)
                seleccion[k] = nuevo

    #Contador para determinar si se encuentra en una linea con el nombre (>) o con la secuencia
    n=0
    #Contador para recorrer la lista con los nombres de las querys
    cuenta=0
    #Lista con los nombres de los archivos generados
    lista_nombres=[]
    for opciones in seleccion.items():
        abre_query=open(querys,"r")#Abrimos el archivo de las querys
        keys=seleccion.keys()#Generamos una lista con las keys del diccionario, que son las querys
        modifica=[]
        modifica1=[]
        modifica2=[]
        modifica3=[]

        nombre_archivo=opciones[0]
        with open (multifasta,mode="r") as f:
            with open(nombre_archivo,"w+") as archivo: #El nombre de cada archivo será el nombre de su query
                #Forma una lista con todos los hits de blast
                modifica2=opciones[1]
                
                # Forma una lista con el nombre de cada una de las querys
                for x in abre_query:   
                    if x[0]==">":
                        modifica1.append(x[1:len(x)-1])
                
                #En caso de que los hits que encuentra en blast no sean las query, las elimina
                eliminar=[item for item in modifica1 if item not in modifica2]
                for r in eliminar:
                    modifica1.remove(r)
                
                #Nos quedamos solamente con los hits que encontró en blast, quitando las querys
                modifica3 = [item for item in modifica2 if item not in modifica1]
                modifica3.sort()
                
                #genera la lista con todos los hits, incluidas las query
                if len(modifica1)<=len(keys):
                    modifica=modifica1+modifica3

                #Forma un archivo por cada query introducida, con los nombres y secuencias
                #que se obtuvieron en el blast
                for linea in f:
                    if cuenta==(len(modifica)):
                        break
                    if linea[1:(len(linea)-1)]==modifica[cuenta]:
                        archivo.write(linea)
                        n+=1
                    elif n==1 and linea[0]!=">":
                        archivo.write(linea)
                        cuenta+=1
                        n=0
                    else:
                        n=0
                lista_nombres=lista_nombres+[nombre_archivo] 
                archivo.close()
                n=0
                cuenta=0
            f.close()
        
            
     

    
    return lista_nombres