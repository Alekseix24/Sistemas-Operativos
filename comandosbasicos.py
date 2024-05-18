'''
AUTOR: ADRIAN ALEKSEI MARQUEZ GONZALEZ
Programa que crea un menu y hace diferentes carpetas y Archivos utilizando los
comandos de ubuntu.

'''

import subprocess 
def ejecutar(comando):
    subprocess.run(comando,shell = True)


print("comandos")
print("1. Crea archIvo txt")
print("2. mkdir calificaciones")
print("3. mkdir primerparcial")
print("4. mover archivos")
print("5. crea comando.py")
print("6. importa calculadora")
opcion= input("choose an option: ")

if opcion == '1':
     ejecutar ("touch promedio.txt")
if opcion == '2':
    ejecutar("mkdir calificaciones")
if opcion == '3':
    ejecutar("mkdir primerParcial")
if opcion == '4':
    ejecutar('mv "promedio.txt" "primerParcial"')
if opcion == '5':
    ejecutar ("touch comando.py")
if opcion =='5':
    ejecutar ('mv "comando.py" "calificaciones"')
if opcion == '6':
    import calculadora
    








    
