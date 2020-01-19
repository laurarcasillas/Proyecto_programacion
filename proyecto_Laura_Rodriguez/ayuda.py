def help():
    dar_bienvenida="""Bienvenido a la ayuda del programa. A continuación, se le expondrán los diferentes pasos que debe seguir para su
uso, así como las diferentes funciones que le puede aportar."""
    print(chr(27)+"[1;33m"+dar_bienvenida.center(100)+chr(27)+"[0m")
    print("""-Nombre con el que desea formar la carpeta donde se almacenarán los resultados.
Permite que el usuario pueda correr el programa el número de veces que quiera, siempre que la carpeta no reciba el nombre de otra ya
previamente formada.""")
    print("-Introduzca un archivo query: puede contener tanto una como varias querys." 
+chr(27)+"[1m"+"\n"+"Este archivo debe tener la extensión .fasta o .fa"+chr(27)+"[0m")
    print("""-Número de archivos genbank que desea introducir. Deberá escribirse
un número a partir del 1 y después le pedirá el/los archivos.""")
    print("""-Escribir cada uno de los archivos genbank, siendo importante que los escriba
uno por uno, para que luego el programa pueda realizar su función."""+chr(27)+"[1m"+"\n"+
"Es importante que estos archivos tengan la extensión .gbff"+chr(27)+"[0m"+"\n")
    print(chr(27)+"[1;32m"+"Función de Blast: "+chr(27)+"[0m")
    print("""La query que usará es el archivo introducido incialmente que puede contener una o varias querys. Estas
se introducirán en el subject.
El subject es un archivo multifasta formado con las secuencias extraídas de los archivo/archivos genbank que introduzca.\n
-Se filtrarán los valores por identidad, coverage y e-value. Si el usuario quiere, puede introducir sus valores, sino tendrán por defecto 85,30 y 1e-2, respectivamente.\n
-En caso de tener"""+chr(27)+"[1m"+" una sola query"+chr(27)+"[0m"+""": se formará solamente un archivo llamado "filtro.fasta" con los hits ya filtrados.
-En caso de tener"""+chr(27)+"[1m"+" varias querys"+chr(27)+"[0m"+""": se formarán tantos archivos como querys haya y tendrán el mismo nombre de las querys.\n
TODOS LOS ARHCIVOS SERÁN ALMACENADOS EN LA CARPETA CREADA POR EL USUARIO EN EL SIGUIENTE APARTADO: nombre_carpeta/results/blast.\n """)
    print(chr(27)+"[1;32m"+"Función Muscle: "+chr(27)+"[0m")
    print("""-En caso de tener"""+chr(27)+"[1m" +"una sola query"+chr(27)+"[0m"+""": en primer lugar, se realizará el alineamiento con muscle para que seguidamente, con estos
pueda llevar a cabo la obtención del árbol.

-En caso de tener"""+chr(27)+"[1m"+" varias querys"+chr(27)+"[0m"+""": con los diferentes archivos obtenidos en blast, se llevará a cabo el alineamiento de cada uno de ellos,
recibiendo el nombre de "nombrequery_alineamiento". A continuación, de cada uno de ellos formaremos un árbol que será almacenado con el nombre
anterior seguido de "_arbol.phy".\n""")
    print(chr(27)+"[1;32m""Función Prosite: "+chr(27)+"[0m")
    print("""Los archivos prosite.dat y prosite.doc adjuntados permitirán que de los hits obtenidos en blast, se pueda obtener más información sobre ellos de la base de datos
de Prosite. Es IMPORTANTE que ambos archivos se encuentren en la misma carpeta donde se corre el programa, donde al igual encontrará el archivo query y el/los archivos
genbank.
-El resultado se obtendrá en "nombre_carpeta/results/prosite". """)
    print("""Además, tanto el archivo query como el/los archivos genbank se copiarán a "nombre_carpeta/data". Y el módulo será introducido en "nombre_carpeta/scripts". """)
    return