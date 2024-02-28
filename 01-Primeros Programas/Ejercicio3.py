import math
"""
Dados los catetos de un triángulo rectángulo, calcular la hipotenusa.
"""

cateto1 = float(input("Inserte el cateto 1:"))
cateto2 = float(input("Inserte el cateto 2:"))

hipotenusa = math.sqrt((cateto1**2+cateto2**2))

print("La hipotenusa es "+str(hipotenusa))