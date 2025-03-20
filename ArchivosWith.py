'''

Con estos metodos vemos que se estan ejecutando internamente metodos como

__enter__
__exit__

Es la Maravillas de utilizar "with" se manda a llamar al metodo de los archivos
'''

from ManejoArchivo import ManejoArchivos

# with open('prueba.txt','r', encoding='utf8') as archivo:
with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

