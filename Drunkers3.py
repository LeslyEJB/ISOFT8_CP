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

    for nombre in drunkards:
        accion = random.choice(["servir", "usar_baño", "llamada_ex", "cantando"])
        
        if accion == "usar_baño":
            if not ocupado_baño and contador_cervezas[nombre] >= 1:
                usar_baño(nombre)
                ocupado_baño = True
            else:
                sirviendo_cerveza(nombre)  # fallback: le sirven otra
        elif accion == "llamada_ex":
            if not ocupado_llamada:
                llamada_ex(nombre)
                ocupado_llamada = True
            else:
                cantando(nombre)
        elif accion == "servir":
            sirviendo_cerveza(nombre)
        elif accion == "cantando":
            cantando(nombre)

# Ejecutar 4 ciclos
for i in range(4):
    ciclo_acciones(drunkards, i)

# Mostrar resumen de cervezas
# Mostrar un título para la lista de cervezas
print("\n--- Cervezas tomadas por cada borracho ---")

for nombre in contador_cervezas:
    cervezas = contador_cervezas[nombre]
    print(nombre + ": " + str(cervezas) + " cerveza(s)")
