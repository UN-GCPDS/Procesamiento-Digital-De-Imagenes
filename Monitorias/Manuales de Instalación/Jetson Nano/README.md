# Instalación de sistema operativo en JetsonNano

Para realizar la instalación necesitan una micro SD y un adaptador micro SD a USB para poder conectarla a un computador y poder instalar el sistema operativo.

## Descarga de archivos

Nos dirigimos al siguiente enlace para descargar la ISO de Nvidia:
````
https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write
````
En el menú e la izquierda seleccionamos "Write image to the microSD Crad".
En el numeral 1 damos clic en "Jetson Nano Developer Kit SD Card Image" aparece en verde las letras, se descargará automáticamente la ISO del sistema operativo.
Una vez se descargue lo descomprimimos.

Nos dirigimos al siguiente enlace para descargar el programa balenaEtcher:
````
https://www.balena.io/etcher/
````
Este programa nos sirve para instalar el sistema operativo en nuestra microSD, una vez descargado instalamos el programa en nuestro PC.

## Instalacion del sistema operativo

+ Abrimos el programa BalenaEtcher
+ Seleccionamos la opcion "Flash from file"
+ Buscamos la ISO de Nvidia con extension .img lo seleccionamos y clicamos en abrir
+ Seleccionamos la opcion "Select target" y escogemos nuestra microSD y clicamos en "Select"
+ Por ultimo seleccionamos la opcion "Flash!"

El programa comenzara a instalar el sistema operativo, este puede tardar varios minutos.
