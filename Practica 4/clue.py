import random

# Definición de personajes, armas y lugares
personajes = ["Alejandro", "Beatriz", "Carlos", "Daniela", "Esteban"]
armas = ["Cuchillo", "Bate", "Cuerda", "Tijeras", "Libro"]
lugares = ["Laboratorio", "Cafetería", "Aula de Informática", "Biblioteca", "Gimnasio"]
actividades = {
    "Laboratorio": "investigar química",
    "Cafetería": "comer algo",
    "Aula de Informática": "trabajar en la computadora",
    "Biblioteca": "leer un libro",
    "Gimnasio": "jugar al fútbol"
}

# Seleccionar aleatoriamente el asesino
asesino = random.choice(personajes)
arma_asasino = random.choice(armas)
lugar_asasino = random.choice(lugares)

# Asignar historias a los personajes, asegurando que el asesino no comparta su arma
historias = {}
for personaje in personajes:
    if personaje == asesino:
        historias[personaje] = {
            "arma": arma_asasino,
            "lugar": lugar_asasino,
            "actividad": actividades[lugar_asasino],
            "historia": f"{personaje} estaba en el {lugar_asasino}, donde estaba {actividades[lugar_asasino]}. Vio un objeto: {arma_asasino}."
        }
    else:
        # Asignar una historia diferente que no incluya el arma del asesino
        arma_no_usada = random.choice([arma for arma in armas if arma != arma_asasino])
        lugar_no_usado = random.choice([lugar for lugar in lugares if lugar != lugar_asasino])
        historias[personaje] = {
            "arma": arma_no_usada,
            "lugar": lugar_no_usado,
            "actividad": actividades[lugar_no_usado],
            "historia": f"{personaje} estaba en el {lugar_no_usado}, donde estaba {actividades[lugar_no_usado]}. Vio un objeto: {arma_no_usada}."
        }

# Función para obtener la historia del personaje
def obtener_historia(personaje):
    return historias[personaje]["historia"]

# Función para obtener información sobre el arma
def obtener_info_arma(arma):
    vistos = []
    for personaje in personajes:
        if historias[personaje]["arma"] == arma:
            vistos.append(f"{personaje} vio el objeto: {arma} en {historias[personaje]['lugar']}.")
    return vistos if vistos else [f"Nadie ha visto el objeto: {arma}."]

# Función para obtener información sobre el lugar
def obtener_info_lugar(lugar):
    vistos = []
    for personaje in personajes:
        if historias[personaje]["lugar"] == lugar:
            vistos.append(f"{personaje} estaba en {lugar} realizando {historias[personaje]['actividad']}.")
    return vistos if vistos else [f"No había nadie en {lugar}."]

# Función para verificar la acusación final
def verificar_acusacion(acusacion_personaje, acusacion_arma, acusacion_lugar):
    return (acusacion_personaje == asesino and 
            historias[acusacion_personaje]["arma"] == acusacion_arma and 
            historias[acusacion_personaje]["lugar"] == acusacion_lugar)

# Lógica del juego
def juego():
    print("¡Bienvenido al juego de deducción! Descubre quién es el asesino.")
    
    # Monitoreo: Imprimir todas las historias al inicio del juego
    print("\n[MONITOREO] Historias de los personajes:")
    for personaje in personajes:
        print(f"- {personaje}: {obtener_historia(personaje)}")
    
    print("\n[MONITOREO] Información de Armas:")
    for personaje in personajes:
        print(f"- {personaje}: Usó el arma: {historias[personaje]['arma']}.")

    print("\n[MONITOREO] Información de Lugares:")
    for personaje in personajes:
        print(f"- {personaje}: Estaba en el lugar: {historias[personaje]['lugar']} donde {historias[personaje]['actividad']}.")

    # Proceso de preguntas
    preguntas_restantes = 4

    while preguntas_restantes > 0:
        print("\n¿Qué deseas preguntar?")
        print("1. Historia de un personaje")
        print("2. Información sobre un arma")
        print("3. Información sobre un lugar")
        
        opcion = input("Ingresa el número de tu elección: ")

        if opcion == "1":
            personaje = input("¿Sobre qué personaje deseas preguntar? ")
            if personaje in personajes:
                print(obtener_historia(personaje))
            else:
                print("Personaje no válido.")
        elif opcion == "2":
            arma = input("¿Sobre qué arma deseas preguntar? ")
            print("\n".join(obtener_info_arma(arma)))
        elif opcion == "3":
            lugar = input("¿Sobre qué lugar deseas preguntar? ")
            print("\n".join(obtener_info_lugar(lugar)))
        else:
            print("Opción no válida.")

        preguntas_restantes -= 1
        print(f"Te quedan {preguntas_restantes} preguntas.")

    # Acusación final
    acusacion_personaje = input("\n¿Quién crees que es el asesino? ")
    acusacion_arma = input("¿Qué arma se usó? ")
    acusacion_lugar = input("¿Dónde ocurrió el crimen? ")

    if verificar_acusacion(acusacion_personaje, acusacion_arma, acusacion_lugar):
        print("¡Correcto! Has resuelto el misterio.")
    else:
        print(f"Incorrecto. El asesino era {asesino}, usó {arma_asasino} en {lugar_asasino}.")

# Iniciar el juego
if __name__ == "__main__":
    juego()
