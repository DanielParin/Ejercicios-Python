"""
Crear un programa que almacene con dos opciones: 1. Agregar personas: permite introducir nombres de personas 
de forma interactiva, 2. Sorteo: devuelve el nombre de una persona al azar. Opcional: Cargar nombre a partir de un archivo csv.
"""

import random

menu="1-Agregar una persona.\n2-Sorteo.\n0-Salir.\n\nSeleccione opcion:"
lista_personas=[]

salir=False

while not salir:

    eleccion = input(menu)

    while eleccion!="1" and eleccion!="2" and eleccion!="0":
        eleccion=input("Ingrese una opcion valida: ")
    
    if eleccion=="1":
        persona=input("Inserte el nombre de una persona: ")
        lista_personas.append(persona)
    elif eleccion=="2":
        if len(lista_personas)==0:
            print("No hay personas para hacer un sorteo\n")
        else:
            print("Ha ganado " + random.choice(lista_personas))
    else:
        salir=True


