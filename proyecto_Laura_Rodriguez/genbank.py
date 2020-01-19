#Módulo Genbank
from Bio import Seq
from Bio import SeqIO



def obtener_multifasta(archivo_entrada,archivo_salida):
    #parser para la obtención de cada una de las secuencias subject y de su id
    for i in archivo_entrada:

        for record in SeqIO.parse(i,"genbank"):
            print()

        for feature in record.features:
            if feature.type =="CDS":
                inicio=(">"+feature.qualifiers['protein_id'][0])
                proteina=(feature.qualifiers['translation'][0]+"\n")

                total=(inicio+"\n"+proteina)
                print (total, file=archivo_salida)
        
    archivo_salida.close()
    return archivo_salida

def introducir_query(lista_query,archivo_salida):
    #Función que introduce las query en el archivo subject, para hacer un blast múltiple
    with open(lista_query, mode="r") as query:
        for linea in query:
            if linea[0]==">": #Busca los nombres
                archivo_salida.write(linea)#Escribe los nombres
                
            if linea[-1]=="\n" and linea[0]!=">":#Busca las secuencias
                #Se generan dos variables que incluiran las 2 lineas que pudiese contener en caso de salto de linea
                #Lo elimina y las junta
                DAN=linea.rstrip("\n")
                DAN2=linea.rstrip("\n")
                total=DAN+DAN2
                
                archivo_salida.write(total+"\n")

    return archivo_salida




