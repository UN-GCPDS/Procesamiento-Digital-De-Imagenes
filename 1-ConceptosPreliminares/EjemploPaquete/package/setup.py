from setuptools import setup,find_packages


setup(
   name='geometry',
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