"""
Programa que adivine el numero en el que está pensando (entre 0 y 100) el usuario 
por tanteo (preguntando sucesivamente si es mayor o menor que un número aleatorio de partida)
"""

import random

numero_adivinar = random.randint(1,100)
acertado = True

while acertado:

    numero_elegido=int(input("Ingrese un numero: "))

    if numero_elegido==numero_adivinar:
        print("Has acertado el numero!!!")
        acertado=False
    elif numero_elegido<numero_adivinar:
        print("El numero es mayor.")
    else:
        print("El numero es menor.")
