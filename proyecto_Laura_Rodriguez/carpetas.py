#Modulo que crea la carpeta y subcarpetas que almacenarán los archivos obtenidos en el programa
import os

def crea_carpetas(nombre):
    current_directory= os.getcwd()

    os.mkdir(nombre,0o777)
    
    path=os.chdir(nombre)
    
    os.mkdir("data",0o777)
    os.mkdir("scripts",0o777)
    os.mkdir("results",0o777)

    #Dentro de la carpeta results, genero otras subcarpetas para ordenar las 
    #salidas de cada una de las funciones que se usan en el programa
    os.mkdir("results/blast",0o777)
    os.mkdir("results/muscle",0o777)
    os.mkdir("results/prosite",0o777)

    return
