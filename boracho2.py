import time
import random

def tomar(nombre):
    print(f"{nombre} está tomando cerveza...")
    time.sleep(1)

def usar_baño(nombre):
    print(f"{nombre} está en el baño...")
    time.sleep(1)
    print(f"{nombre} salió del baño.")

def llamada_ex(nombre):
    print(f"{nombre} está llamando a su ex...")
    time.sleep(1)
    print(f"{nombre} colgó la llamada.")

def cantando(nombre):
    print(f"{nombre} está cantando una canción dolida...")
    time.sleep(1)
    
def ciclo_acciones(drunkards, ciclo):
    print(f"\n------ Ciclo {ciclo + 1} ------")
    
    # Reordenar aleatoriamente los drunkards para variar los turnos
    random.shuffle(drunkards)
    
    # Marcar si el baño o la llamada están ocupados
    ocupado_baño = False
    ocupado_llamada = False

    for nombre in drunkards:
        accion = random.choice(["tomar", "usar_baño", "llamada_ex", "cantando"])
        
        # Controlar acciones exclusivas
        if accion == "usar_baño":
            if not ocupado_baño:
                usar_baño(nombre)
                ocupado_baño = True
            else:
