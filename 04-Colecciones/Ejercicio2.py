"""
Crear un programa que almacene nombres de personas, tras introducir un nombre nuevo mostrará un conteo de los 
nombres que tienen 5 o más caracteres y preguntará si desea introducir un nuevo nombre o salir del programa.
Opcional: Cargar palabras a partir de un archivo txt.
"""

conteo = 0
salir_programa="n"
lista_nombres=[]

while salir_programa != "s":

    nombre = input("Introduce un nombre: ")
    lista_nombres.append(nombre)

    if len(nombre)>=5:
        conteo+=1
        print(str(conteo))
    
    salir_programa = input("Quiere salir del programa?(s/n)\n")

    while salir_programa!="n" and salir_programa!="s":

        salir_programa = input("Ingrese una opcion valida: ")

print(lista_nombres)