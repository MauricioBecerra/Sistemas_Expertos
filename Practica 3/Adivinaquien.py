##Mauricio Becerra Guzmán   ---- 21310105  #####

import json

ANIMALES_FILE = "animales.json"

def cargar_animales():
    """Carga la lista de animales desde un archivo JSON."""
    try:
        with open(ANIMALES_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [
            {"nombre": "Perro", "plumas": False, "acuatico": False, "domestico": True},
            {"nombre": "Pato", "plumas": True, "acuatico": True, "domestico": False},
            {"nombre": "Gato", "plumas": False, "acuatico": False, "domestico": True},
            {"nombre": "Tiburón", "plumas": False, "acuatico": True, "domestico": False},
        ]

def guardar_animales(animales):
    """Guarda la lista de animales en un archivo JSON."""
    with open(ANIMALES_FILE, "w") as f:
        json.dump(animales, f, indent=4)

def existe_animal(animales, nombre):
    """Verifica si un animal ya existe en la base de datos."""
    nombre = nombre.strip().lower()
    return any(animal["nombre"].lower() == nombre for animal in animales)

def filtrar_por_regla(animales, atributo, valor):
    """Aplica una regla de encadenamiento hacia adelante para reducir los animales posibles."""
    return [animal for animal in animales if animal[atributo] == valor]

def aprendizaje(animales):
    """Aprende un nuevo animal si no está en la base de datos."""
    nombre = input("¿Cuál era el animal que estabas pensando? ").strip()
    
    if existe_animal(animales, nombre):
        print(f"El animal '{nombre}' ya existe en la base de datos.")
        return

    plumas = input("¿Tiene plumas? (sí/no): ").strip().lower() == "sí"
    acuatico = input("¿Es acuático? (sí/no): ").strip().lower() == "sí"
    domestico = input("¿Es doméstico? (sí/no): ").strip().lower() == "sí"

    animales.append({
        "nombre": nombre,
        "plumas": plumas,
        "acuatico": acuatico,
        "domestico": domestico
    })

    guardar_animales(animales)
    print(f"¡He aprendido sobre {nombre}!")

def juego():
    animales = cargar_animales()
    posibles = animales[:]

    print("¡Piensa en un animal y yo intentaré adivinarlo!")
    atributos = ["plumas", "acuatico", "domestico"]

    # Encadenamiento hacia adelante: Aplica reglas a medida que responde el usuario
    for atributo in atributos:
        if len(posibles) > 1:
            respuesta = input(f"¿El animal tiene {atributo}? (sí/no): ").strip().lower() == "sí"
            posibles = filtrar_por_regla(posibles, atributo, respuesta)

    if len(posibles) == 1:
        if input(f"¿Es un {posibles[0]['nombre']}? (sí/no): ").strip().lower() == "sí":
            print("¡Adiviné! ¡Gracias por jugar!")
        else:
            print("Oh, fallé...")
            aprendizaje(animales)
    else:
        print("No pude adivinar tu animal.")
        aprendizaje(animales)

if __name__ == "__main__":
    juego()
