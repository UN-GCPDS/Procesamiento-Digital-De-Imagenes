# Creacion de repositorio en GitHub.

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
Con el siguiente comando vamos a agregar todos los archivos que están en la carpeta con su estado actual al registro de Git.
````
git add .
````
En este paso realizaremos nuestro primer "commit" esta es la forma que Git tiene para registrar los cambios de nuestros archivos, gracias podemos ver versiones pasadas de nuestros proyectos. Importante entre comillas siempre poner un mensaje, preferiblemente la versión de su proyecto o un mensaje de describiendo que realizaron en el proyecto.

````
git commit - m "Version_#1"
````
Para subir los archivos escribimos lo siguiente, después de "origin" colocamos el enlace de GitHub de nuestro repositorio.
Este paso solo se realiza la primera vez que queremos subir archivos a un repositorio nuevo, este comando vincula el repositorio local en nuestro PC, con el de la nube en GitHub.
````
git remote add origin https:example.com
````
Sí queremos probar nuevas cosas en nuestro proyecto sin perder lo que llevamos o afectar nuestros resultados, podemos crear una nueva ramificación de nuestro proyecto y así no perder lo que llevemos, para esto usamos el siguiente comando, en "main" colocamos el nombre de nuestra nueva rama, por defecto se coloca "main" que es la ramificación principal de nuestro proyecto.
````
git branch -M main
````
El último paso es subir nuestros archivos, el cual se realiza con el siguiente comando, en "main" va el nombre de la rama donde queremos subir nuestros archivos.
````
git push -u origin main
````
Si es la primera vez que suben archivos desde su computador a su GitHub, este les pedirá credenciales o iniciar sesión nuevamente, ya con esto tendrán sus archivos subidos a su repositorio, si desean conocer más comandos que le puedan ser de utilidad revisar el PDF llamado " git-cheat-sheet-education " que se encuentra en esta misma carpeta.
