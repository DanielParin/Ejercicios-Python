# Programa que dibuje con asteriscos un triángulo rectángulo isósceles de N asteriscos de alto.


altura=int(input("Inserta el alto del triangulo: "))

for i in range(1, altura+1):
    print("*" * i)
