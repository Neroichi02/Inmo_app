import tkinter as tk

#Ventana principal
ventana = tk.Tk()
ventana.title("Sistema Inmobiliario")
ventana.geometry("800x500")

titulo =tk.Label(ventana,text="INMOBILIARIA SYSTEM",
                 font=("Arial", 18))
titulo.pack(pady=20)

ventana.mainloop()