from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from customtkinter import *

'''
nombre: 
apellido: 
---
Ejercicio 9
---
Enunciado:
Ingresar por los cuadros de texto el importe de una compra
y el porcentaje de descuento que se aplicará. Mostrar por alert el importe 
ingresado y el total con el descuento.
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
frame.pack(expand=True, fill="both", pady=20, padx=70)

#Crea una entrada de texto
txt_numero_1 = CTkEntry(master=frame, placeholder_text="Ingrese importe",font=("Calibri", 16), width = 200, 
                                 height=28, border_color="#0b5394", border_width=2.5, text_color="#0b5394")
txt_numero_1.pack(pady=20)

txt_numero_2 = CTkEntry(master=frame, placeholder_text="Ingrese % de descuento",font=("Calibri", 16), width = 200, 
                                 height=28, border_color="#0b5394", border_width=2.5, text_color="#0b5394")
txt_numero_2.pack(pady=21)

#Crea un boton que ejecuta una funcion
boton = CTkButton(master=frame, text="Operar", command=codigo, font=("Arial", 18), width = 160, height=35,
                                 corner_radius=7.5, fg_color="#0b5394", text_color="white")
boton.pack(pady=23)


root.mainloop()