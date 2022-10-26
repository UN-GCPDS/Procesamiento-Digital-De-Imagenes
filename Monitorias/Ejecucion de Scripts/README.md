# Ejecucion de Scripts
Para poder realizar la ejecución de los scripts ya debemos tener nuestros ambientes virtuales creados y tener clonado el repositorio del curso.

Pasos:
+ Abren la terminal 
+ Activan su ambiente virtual
+ Para la ejecución del script escriben el siguiente comando en la terminal:
````
python3.7 Path
````
Donde está la palabra Path deben colocar la ruta del script, un ejemplo seria:
````
python3.7 2-ConceptosBasicosDeImagenes/scripts/3_pictureFromCamera.py
````
Hay algunos scripts como el anterior que les pedirá información extra aparte de la ruta, un ejemplo sería el script "3_pictureFromCamera.py", 
si lo ejecutan como antes la terminal les responderá con lo siguiente:
````
usage:
  3_pictureFromCamera.py -f FOLDER [-p PATH]
````
Para saber que significa van al script lo abren con cualquier editor de texto y en las primeras líneas del código les explicaran que significa cada parte.

En este caso -f FOLDER nos pide la ruta en donde queremos guardar las imágenes, por lo cual para la correcta ejecución del script se vería de la siguiente forma:
````
python3.7 2-ConceptosBasicosDeImagenes/scripts/3_pictureFromCamera.py -f /home/PDI/Desktop/PDI/Procesamiento-Digital-De-Imahenes/fotos/
````
la primera ruta indica la posición del script y la segunda donde se guardaran las imágenes.

Si desean saber como funcionan los scripts simplemente los abren en un editor de texto, ahí mismo hay una explicación de como funcionan.
