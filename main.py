import pandas as pd
import csv
from tkinter import *
from random import randint

# Datos globales
BACKGROUND_COLOR = "#B1DDC6"
correctas = 0
incorrectas = 0

# Lista no aprendida
with open("data/already_learn.csv", "w") as learn_words:
    data_already_learn = csv.writer(learn_words)
# Lectura de palabras

data_frame = pd.read_csv('data/french_words.csv')
datos_palabras = pd.DataFrame.from_dict(data_frame)
# print(data_frame)  # Imprime todo
# print(data_frame["French"])  # Imprime la primer columna con las palabras en frances
# print(data_frame["French"][0]) # Imprime de la primer columna el valor que le demos al numero
# Def

num_random = {}

def palabra_random():
    global num_random, contador  # Variables globales
    window.after_cancel(contador)  # reinicia el tiempo si cambiamos antes nosotros
    num_random = randint(0, len(data_frame) - 1)
    carta_elegida = data_frame["French"][num_random]
    canvas_frontal.itemconfig(texto_principal, text="French", fill="black")
    canvas_frontal.itemconfig(texto_respuesta, text=carta_elegida)
    canvas_frontal.itemconfig(imagen, image=imagen_delantera)
    contador = window.after(2000, vuelta_de_carta)  # de nuevo comienza el contador si no elegimos nada y cambia
    return carta_elegida

def vuelta_de_carta():
    global num_random
    carta_elegida = data_frame["English"][num_random]
    canvas_frontal.itemconfig(texto_principal, text="English", fill="white")
    canvas_frontal.itemconfig(texto_respuesta, text=carta_elegida)
    canvas_frontal.itemconfig(imagen, image=imagen_trasera)

def boton_correcto_presionado():
    global correctas
    correctas += 1
    palabra_random()
    label_correctas.config(text=f"Correctas: {correctas}")

def boton_incorrecto_presionado():
    global incorrectas
    incorrectas += 1
    palabra_random()
    label_incorrectas.config(text=f"Incorrectas: {incorrectas}")


# Ventana y tamaño
window = Tk()
window.title("Estudiando con cartas")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # el tamaño entre la ventana y los widgets

contador = window.after(2000, func=vuelta_de_carta)

# Etiqueta para contador de correctas
label_correctas = Label(text="Correctas: 0", font=("Arial", 20, "bold"), bg=BACKGROUND_COLOR)
label_correctas.grid(column=0, row=2)

# Etiqueta para contador de incorrectas
label_incorrectas = Label(text="Incorrectas: 0", font=("Arial", 20, "bold"), bg=BACKGROUND_COLOR)
label_incorrectas.grid(column=1, row=2)

# Imagen frontal
canvas_frontal = Canvas(width=800, height=526)
imagen_delantera = PhotoImage(file="images\card_front.png")  # Con PhotoImage vamos a ubicar el archivo/foto a usar
imagen_trasera = PhotoImage(file="images\card_back.png")
imagen = canvas_frontal.create_image(400, 263, image=imagen_delantera)  # Ubicar la imagen en el centro.
texto_principal = canvas_frontal.create_text(400, 150, text="", font=("Arial", 40, "italic"))  # El texto va mejor aca para ubicarlo
texto_respuesta = canvas_frontal.create_text(400, 263, text="", font=("Arial", 60, "bold"))  # El texto va mejor aca para ubicarlo
canvas_frontal.config(bg=BACKGROUND_COLOR, highlightthickness=0)  # Cambiamos el color de la ventana/imagen
canvas_frontal.grid(column=0, row=0, columnspan=2)

# Imagen icono acertado
canvas_acertado = Canvas(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)
imagen_correcto = PhotoImage(file="images\correct.png")  # Con PhotoImage vamos a ubicar el archivo/foto a usar
# Imagen icono equivocado
canvas_equivocado = Canvas(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)
imagen_incorrecto = PhotoImage(file="images\wrong.png")  # Con PhotoImage vamos a ubicar el archivo/foto a usar

# Boton correcto
boton_correcto = Button(image=imagen_correcto, highlightthickness=0, command=boton_correcto_presionado)
boton_correcto.grid(column=0, row=1)

# Boton incorrecto
boton_incorrecto = Button(image=imagen_incorrecto, highlightthickness=0, command=boton_incorrecto_presionado)
boton_incorrecto.grid(column=1, row=1)


palabra_random()

window.mainloop()

