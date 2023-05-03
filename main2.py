import random
import pandas as pd
from tkinter import *

# Datos globales
BACKGROUND_COLOR = "#B1DDC6"
# Lectura de palabras

data = pd.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient="records")

# Ventana y tamaño
window = Tk()
window.title("Estudiando con cartas")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  # el tamaño entre la ventana y los widgets

# Imagen frontal
canvas_frontal = Canvas(width=800, height=526)
imagen_delantera = PhotoImage(file="images\card_front.png")  # Con PhotoImage vamos a ubicar el archivo/foto a usar
canvas_frontal.create_image(400, 263, image=imagen_delantera)  # Ubicar la imagen en el centro.
texto_principal = canvas_frontal.create_text(400, 150, text="", font=("Arial", 40, "italic"))  # El texto va mejor aca para ubicarlo
texto_frances = canvas_frontal.create_text(400, 263, text="", font=("Arial", 60, "bold"))  # El texto va mejor aca para ubicarlo
canvas_frontal.config(bg=BACKGROUND_COLOR, highlightthickness=0)  # Cambiamos el color de la ventana/imagen
canvas_frontal.grid(column=0, row=0, columnspan=2)


# Imagen icono acertado
canvas_acertado = Canvas(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)
imagen_correcto = PhotoImage(file="images\correct.png")  # Con PhotoImage vamos a ubicar el archivo/foto a usar
# Imagen icono equivocado
canvas_equivocado = Canvas(width=100, height=100, highlightthickness=0, bg=BACKGROUND_COLOR)
imagen_incorrecto = PhotoImage(file="images\wrong.png")  # Con PhotoImage vamos a ubicar el archivo/foto a usar


# Def random
def palabra_random():
    current_card = random.choice(to_learn)
    canvas_frontal.itemconfig(texto_principal, text="French")
    canvas_frontal.itemconfig(texto_frances, text=current_card["French"])

# Boton correcto
boton_correcto = Button(image=imagen_correcto, highlightthickness=0, command=palabra_random)
boton_correcto.grid(column=0, row=1)

# Boton incorrecto
boton_incorrecto = Button(image=imagen_incorrecto, highlightthickness=0, command=palabra_random)
boton_incorrecto.grid(column=1, row=1)

palabra_random()



window.mainloop()
