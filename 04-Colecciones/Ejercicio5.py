"""
Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. Crear una nueva lista 
con los nombres ordenados alfabéticamente e imprimirla por pantalla.
Opcional: Crea una función que ordene os nombres por su longitud para pasársela como parámetro al método Short.
"""

lista_nombres=[]
lista_ordenada=[]


for i in range(0,5,1):
    lista_nombres.append(input("Inserte un nombre: "))

lista_nombres.sort() # sort() ordena la lista in-place y devuelve none, por lo que no se puede poner lista_ordenada = lista_nombres.sort()
lista_ordenada =lista_nombres

print(lista_ordenada)