# Confeccionar un programa que calcule el factorial de un número introducido por teclado.

def factorial(numero):

    factorial = 1

    for i in range(numero,1,-1):
        factorial=factorial*i
    
    return factorial


numero = int(input("Ingrese un numero:"))

print("El factorial es: "+str(factorial(numero)))