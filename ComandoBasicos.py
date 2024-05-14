

import subprocess

def ejecutar(comando):
    subprocess.run(comando,shell = True)

Opcion= input('choose an option')

if opcion == '1':
     ejecutar ("touch promedio.txt")
     
     
