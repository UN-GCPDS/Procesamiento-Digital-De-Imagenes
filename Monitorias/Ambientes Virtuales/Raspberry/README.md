# Creación de ambientes virtuales en Raspberry Pi

## Configuracion de Camara

Antes de crear los ambientes virtuales debemos configurar la cámara de nuestra Raspberry.
Para ello debemos abrir el explorador de archivos, en la parte de la izquierda en "Removable Devices" seleccionamos "BOOT_MNJRO", en esta carpeta abrimos el archivo
"config.txt", agregamos una nueva línea al final con lo siguiente:
````
start_x=1
````
Guardamos este les pedirá la contraseña la escriben y aceptar, si no tienen contraseña simplemente lo dejan en blanco y aceptar, reiniciamos la Raspberry Pi.

## Actualizacion del sistema

Para la creación de los ambientes virtuales en Raspberry, primero debemos actualizar nuestro sistema operativo, para esto debemos conectar al internet nuestra
Raspberry Pi, la Raspberry Pi cuenta con modulo WIFI.

Una vez conectados a internet abrimos la terminal de linux con "Ctrl + alt + t" 

Con la terminal abierta escribimos el siguiente comando:
````
sudo pacman -Syyu
````
Después de ejecutarlo les pedirá la contraseña del sistema, es la misma que colocaron en la configuración inicial del sistema, si no tiene contraseña lo dejan vacío.

Dan en la tecla enter y comenzará a actualizar.

Pueden corroborar si se actualizó correctamente si dan clic en el icono que tiene una flecha hacia arriba, este está ubicado en la barra de tareas en la parte derecha,
 se les abrirá una pestaña, en la parte superior de esta seleccionan "Updates" o "Actualizaciones" según su idioma, en esta nueva pestaña les debe aparecer que su 
 sistema está completamente actualizado.
 
 Al finalizar las actualizaciones reiniciamos la Raspberry.
 
## Instalacion Python 3.7

Por defecto esta versión de Manjaro viene con Python 3.10, pero para este curso y correr los scripts que se requieren necesitamos Python 3.7.
Para la instalación abrimos la terminal y escribimos el siguiente comando:
````
sudo pacman -S yay
````
Nos preguntará si queremos seguir con la instalación, escribimos que "S" o "Y" según el idioma.
Dejamos que termine de instalar.

Una vez terminado ejecutamos el siguiente comando:
````
yay -S python37
````
Una vez ejecutado, nos harán 4 preguntas, por lo cual escribiremos en la terminal lo siguiente para responderlas:
+ "N"
+ "N"
+ "S" o "Y"
+ "S" o "Y"

Para finalizar nos pedira la contraseña, si no tenemos lo dejamos en blanco.
Nos preguntará si queremos seguir con la instalación, escribimos que "S" o "Y" según el idioma.
Dejamos que termine de instalar este proceso es demorado, dejarlo hasta que se termine.
