"""
Crea una clase “Saludo” que tenga los métodos: formal, informal y aleatorio. Los métodos pueden aceptar un 
parámetro (nombre de la persona a saludar) o ninguno (saludo genérico), el método aleatorio imprimirá un saludo 
aleatorio de una lista de saludos almacenados en la clase.
"""

import random

class Saludo:

    lista_saludos = ["Hola caracola","Holiwi carakiwi","Ey yooo","Que onda wey"]

    def formal(nombre=None):
        if nombre:
            print("Tengo el agrado de dirigirme a usted señor/a "+nombre)
        else:
            print("Tengo el agrado de dirigirme a usted")

    def informal(nombre=None):
        if nombre:
            print("Ey que pasa "+nombre)
        else:
            print("Ey que pasa")
    
    def aleatorio(self):
        print(random.choice(self.lista_saludos))
