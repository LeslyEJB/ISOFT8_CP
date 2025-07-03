import time
import random

# todo FUNCIONES QUE SIMULAN LOS "RECURSOS DEL SISTEMA"

def PedirCerveza(quien, core_name):

#! Recurso exclusivo: La persona que lo usa queda ocupada
    print(f"🍺 ACCIÓN EXCLUSIVA: {quien} del {core_name} está pidiendo una cerveza.")
    time.sleep(0.2)

def Rockola(quien, core_name):

#! Recurso exclusivo: La persona que lo usa queda ocupada
    print(f"🎶 ACCIÓN EXCLUSIVA: {quien} del {core_name} ha puesto una canción en la rockola.")
    time.sleep(0.2)