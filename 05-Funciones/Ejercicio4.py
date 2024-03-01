# Escribe una función que pasada una palabra indique si es un palíndromo o no.

def is_palindromo(palabra):
    if(palabra==''.join(reversed(palabra))):
        return True
    else:
        return False

palabra = input("Escriba una palabra: ")

if is_palindromo(palabra):
    print("Es palindromo.")
else:
    print("No es palindromo.")