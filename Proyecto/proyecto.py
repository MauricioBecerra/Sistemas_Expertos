import json
import tkinter as tk
from tkinter import messagebox

def cargar_base_datos(ruta_archivo):
    """Carga el archivo JSON que actúa como base de datos."""
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)

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

# Datos de ejemplo (normalmente se cargarían desde un archivo JSON)
datos = {
  "fallas": [
    {
      "nombre": "Batería dañada",
      "atributos": {
        "enciende": False,
        "carga": False,
        "pantalla_tactil": True
      },
      "soluciones": ["Reemplazar la batería", "Revisar el cargador"]
    },
    {
      "nombre": "Pantalla rota",
      "atributos": {
        "enciende": True,
        "carga": True,
        "pantalla_tactil": False
      },
      "soluciones": ["Reemplazar la pantalla"]
    }
  ],
  "atributos": [
    {"clave": "enciende", "pregunta": "¿El dispositivo enciende?"},
    {"clave": "carga", "pregunta": "¿El dispositivo muestra que está cargando?"},
    {"clave": "pantalla_tactil", "pregunta": "¿La pantalla responde al tacto?"}
  ]
}

# Datos de ejemplo (normalmente se cargarían desde un archivo JSON)
datos = {
  "fallas": [
    {
      "nombre": "Batería dañada",
      "atributos": {
        "enciende": False,
        "carga": False,
        "pantalla_tactil": True,
        "microfono": True,
        "bocina": True,
        "voltaje": True,
        "camara": True,
        "sensor": True,
        "antena": True,
        "huella": True
        
      },
      "soluciones": [
        "Reemplazar la batería",
        "Revisar el cargador"
      ]
    },
    {
      "nombre": "Touch",
      "atributos": {
        "enciende": True,
        "carga": True,
        "pantalla_tactil": False,
        "microfono": True,
        "bocina": True,
        "voltaje": True,
        "camara": True,
        "sensor": True,
        "antena": True,
        "huella": True
      },
      "soluciones": [
        "Reemplazar la pantalla"
      ]
    },
    {
      "nombre": "Micrófono no funciona",
      "atributos": {
        "enciende": True,
        "carga": True,
        "pantalla_tactil": True,
        "microfono": False,
        "bocina": True,
        "voltaje": True,
        "camara": True,
        "sensor": True,
        "antena": True,
        "huella": True
      },
      "soluciones": [
        "Revisar permisos de la aplicación",
        "Reemplazar el micrófono"
      ]
    },
    {
      "nombre": "Altavoz no funciona",
      "atributos": {
        "enciende": True,
        "carga": True,
        "pantalla_tactil": True,
        "microfono": True,
        "bocina": False,
        "voltaje": True,
        "camara": True,
        "sensor": True,
        "antena": True,
        "huella": True
      },
      "soluciones": [
        "Revisar configuraciones de sonido",
        "Reemplazar el altavoz"
      ]
    },
    {
      "nombre": "Conector de carga dañado",
      "atributos": {
        "enciende": True,
        "carga": False,
        "pantalla_tactil": True,
        "microfono": True,
        "bocina": True,
        "voltaje": False,
        "camara": True,
        "sensor": True,
        "antena": True,
        "huella": True,
        "conector": True
      },
      "soluciones": [
        "Reparar o reemplazar el conector de carga"
      ]
    },
    {
      "nombre": "Cámara no funciona",
      "atributos": {
        "enciende": True,
        "carga": True,
        "pantalla_tactil": True,
        "microfono": True,
        "bocina": True,
        "voltaje": True,
        "camara": False,
        "sensor": True,
        "antena": True,
        "huella": True
      },
      "soluciones": [
        "Actualizar la aplicación de la cámara",
        "Reemplazar la cámara"
      ]
    },
    {
      "nombre": "Sensor de proximidad defectuoso",
      "atributos": {
        "enciende": True,
        "carga": True,
        "pantalla_tactil": True,
        "microfono": True,
        "bocina": True,
        "voltaje": True,
        "camara": True,
        "sensor": False,
        "antena": True,
        "huella": True
      },
      "soluciones": [
        "Calibrar el sensor de proximidad",
        "Reemplazar el sensor"
      ]
    },
    {
      "nombre": "Wi-Fi no funciona",
      "atributos": {
        "enciende": True,
        "carga": True,
        "pantalla_tactil": True,
        "microfono": True,
        "bocina": True,
        "voltaje": True,
        "camara": True,
        "sensor": True,
        "antena": False,
        "huella": True
      },
      "soluciones": [
        "Reiniciar el router",
        "Actualizar configuraciones Wi-Fi",
        "Reparar el módulo Wi-Fi"
      ]
    },
    {
      "nombre": "Sensor de huella dactilar no funciona",
      "atributos": {
        "enciende": True,
        "carga": True,
        "pantalla_tactil": True,
        "microfono": True,
        "bocina": True,
        "voltaje": True,
        "camara": True,
        "sensor": True,
        "antena": True,
        "huella": False
      },
      "soluciones": [
        "Limpiar el sensor de huella dactilar",
        "Reemplazar el sensor de huella"
      ]
    },
    {
      "nombre": "Display",
      "atributos": {
        "enciende": False,
        "carga": True,
        "pantalla_tactil": True,
        "display": False,
        "microfono": True,
        "bocina": True,
        "voltaje": True,
        "camara": True,
        "sensor": True,
        "antena": True,
        "huella": True
      },
      "soluciones": [
        "Cambiar el display",
        "Checar el conector display"
      ]
    }
  ],
  "atributos": [
    {"clave": "enciende", "pregunta": "¿El dispositivo enciende?"},
    {"clave": "pantalla_tactil", "pregunta": "¿La pantalla responde al tacto?"},
    {"clave": "vibra", "pregunta": "¿El dispositivo vibra o hace sonido al presionar el botón de encendido?"},
    {"clave": "display", "pregunta": "¿La pantalla muestra imagen correctamente?"},
    {"clave": "bocina", "pregunta": "¿El dispositivo reproduce audio correctamente?"},
    {"clave": "voltaje", "pregunta": "¿El dispositivo muestra que está cargando?"},
    {"clave": "camara", "pregunta": "¿La cámara muestra una imagen al usarla?"},
    {"clave": "sensor", "pregunta": "¿La pantalla se apaga correctamente durante las llamadas?"},
    {"clave": "antena", "pregunta": "¿El dispositivo se conecta correctamente a una red?"},
    {"clave": "carga", "pregunta": "¿La batería tiene una duración adecuada?"},
    {"clave": "microfono", "pregunta": "¿El micrófono graba audio correctamente?"},
    {"clave": "conector", "pregunta": "¿El conector de carga muestra signos visibles de daño?"},
    {"clave": "huella", "pregunta": "¿El detecta tu huella?"}
  ]
}



realizar_diagnostico(datos)
