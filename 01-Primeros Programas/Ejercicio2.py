"""
Haz un programa que adivine la talla de pie y la edad del usuario que lo ejecute. Se basa en un sencillo truco matemático. 
El programa debe pedir al usuario que realice las siguientes operaciones 
(las operaciones la tiene que realizar el de cabeza, no el programa):

    Pensar, escribir o apuntar su talla de zapato.
    Multiplicar ese número por 5.
    Sumarle 50.
    Multiplicarlo por 20.
    Sumarle 1023.
    Restarle el año de nacimiento.
"""

import time

print("Vamos a adivinar tu talla de pie con unas preguntas.")
time.sleep(2.5)
print("Piensa en tu talla de zapato")
time.sleep(2.5)
print("Ahora multiplicala por 5.")
time.sleep(2.5)
print("Al resultado le sumamos 50.")
time.sleep(2.5)
print("Luego lo multiplicamos por 20.")
time.sleep(2.5)
print("Le sumamos 1023.")
time.sleep(2.5)
print("Y por ultimo le restas tu año de nacimiento")
time.sleep(3)
resultado=int(input("Que te ha salido?\n"))
talla = str(resultado // 100)
edad = str(resultado % 100)

print("Tienes "+edad+" años y tu talla de zapatos es la "+talla)


