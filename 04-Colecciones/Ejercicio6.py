"""
Crear una lista con contenido [[50,34,70,20], [5,70,30,25], [10,5], [75,43,56,32,89], [[54,72]]]. Imprimir la lista, asignar valor cero 
a todos los elementos mayores a 50 y volver a imprimir la lista.
"""

lista = [[50,34,70,20], [5,70,30,25], [10,5], [75,43,56,32,89], [[54,72]]]

print(lista)

for sublista in lista: # Para recorrer los elementos de la lista

    for elemento in range(len(sublista)): # Para que recorra los elementos de dentro de los elementos de la lista. OJO con la ultima

        if isinstance(sublista[elemento],list): # Si hay otra lista dentro de la lista (para la ultima)
            for subelemento in range(len(sublista[elemento])):

                if sublista[elemento][subelemento] > 50:
                    sublista[elemento][subelemento] = 0
        else:
            if sublista[elemento] > 50:
                sublista[elemento] = 0

print(lista)
