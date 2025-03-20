'''
En este caso nos permitimos realizar una sobrecarga con o sobreescritura de la idea de los archivos

Es interesante como se va a enfrentar

'''
class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50,'>'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print('Cerramos el recurso'.center(50,'>'))
        if self.nombre:
            self.nombre.close()