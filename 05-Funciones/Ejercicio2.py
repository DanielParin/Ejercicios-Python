# Escribe una función que tome una palabra y retorne con todas las letras en minúscula menos la primera y la última.

def modificar_palabra(palabra):

   palabra_modificada = palabra[1:-1]
   return palabra_modificada

palabra = input("Ingrese una palabra: ")
print(modificar_palabra(palabra))