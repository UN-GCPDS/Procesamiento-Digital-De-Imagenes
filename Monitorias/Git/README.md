# <center> Procesamiento Digital de Imágenes. </center>

Creacion de repositorio en GitHub.

## Resgirtro.
Si no se posee cuenta en GitHub, registrarse con el correo institucional para tener beneficios adicionales.

## Nuevo repositorio.
Para la creación de un nuevo repositorio, ir a la página principal de GitHub, en la parte superior izquierda, dar a nuevo, escribir el nombre del repositorio y agregar una descripción si lo desean, dejar la opción de repositorio público para más comodidad, dejar todo lo demás por defecto y dar en crear repositorio.

## Subir archivos con Git.

### (Solo para sistemas operativos windows).
Para poder subir archivos con Git desde Windows, se debe descargar la aplicación desde el siguiente enlace:

````
https://git-scm.com/
````
Se descarga Git y a la hora de la instalación dejar todo por defecto, darle a siguiente hasta que se termine la instalación.

En sistemas operativos Linux no es necesario instalar Git este ya viene instalado por defecto.

### Mi primer repositorio.

En nuestro PC seleccionamos la carpeta donde va a estar nuestro repositorio de manera local, en Linux ejecutamos la terminal en nuestra carpeta, en Windows dentro de la carpeta damos clic derecho y le seleccionamos "Git Bash Here", en ambos casos se abrirá una ventana de comandos.

Si es la primera vez que subimos archivos desde nuestro PC, primero debemos configurarlo.

Con el siguiente comando le damos un nombre a nuestro PC, podemos escribir el nombre que queramos entre las comillas.
````
git config --global user.name "Mi nombre"
````
También debemos vincular un correo electrónico, este correo debe ser el mismo con el que no registramos en GitHub, para eso usamos el siguiente comando.
````
git config --global user.email "micorreo@example.com"
````
Una vez configurado ya podemos subir nuestros archivos.
Para esto primero debemos inicializar nuestra carpeta, para ello usamos.
````
git init
````
