"""
Solicitar una oración por teclado y realizar las siguientes operaciones sobre ella:

    Mostrar longitud de la cadena.
    Mostrar espacios en blanco se ingresaron.
    Mostrar toda la oración en letras mayúsculas.
    Duplicar el contenido de la cadena.
    Dividir la cadena en una lista de palabras y recorrerla mostrándola y numerando cada palabra.
"""

oracion=input("Escriba una oracion: ")

print( "Su longitud es " + str( len(oracion) ) )
print( "Tiene " + str( oracion.count(" ") ) + " espacios en blanco" )
print(oracion.upper())
print(oracion * 2)

palabras=oracion.split()

for num,palabra in enumerate(palabras, 1):
    print(f"{num}- {palabra}")