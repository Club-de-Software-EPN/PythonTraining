import tkinter as tk
from tkinter import GROOVE, SUNKEN, ttk
from utilidades import center

colorGris = '#B8B9AA'
colorBlanco = '#F7F7F7'
colorVerde = '#1BE518'
colorAmarillo = '#F7FF00'
colorAmarilloOscuro = '#E6DD08'

class Ventana:
    def __init__(self, titulo) -> None:
        self.titulo = titulo
        self.dibujar()
    def dibujar(self):
        root = tk.Tk()
        root.title(self.titulo)
        root.geometry('800x550')
        root.resizable(width=True, height=True)
        center(root)
        root.mainloop()

ventana = Ventana('Ejercicio 1')

