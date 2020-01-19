import sys
import os
import pandas as pd
import shutil
import carpetas
import genbank
import blast
import parsear
import muscle
import prosite
import ayuda

if len(sys.argv)>1:
    try:
        if sys.argv[1]=="-h" or sys.argv[1]=="--help":
            ayuda.help()
            sys.exit()
    except:
        sys.exit()

#Pide el nombre de la carpeta, así el usuario usa el programa el numero de veces que quiera
nombre_carpeta=input("Introduzca el nombre de la carpeta en el que desea guardar el trabajo: ")
current_directory= os.getcwd()
#Comprueba que el nombre elegido no se encuentre ya en el directorio
while nombre_carpeta in os.listdir(current_directory):
    print("La carpeta ya está creada, prueba a ponerle otro nombre")
    nombre_carpeta=input("Introduzca el nombre de la carpeta en el que desea guardar el trabajo: ")
else:
    carpetas.crea_carpetas(nombre_carpeta)

#Volver al directorio principal para buscar el archivo y copiarlo en data
path=os.chdir(current_directory)

#Pide el archivo query que quiere usar el usuario
archivo_query=input("Introduzca un solo archivo query que va a usar con la extensión .fasta o .fas: ")
copiar=shutil.copy(archivo_query, (nombre_carpeta+"/data/"+archivo_query))

#Comprueba si es fasta
if archivo_query[-6:]==".fasta" or archivo_query[-3:]==".fa":
    querys=archivo_query
else:
    print("Lo siento, el archivo introducido no es formato fasta")


genbanks=[]#Lista para incluir los genbanks que el usuario desee
#Pide el número primero
numero_genbank=int(input("Introduzca el número de archivos genbank que desee usar: "))

while numero_genbank!=0:
    archivo_genbank=input("Introduzca un solo archivo genbank que va a usar: ")#Va pidiendo los genbank 1 a 1 para almacenarlos en la lista
    if archivo_genbank[-5:]==".gbff" or archivo_genbank[-4:]==".seq":
        copia_genbank=shutil.copy(archivo_genbank,(nombre_carpeta+"/data/"+archivo_genbank))
        genbanks.append(archivo_genbank)
        numero_genbank-=1
    else: 
        print("Lo siento, el archivo introducido no es formato Genbank")

#Abro el archivo que vamos a usar como subject para blast
with open ("Archivo_multifasta.fasta", mode="w+") as output:
    #Llamadas al modulo genbank para generar el archivo multifasta(subject)
    genbank.introducir_query(archivo_query,output)
    genbank.obtener_multifasta(genbanks,output)

    output.close()


#Llamada al modulo blast para hacerlo
blast.hacer_blast(archivo_query,"Archivo_multifasta.fasta","Resultado_blast_completo")

print(chr(27)+"[1;33m"+"Blast se ha realizado con éxito, el archivo lo encontrará en: "+ nombre_carpeta+"/results/blast"+"\n"+chr(27)+"[0m")

#Llamada el modulo parsear: para sacar los resultados de blast
ordenado=parsear.leer_blast("Resultado_blast_completo",archivo_query)#Ordenado es la variable que contiene
                                                                    #los datos sacados de blast filtrados
lista_nombres_blast=parsear.seleccion(ordenado,"Archivo_multifasta.fasta",archivo_query)#Devuelve la lista de los nombres
                                                                                        #de los archivos que genera, en caso
                                                                                        #de hacer un blast multiple

#Llamadas al modulo muscle
alineamiento=muscle.hacer_alineamiento(lista_nombres_blast)#devuelve una lista con los archivos ya alineados
print(chr(27)+"[1;33m"+"El alineamiento en muscle se ha realizado con éxito, el archivo lo encontrará en: "+ nombre_carpeta+"/results/muscle"+"\n"+chr(27)+"[0m")

arboles=muscle.hacer_arbol(alineamiento)#devuelve una lista con los archivos que contienen los arboles obtenidos
print(chr(27)+"[1;33m"+"El/los árboles se han realizado con éxito, el archivo lo encontrará en: "+ nombre_carpeta+"/results/muscle"+"\n"+chr(27)+"[0m")

#Llamadas al modulo prosite
prosite.blast_prosite(archivo_query,ordenado,"Archivo_multifasta.fasta")
prosite.encuentra("filtro.fasta")
print(chr(27)+"[1;33m"+"Se ha extraído la información de la base de datos de prosite de los matches, el archivo lo encontrará en: "+ nombre_carpeta+"/results/prosite"+"\n"+chr(27)+"[0;37m")



#Muevo los diferentes archivos generados a las carpetas correspondientes
mover=shutil.move("Archivo_multifasta.fasta", (nombre_carpeta+"/results/Archivo_multifasta.fasta"))
mover2=shutil.move("Resultado_blast_completo", (nombre_carpeta+"/results/blast/Resultado_blast_completo"))
mover3=shutil.move("filtro.fasta", (nombre_carpeta+"/results/blast/filtro.fasta"))
mover4=shutil.move("Archivo_prosite", (nombre_carpeta+"/results/prosite/Archivo_prosite"))
mover5=shutil.copy("prosite.dat", (nombre_carpeta+"/data/prosite.dat"))
mover6=shutil.copy("prosite.doc", (nombre_carpeta+"/data/prosite.doc"))

#Mover los archivos del alineamiento de muscle
for x in os.listdir(current_directory):
    for s,arbol in zip(alineamiento,arboles):
        if x==s or x==arbol:
            mueve=shutil.move(x, (nombre_carpeta+"/results/muscle/"+x))


#Mover los archivos del resultado de blast
for archivo in os.listdir(current_directory):
    for nombre in lista_nombres_blast:
        if archivo==nombre:
            mueve=shutil.move(archivo, (nombre_carpeta+"/results/blast/"+archivo))


mover_modulo=shutil.copytree("proyecto_Laura_Rodriguez",(nombre_carpeta+"/scripts/proyecto_Laura_Rodriguez"))
