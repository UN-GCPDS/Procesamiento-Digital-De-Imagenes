# <center> Procesamiento Digital de Imágenes </center>

Repositorio del curso de Procesamiento Digital de Imágenes.  

[Información del curso](https://docs.google.com/spreadsheets/d/1ODFNuppfZTspb2CqdAHMDGFF0lk150aQ/edit?usp=sharing&ouid=102209159107774849732&rtpof=true&sd=true)


## Instalación 

### Configuración (Solo para Raspberry Pi)

#### Actualizar el sistema 

```
sudo pacman -Syyu
```

#### Instalar Python 

```
sudo pacman -S yay
```

```
sudo yay -S python37
```

#### Configurar Camara 

```
sudo echo start_x=1 >> /boot/config.txt
```

Reinicie la Raspberry Pi










### Clonar repositorio 
```
git clone https://github.com/UN-GCPDS/Procesamiento-Digital-De-Imagenes.git
```
```
cd Procesamiento-Digital-De-Imagenes
```

### Creación ambiente virtual 

Verificar que la versión de python sea la 3.7 


```
python --version 
```

```
python -m venv .env 
```

### Activación ambiente virtual 

```
source .env/bin/activate 
```

### Instalación paquetes necesarios 
```
pip install -r requirements.txt
```
Recordar que mientras el ambiente virtual este activado pip instalará paquete solo sobre este. 

### Desactivar ambiente virtual

```
deactivate 
```
