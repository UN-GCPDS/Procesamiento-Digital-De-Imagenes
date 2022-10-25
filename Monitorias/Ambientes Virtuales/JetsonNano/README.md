# Creación de ambientes virtuales en JetsonNano
## Actualizacion del sistema
para la creacion de ambientes virtuales en JetsoNano primero debemos actualizar el sistema, para esto debemos conector la JetsonNano al internet, la jetson no cuenta
con modulo WIFi por lo que debe conectarse por medio de cable ethernet o un modulo WIFI USB.

Una vez conectados abrimos la terminal de linux con la siguiente combiancion de teclas "Ctrl + alt + t"

con la terminal abirta escribimos el siguiente comando:
````
sudo apt-get update
````
nos pedira la contraseña la escribimos y enter.

al terminar escribimos el siguiente comando:
````
sudo apt-get upgrade
````
luego nos preguntara si queremos continuar escribimos "S" o "Y" segun el idioma damos enter y esperamos a que termine
puede tomar varios minutos.

Al finalizar reinician.

## Instalacion Python 3.7
Por defecto esta version de linux no viene con Python 3.7, pero para este curso y correr los scripts que se requieren necesitamos Python 3.7, para la instalacion abrimos
la terminal y escribimos los siguientes comandos:
````
sudo apt install python3.7
````
Nos pedira la contraseña, la escribimos y damos a enter.

al terminar escribimos el siguiente comando:
````
sudo apt-get install python3.7-venv
````

para corroborar la correcta instalacion de Python 3.7 escribimos el siguiente comando:
````
python3.7 --version
````
Debajo de esa linea debe aparecer "Python 3.7"

## Creacion del ambiente virtual
Creamos una carpeta en el escritorio con el nombre que quieran. La abrimos y ejecutamos la terminal en esta carpeta, para eso damos clic derecho en la carpeta
y seleccionamos "Open in terminal". Necesitaremos el repositorio del curso por lo que lo clonaremos.
````
git clone https://github.com/UN-GCPDS/Procesamiento-Digital-De-Imagenes.git
````
abrimos la carpeta resultante y abrimos una nueva terminal dentro de la carpeta "Procesamiento-Digital-De-Imagenes", en esta carpeta vamos 
a crear nuestro ambiente virtual para eso usamos los siguientes comandos:
````
python3.7 -m venv .env
````
dejamos que finalice, si activamos la vista de archivos ocultos debe aparecer una carpeta con el nombre de".env", esto significa que quedo bien creado el ambiente.

## Activacion del ambiente virtual
En la carpeta donde creamos el ambiente virtual, abrimos la terminal en esa carpeta y ejecutamos el siguiente comando:
````
source .env/bin/activate 
````
si está correctamente abierta en la parte izquierda de la línea de comando debe aparecer"(.env)".

## Instalación paquetes necesarios
Para que los scripts corran de manera correcta debemos instalar unos paquetes, activamos nuestro ambiente virtual y para instalar 
la paquetería usaremos el siguiente comando:
````
pip install -r requirements.txt
````

## Desactivar ambiente virtual
Para desactivar el ambiente virtual ejecutamos el siguiente comando en la terminal:
````
deactivate
````
