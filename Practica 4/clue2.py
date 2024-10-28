import random

class Personaje:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
        self.historia = ""
        self.lugar = ""
        self.actividad = ""
        self.objeto = ""
        self.rol = ""

class JuegoAmongUs:
    def __init__(self):
        self.personajes = [
            Personaje('Juan', 'Profesor'),
            Personaje('Ana', 'Estudiante'),
            Personaje('Carlos', 'Conserje'),
            Personaje('Maria', 'Bibliotecaria'),
            Personaje('Luis', 'Entrenador')
        ]
        self.locaciones = ['Aula', 'Biblioteca', 'Gimnasio', 'Cafetería', 'Laboratorio']
        self.armas = ['Tijeras', 'Lápiz', 'Cuerda', 'Libro', 'Piedra']
        self.culpable = None
        self.arma = None
        self.locacion = None
        self.asignar_roles()

    def asignar_roles(self):
        random.shuffle(self.personajes)
        self.culpable = self.personajes[0]
        self.arma = random.choice(self.armas)
        self.locacion = random.choice(self.locaciones)
        
        for personaje in self.personajes:
            personaje.lugar = random.choice(self.locaciones)
            personaje.actividad = random.choice(['Estudiando', 'Limpiando', 'Entrenando', 'Comiendo', 'Trabajando'])
            personaje.objeto = random.choice(self.armas)
            personaje.rol = "Inocente"
            personaje.historia = f"Estaba en {personaje.lugar}, {personaje.actividad}, y vio un {personaje.objeto}."
        self.culpable.rol = "Asesino"
        self.culpable.historia = f"Estaba en {self.locacion} con {self.arma}."

    def preguntar_personaje(self, nombre):
        for personaje in self.personajes:
            if personaje.nombre == nombre:
                informacion = (f"{personaje.nombre} ({personaje.profesion}) estaba en {personaje.lugar} "
                               f"{personaje.actividad} y vio un {personaje.objeto}. "
                               f"{personaje.historia if personaje.rol == 'Asesino' else ''}")
                print(informacion)
                return
        print("Personaje no encontrado.")

    def preguntar_arma(self, arma):
        for personaje in self.personajes:
            if personaje.objeto == arma:
                informacion = f"{personaje.nombre} vio el {arma} en {personaje.lugar}."
                print(informacion)
                return
        print("No se encontró información sobre esa arma.")

    def preguntar_lugar(self, lugar):
        resultado = f"En {lugar} se encontraron: \n"
        for personaje in self.personajes:
            if personaje.lugar == lugar:
                resultado += f"- {personaje.nombre} ({personaje.profesion}) que vio un {personaje.objeto}.\n"
        print(resultado if resultado != f"En {lugar} se encontraron: \n" else "No había nadie en ese lugar.")

    def mostrar_historias(self):
        print("\nHistorias creadas al inicio del juego:")
        for personaje in self.personajes:
            print(f"- {personaje.nombre} ({personaje.profesion}): {personaje.historia}")

    def jugar(self):
        print("Bienvenido al juego estilo Among Us")
        print("Puedes hacer 4 preguntas para descubrir quién es el asesino, con qué arma y en qué lugar.")
        preguntas_restantes = 4

        self.mostrar_historias()

        while preguntas_restantes > 0:
            print("\n¿Qué deseas preguntar?")
            print("1. Información sobre un personaje")
            print("2. Información sobre un arma")
            print("3. Información sobre un lugar")
            opcion = int(input("Selecciona una opción (1, 2, 3): "))

            if opcion == 1:
                nombre = input("Escribe el nombre del personaje: ")
                self.preguntar_personaje(nombre)
            elif opcion == 2:
                arma = input("Escribe el nombre del arma: ")
                self.preguntar_arma(arma)
            elif opcion == 3:
                lugar = input("Escribe el nombre del lugar: ")
                self.preguntar_lugar(lugar)

            preguntas_restantes -= 1
            print(f"Te quedan {preguntas_restantes} preguntas.\n")

        acusacion_personaje = input("¿Quién es el asesino? ")
        acusacion_arma = input("¿Cuál fue el arma usada? ")
        acusacion_lugar = input("¿Dónde ocurrió el asesinato? ")

        if (acusacion_personaje == self.culpable.nombre and 
            acusacion_arma == self.arma and 
            acusacion_lugar == self.locacion):
            print("¡Has resuelto el misterio! ¡Felicidades!")
        else:
            print("No has acertado. Mejor suerte la próxima vez.")
            print(f"El asesino fue {self.culpable.nombre} con {self.arma} en {self.locacion}.")

# Iniciar el juego
juego = JuegoAmongUs()
juego.jugar()
