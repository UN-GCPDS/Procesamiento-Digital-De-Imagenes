# Creación de paquetes de Python

Los paquetes permiten organizar y distribuir código Python para ser reutilizado posteriormente como una librería, como por ejemplo Numpy, Matplotlib etc. 

## Paso 1: Estructuración del paquete

En su forma simple, un paquete de Python es un conjunto de módulos (código Python almacenado en archivos .py) organizados en carpetas.

**Sumado a esta estructura, es requerido que cada carpeta y subcarpeta tenga un archivo** ```__init__.py```. Este archivo tiene un funcionamiento similar al ```__init__``` de una clase.  Este archivo generalmente se encuentra vacio.

A continuación se muestra un ejemplo.
```
geometry
├── __init__.py
├── objetos
│   ├── __init__.py
│   └── objetos.py
├── operaciones
│   ├── __init__.py
│   └── operaciones.py
└── variables
    ├── __init__.py
    └── variables.py
```

Con tan solo esa estructura podemos usar *geometry* como un paquete cualquiera, pero es requerido que siempre esta carpeta se encuentre el el mismo directorio de donde va a ser usado. 

```
.
├── geometry
└── main.py
```
En el archivo ```main.py```:

```
from geometry.objetos.objetos import cuadrado
from geometry.variables.variables import PI
from geometry.operaciones.operaciones import obtener_area

...
```
**Observe que para acceder a las clases, variables y/o funciones es necesario "navegar" por las carpetas y archivos .py.** Por ejemplo para acceder a la clase cuadrado es necesario; geometry -> objetos -> objetos.py

## Paso 2: Instalación con pip

Aunque el paso 1 parece ser suficiente para organizar el código, como se vió, siempre es necesario que la carpeta se encuentre en el mismo directorio de donde es llamada. Para evitar esto y poner el paquete de forma global usamos pip.

### Paso 2.1: Creación setup.py 
Para usar pip se requiere el archivo *setup.py*. La información mínima que debe contener este archivo se muestra a continuación:

```
from setuptools import setup,find_packages

setup(
   name='geometry', #nombre del paquete 
   version='1.0',
   description='A useful module',
   author='Juan',
   author_email='jucaguirrear@unal.edu.co',
   packages=['geometry', 'geometry.variables',
             'geometry.objetos',
            'geometry.operaciones'], 
   install_requires=['matplotlib',
                        'numpy'], #external packages as dependencies
)
```

Este archivo debe estar al mismo nivel de la carpeta donde se encuentra el paquequete.

```
.
├── geometry
│   ├── __init__.py
│   ├── objetos
│   │   ├── __init__.py
│   │   └── objetos.py
│   ├── operaciones
│   │   ├── __init__.py
│   │   └── operaciones.py
│   └── variables
│       ├── __init__.py
│       └── variables.py
└── setup.py
```

### Paso 2.3: Instalación con pip

Finalmente ubicado en la en el mismo directorio donde esta *setup.py* ejecutamos el siguiente código:

```
pip install .
```

Con esto podemos usar el parquete *geometry* en cualquier lugar.