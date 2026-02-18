import tkinter as tk
from tkinter import ttk
from testing.teste import tablas

#Ventana principal
ventana = tk.Tk()
ventana.title("Sistema Inmobiliario")
ventana.geometry("800x500")
#Texto de la ventana
titulo =tk.Label(ventana,text="INMOBILIARIA SYSTEM",
                font=("Arial", 18))
titulo.pack(pady=20)

#Ventana
tablas(ventana)

ventana.mainloop()