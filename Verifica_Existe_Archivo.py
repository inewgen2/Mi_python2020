import os

if os.path.isdir('/home/dev/Documentos/python/archivos_prueba/'):
    print('La carpeta existe.');
else:
    print('La carpeta no existe.');

if os.path.isfile('fichero.txt'):
    print('El archivo existe.');
else:
    print('El no archivo existe.');