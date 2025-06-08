import time
import random

# Contador de cervezas por borracho
contador_cervezas = {}

# Inicializar contador
drunkards = ["Alexis Vega", "Gio Do Santos", "Cristian Calderon", "Marco Fabian", "Carlos Peña"]
for nombre in drunkards:
    contador_cervezas[nombre] = 0
    
def sirviendo_cerveza(nombre):
    print(f"Bartender está sirviendo una cerveza a {nombre}...")
    time.sleep(1)
    contador_cervezas[nombre] += 1

def usar_baño(nombre):
    print(f"{nombre} está en el baño...")
    time.sleep(1)
    print(f"{nombre} salió del baño. Baño Libre.")

def llamada_ex(nombre):
    print(f"{nombre} está llamando a su ex...")
    time.sleep(1)
    print(f"{nombre} colgó la llamada.")

def cantando(nombre):
    print(f"{nombre} está cantando una canción dolida...")
    time.sleep(1)

def ciclo_acciones(drunkards, ciclo):
    print(f"\n------ Ciclo {ciclo + 1} ------")
    
    random.shuffle(drunkards)
    
    ocupado_baño = False
    ocupado_llamada = False