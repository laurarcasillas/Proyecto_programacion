#Módulo blast
from subprocess import Popen, PIPE

def hacer_blast(query,subject,nombre_resultado):
    """query=archivo que contiene la(s) query(s)
    subject=Archivo_multifasta.fasta que se generó en el módulo genbank
    nombre_resultado=Resultado_blast_completo -> archivo que contiene el resultado
    """
    #Se realiza un blast múltiple (si hay query múltiple), con subject obtenido del modulo genbank (incluye las querys)
    blast = Popen(['blastp','-query',query,'-subject',subject,'-outfmt',"6 qseqid sseqid qcovs pident evalue" ], stdout=PIPE, stderr=PIPE)
    error_encontrado = blast.stderr.read()
    leer_blast = blast.stdout.read()

    blast.stderr.close()
    blast.stdout.close()
    
    with open(nombre_resultado,mode="w+") as fichero:
        cabeceras=["Nombre_query","Nombre_subject","Cobertura","Identidad","Evalue",] #Se incluyen cabeceras al archivo
        for i in cabeceras:
            fichero.write(i+"\t")
            if i=="Evalue":
                fichero.write('\n')
        fichero.write(leer_blast.decode('utf-8')) #Se incluyen los resultados obtenidos del blast
        fichero.close()

    return nombre_resultado



