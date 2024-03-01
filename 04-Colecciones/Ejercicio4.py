"""
Crear un programa “Diccionario” que permita consultar definiciones, agregar nuevas palabras 
con su definición o eliminar palabras. Opcional: Cargar diccionario a partir de un archivo csv.
"""

menu = "\n1-Consultar definicion de palabra.\n2-Agregar palabra.\n3-Eliminar palabra.\n0-Salir.\n\nSeleccione opcion: "
salir = False
diccionario_palabras = {}

while not salir:
    eleccion=input(menu)

    while eleccion!="1" and eleccion!="2" and eleccion!="0" and eleccion!="3":
        eleccion=input("Ingrese una opcion valida: ")
    
    if eleccion=="1":

        palabra_buscada=input("Seleccione palabra para consultar: ")

        if palabra_buscada in diccionario_palabras:
            print(palabra_buscada+": "+diccionario_palabras[palabra_buscada])
        else:
            print("No se encontro definicion para la palabra.")

    elif eleccion=="2":
        
        palabra=input("Ingrese palabra: ")
        definicion=input("Ingrese su definicion: ")

        diccionario_palabras[palabra]=definicion

    elif eleccion=="3":

        palabra_buscada=input("Seleccione palabra para borrar: ")

        if palabra_buscada in diccionario_palabras:
            del diccionario_palabras[palabra_buscada]
            print("Palabra eliminada correctamente.")
        else:
            print("No se encontro la palabra.")
    else:
        salir=True
