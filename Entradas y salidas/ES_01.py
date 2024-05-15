from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from customtkinter import *

'''
nombre: 
apellido: 
---
Ejercicio: Prueba GUI
---
Enunciado:
Mostrar por alert el mensaje "Hola Rio de la Plata"
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

#Crea un boton que ejecuta una funcion
boton = CTkButton(master=frame, text="Saludar", command=codigo, font=("Arial", 18), width = 160, height=35,
                                 corner_radius=7.5, fg_color="#0b5394", text_color="white")
boton.pack(pady=30)


root.mainloop()