# Proyecto_programacion
Paquete diseñado para encontrar hits en Blast, un alineamiento y árbol filogenético en Muscle y obtener mayor información de los hits de Blast gracias a la base de datos de Prosite.

Este programa funciona de la siguiente manera:
#
-->En primer lugar, se ejecutará el módulo main.py a partir del cual se van a ir ejecutando secuencialmente el resto de módulos creados.

-El programa pedirá un nombre para ponerle a una carpeta que permitirá que el usuario pueda correr el programa cuantas veces quiera, siempre que no exista otra carpeta o archivo con ese nombre.

-Además, pedirá un archivo query que puede contener tanto una como varias secuencias. Es importante que este archivo tenga la extensión .fa o .fasta, debido al control de errores.

-En último lugar, pedirá al usuario el número de archivos genbanks que desea usar, donde se escribirá el número y a continuación, los irá pidiendo uno a uno. Es muy importante solamente introducir uno cuando lo pida, sino el programa no funcionará correctamente. Es importante que este archivo contenga la extensión .gbff para que el programa funcione correctamente.
#
-->En segundo lugar, a partir del archivo o archivos genbank, generará un archivo multifasta que usará como subject en el Blastp. Este archivo también contendrá las querys y se almacenará en "nombre_carpeta/results" con el nombre de "Archivo_multifasta.fasta".
#
-->En tercer lugar, se ejecuta el Blastp del archivo query frente al subject generado en el segundo paso y se obtendrá un archivo con los hits de Blast llamado "Resultado_blast_completo" que se almacenará en la "nombre_carpeta/results/blast". 

#
-->En cuarto lugar, se podrá realizar un filtro por identidad, coverage y e-value que puede elegir el usuario los valores o bien puede dejarlos predeterminados, que serán 85,30 y 1e-2, respectivamente. El archivo obtenido tendrá el nombre de "filtro.fasta" y se almacenará en "nombre_carpeta/results/blast".

-Además, en caso de mandar un archivo que contiene varias querys, se generará un archivo por cada query que contenga y cuyo nombre será el de la misma (query) con sus correspondientes hits. En este caso, también se conservará el archivo completo "filtro.fasta" y todos serán almacenados en la carpeta previamente mencionada.
#
-->En quinto lugar, se llevará a cabo el alineamiento en Muscle seguido de la formación del árbol. En este caso, puede ser diferente si el achivo query contiene una sola secuencia o si contiene varias:

-En caso de contener una sola query: el archivo filtrado de blast se alineará y después se mandará a hacer el árbol.

-En caso de contener varias querys: los diversos archivos obtenidos en el filtrado, se mandarán independientemente a alinear, para después obtener un árbol de cada uno de ellos.

        -Los archivos del alineamiento tendrán el nombre "query_alineamiento" y se almacenará en "nombre_carpeta/results/muscle".
        
        -Los archivos árboles tendrán el nombre procedente del alineamiento seguido de "_arbol.phy" y se almacenarán también                en "nombre_carpeta/results/muscle".
#
-->En sexto y último lugar, se llevará a cabo la extracción de mayor información de los hits de blast que hemos obtenido. Para ello, se manda el archivo "filtro.fasta" que contiene todos los hits de blast que hemos filtrado al módulo prosite para que busque dominios de proteínas que se encuentren en nuestros hits y de ellos sacar la información que tiene la siguiente organización en el documento:

        -Nombre del hit: tendrá el formato ">" seguido del nombre del hit.
        -Nombre del dominio.
        -Accession.
        -Patrón.
        -Descripción.
        -Información adicional.
        
-Cada uno de los dominios encontrados estará seaparado por una línea discontinua. El inicio del siguiente hit será cuando vuelva a encontrarse un ">" seguido de otro nombre.

-Para la ejecución de este módulo son necesarios los archivos prosite.doc y prosite.dat que se adjuntan con la carpeta paquete. 

-El archivo generado será almacenado en "nombre_carpeta/results/prosite".
#
-->Todos los archivos que el usuario introduce, así como el script también serán almacenados en las subcarpetas que se generan dentro de la carpeta cuyo nombre puede elegir al inicio y a las que he ido haciendo referencia previamente. La organización de las subcarpetas queda de la siguiente manera:

        -Data: a ella se copiarán los archivos que el usuario manda, así como los archivos prosite.doc y prosite.dat.
        
        -Results: a su vez contiene varias subcarpetas que previamente he ido mencionando:
        
            -Blast: contendrá todos los archivos que se extraen del blast.
            
            -Muscle: contiene todos los archivos que se obtienen al usar la herramienta muscle.
            
            -Prosite: contendrá el archivo que se obtiene al buscar dominios en los archivos de la base de datos.
            
        -Scripts: a esta carpeta se moverá el paquete completo que se usó para obtener todos los resultados.
        
#
-->Por último, el programa cuenta con una función help escribiendo como argumento -h o --help donde describirá algún punto de los explicados aquí.
#
Puede usar este programa con los archivos adjuntados. 

    -Al pedir el nombre de query introduzca: my_query.fa
      En este caso, es un ejemplo que contiene solamente una secuencia.
    -Al pedir el número del genbank, introducir 1 y después su nombre: GCF_000006945.2_ASM694v2_genomic.gbff
    -Finalmente, puede probar a cambiar los valores que pide como filtro o dejarlo como están y obtendrá la carpeta con sus resultados.
