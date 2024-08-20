from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from customtkinter import *

'''
nombre: 
apellido: 
---
Ejercicio 8
---
Enunciado:
Al presionar el botón  'Calcular', se deberá obtener la tarifa de un servicio ingresada en la caja de texto. Luego por prompt ingresar
el valor del porcentaje de incremento que se debera aplicar (por ej 15) y mostrar por prompt el importe con el porcentaje aplicado.
'''

def codigo():
    pass




#Crea y configura la ventana
set_appearance_mode("light")
root = CTk()
root.geometry("400x275+50+300")
root.resizable(False, False)
root.title("Colegio Rio de la Plata")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)



#Crea un frame que funciona como padre de el resto de widgets
frame = CTkFrame(master=root)
frame.pack(expand=True, fill="both", pady=10, padx=70)

#Crea una entrada de texto
entrada = CTkEntry(master=frame, placeholder_text="Ingrese el importe",font=("Calibri", 16), width = 200, 
                                 height=28, border_color="#0b5394", border_width=2.5, text_color="#0b5394")
entrada.pack(pady=20)

#Crea un boton que ejecuta una funcion
boton = CTkButton(master=frame, text="Calcular", command=codigo, font=("Arial", 18), width = 160, height=35,
                                 corner_radius=7.5, fg_color="#0b5394", text_color="white")
boton.pack(pady=30)


root.mainloop()