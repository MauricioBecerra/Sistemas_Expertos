import json
import tkinter as tk
from tkinter import messagebox

def cargar_base_datos(ruta_archivo):
    """Carga el archivo JSON que actúa como base de datos."""
    with open(ruta_archivo, "r") as f:
            return json.load(f)

def mostrar_resultado(fallas):
    """Muestra la falla detectada en un cuadro de mensaje."""
    if len(fallas) == 1:
        mensaje = f"La falla detectada es: {fallas[0]['nombre']}\n\nPosibles soluciones:\n"
        mensaje += "\n".join([f"- {sol}" for sol in fallas[0]['soluciones']])
    elif len(fallas) > 1:
        mensaje = "Existen múltiples posibles fallas aún:\n"
        mensaje += "\n".join([f"- {falla['nombre']}" for falla in fallas])
        mensaje += "\n\nIntente ser más específico con las respuestas."
    else:
        mensaje = "No se pudo identificar la falla exacta con la información proporcionada."
    messagebox.showinfo("Resultados del Diagnóstico", mensaje)

def realizar_diagnostico(datos):
    """Ejecuta el diagnóstico interactivo basado en preguntas dinámicas."""
    posibles_fallas = datos['fallas'][:]
    atributos = datos['atributos']
    

    def preguntar_siguiente_atributo():
        nonlocal posibles_fallas, atributo_actual

        # Si solo queda una falla, mostramos el resultado
        if len(posibles_fallas) == 1:
            mostrar_resultado(posibles_fallas)
            root.quit()
            return

        # Seleccionar el siguiente atributo relevante
        for atributo in atributos:
            valores = {falla['atributos'].get(atributo['clave']) for falla in posibles_fallas}
            if len(valores) > 1:  # Si el atributo aún puede dividir las opciones
                atributo_actual = atributo
                break
        else:
            # Si no hay más atributos para preguntar, mostramos los resultados
            mostrar_resultado(posibles_fallas)
            root.quit()
            return

        # Actualizar la pregunta en la interfaz
        pregunta_var.set(atributo_actual['pregunta'])

    def procesar_respuesta():
        nonlocal posibles_fallas

        # Filtrar las fallas según la respuesta dada
        respuesta = respuesta_var.get()
        posibles_fallas = [
            falla for falla in posibles_fallas
            if falla['atributos'].get(atributo_actual['clave']) == respuesta
        ]

        # Preguntar el siguiente atributo
        preguntar_siguiente_atributo()

    # Configurar la interfaz gráfica
    root = tk.Tk()
    root.title("Sistema Experto de Diagnóstico")

    # Variable para mostrar la pregunta
    pregunta_var = tk.StringVar()

    # Etiqueta para la pregunta
    pregunta_label = tk.Label(root, textvariable=pregunta_var, font=("Arial", 12), wraplength=400)
    pregunta_label.pack(pady=10)

    # Variable para almacenar la respuesta
    respuesta_var = tk.BooleanVar()

    # Botones de respuesta
    si_button = tk.Radiobutton(root, text="Sí", variable=respuesta_var, value=True, font=("Arial", 10))
    si_button.pack(anchor="w")

    no_button = tk.Radiobutton(root, text="No", variable=respuesta_var, value=False, font=("Arial", 10))
    no_button.pack(anchor="w")

    # Botón para confirmar la respuesta
    siguiente_button = tk.Button(root, text="Siguiente", font=("Arial", 12), command=procesar_respuesta)
    siguiente_button.pack(pady=20)

    # Iniciar con la pregunta principal
    atributo_actual = None
    for atributo in atributos:
        if atributo['clave'] == "enciende":
            atributo_actual = atributo
            break
    pregunta_var.set(atributo_actual['pregunta'])

    root.mainloop()

ruta_archivo = "base_datos.json"
datos = cargar_base_datos(ruta_archivo)
realizar_diagnostico(datos)
