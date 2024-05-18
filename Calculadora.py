




num1=int(input("Ingresa un numero: "))
num2=int(input("Ingresa otro numero: "))

def sumar (a,b):
    return a+b

def restar (a,b):
    return a-b

def multiplicar (a,b):
    return a*b

def dividir (a,b):
    return a/b



""" Princcipal program """



print("CALCUADORA")
print("1. suma")
print("2. resta")
print("3. multipicacion")
print("4. division")
print("5. Salir")

op=input("ESCOGE: ")


if op=='1':
    suma = sumar(num1,num2)
    print("La suma es:", suma)

elif op=='2':
    resta = restar(num1,num2)
    print("La resta es:", resta)

elif op=='3':
    multiplicacion = multiplicar(num1,num2)
    print("La multipicacion es:", multiplicacion)

elif op=='4':
    division = dividir(num1,num2)
    print("La division es:", division)

elif op=='5':
    print("Gracias por usar.")




