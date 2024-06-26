from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
from customtkinter import *

'''
nombre: 
apellido: 
---
Ejercicio 5
---
Enunciado:
Ingresar dos numeros por las cajas de texto, convertirlos a entero y mostrar en el textbox resultado
la suma de dichos numeros.
'''

def codigo():
    pass




#Crea y configura la ventana
set_appearance_mode("dark")
root = CTk()
root.geometry("400x375+50+300")
root.resizable(False, False)
root.title("Colegio Rio de la Plata")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)



#Crea un frame que funciona como padre de el resto de widgets
frame = CTkFrame(master=root)
frame.pack(expand=True, fill="both", pady=20, padx=70)

#Crea una entrada de texto
txt_numero_1 = CTkEntry(master=frame, placeholder_text="Ingrese numero",font=("Calibri", 16), width = 200, 
                                 height=28, border_color="#0b5394", border_width=2.5, text_color="#0b5394")
txt_numero_1.pack(pady=20)

txt_numero_2 = CTkEntry(master=frame, placeholder_text="Ingrese otro numero",font=("Calibri", 16), width = 200, 
                                 height=28, border_color="#0b5394", border_width=2.5, text_color="#0b5394")
txt_numero_2.pack(pady=21)

txt_resultado = CTkEntry(master=frame, placeholder_text="Resultado",font=("Calibri", 16), width = 200, 
                                 height=28, border_color="#0b5394", border_width=2.5, text_color="#0b5394")
txt_resultado.pack(pady=22)

#Crea un boton que ejecuta una funcion
boton = CTkButton(master=frame, text="Sumar", command=codigo, font=("Arial", 18), width = 160, height=35,
                                 corner_radius=7.5, fg_color="#0b5394", text_color="white")
boton.pack(pady=23)


root.mainloop()