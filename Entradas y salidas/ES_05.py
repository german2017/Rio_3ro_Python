from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from customtkinter import *

'''
nombre: 
apellido: 
---
Ejercicio 4
---
Enunciado:
Al presionar el botón  'Saludar', se deberá obtener un nombre 
utilizando el Dialog Prompt y luego mostrarlo en la caja de 
texto entrada.
'''

def codigo():
    pass




#Crea y configura la ventana
set_appearance_mode("dark")
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
txt_numero_1 = CTkEntry(master=frame, placeholder_text="Ingrese numero",font=("Calibri", 16), width = 200, 
                                 height=28, border_color="#0b5394", border_width=2.5, text_color="#0b5394")
txt_numero_1.pack(pady=20)

txt_numero_2 = CTkEntry(master=frame, placeholder_text="Ingrese otro numero",font=("Calibri", 16), width = 200, 
                                 height=28, border_color="#0b5394", border_width=2.5, text_color="#0b5394")
txt_numero_2.pack(pady=21)

#Crea un boton que ejecuta una funcion
boton = CTkButton(master=frame, text="Sumar", command=codigo, font=("Arial", 18), width = 160, height=35,
                                 corner_radius=7.5, fg_color="#0b5394", text_color="white")
boton.pack(pady=25)


root.mainloop()