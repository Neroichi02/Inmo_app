import tkinter as tk
from tkinter import ttk

def tablas(ventana):
    
    tabla = ttk.Treeview(ventana)
    tabla["columns"] = ("Tipo", "Operaciones", "Dormitorios", "Precios", "Localidad")

    # Configurar columna #0 
    tabla.column("#0", width=0, stretch=tk.NO)

    # Configurar otras columnas
    tabla.column("Tipo", anchor=tk.CENTER, width=100)
    tabla.column("Operaciones", anchor=tk.CENTER, width=100)
    tabla.column("Dormitorios", anchor=tk.CENTER, width=100)
    tabla.column("Precios", anchor=tk.CENTER, width=100)
    tabla.column("Localidad", anchor=tk.CENTER, width=100)

    # Encabezados
    tabla.heading("Tipo", text="Tipo")
    tabla.heading("Operaciones", text="Operaciones")
    tabla.heading("Dormitorios", text="Dormitorios")
    tabla.heading("Precios", text="Precios")
    tabla.heading("Localidad", text="Localidad")

    tabla.pack(pady=20)
