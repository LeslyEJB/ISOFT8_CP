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

def Cantar(quienes_cantan):

#! Recurso compartido: Muestra cada persona que está cantando.

    print("\n--- Acción Grupal: Cantar ---")
    for persona in quienes_cantan:
        # Determina el core de la persona basado en su nombre
        core = "Core1" if "Borracho" in persona else "Core2"
        print(f"🎤 {persona} del {core} está cantando.")
        time.sleep(0.1) # Pequeña pausa para simular una lista

def Bailar(quienes_bailan):

#! Recurso compartido: Muestra cada persona que está bailando.

    print("\n--- Acción Grupal: Bailar ---")
    for persona in quienes_bailan:
        # Determina el core de la persona basado en su nombre
        core = "Core1" if "Borracho" in persona else "Core2"
        print(f"💃 {persona} del {core} está bailando.")
        time.sleep(0.1) # Pequeña pausa para simular una lista

# todo CONFIGURACIÓN DE LA SIMULACIÓN

borrachos_core1 = [f"Borracho {i}" for i in range(1, 7)]
borrachas_core2 = [f"Borrachita {i}" for i in range(1, 7)]
num_ciclos = 5

acciones_compartidas = [Cantar, Bailar]

print("🍻 INICIO DE LA SIMULACIÓN - DRUNKARD'S PARALLELISM 🍻")
print(f"Mesa 1 (Core1): {', '.join(borrachos_core1)}")
print(f"Mesa 2 (Core2): {', '.join(borrachas_core2)}")
print("-" * 70)