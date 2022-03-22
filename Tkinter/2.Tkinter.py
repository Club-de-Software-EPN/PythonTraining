import tkinter as tk
from tkinter import GROOVE, SUNKEN
from turtle import color

colorVerde = '#C7FF89'
colorAzul = '#042E6C'
colorNegro = '#000000'
colorBlanco = '#FFFFFF'
fuenteTitulos = ('Courie',14,'bold')
fuenteGeneral = ('Courie',11,'normal')

class Ventana:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('Ejemplo 2')
        self.root.resizable(True,True)
        self.root.geometry('600x500')
        self.root.configure(bg=colorVerde)
        self.dibujar()

    def guardarInformacion(self, nombre: str, apellido: str, edad: int):
        print(f'Información {nombre} {apellido} {edad}')

    def saludar(self,texto):
        print('Dices', texto)

    
    
    def dibujar(self):
        titulo = tk.Label(self.root,text='Formulario', bg=colorVerde, font=fuenteTitulos)    
        titulo.place(x=220,y=15)

        texto1 = tk.Label(self.root, text='Ingrese los datos a continuación', bg=colorVerde,
                font=fuenteGeneral, fg=colorAzul)
        texto1.place(x=20, y=60)

        lblNombre = tk.Label(self.root, text='Nombre:', bg=colorVerde, font=fuenteGeneral)
        lblNombre.place(x=20, y=110)

        lblApellido = tk.Label(self.root, text='Apellido:', bg=colorVerde, font=fuenteGeneral)
        lblApellido.place(x=20, y=150)

        lblEdad = tk.Label(self.root, text='Edad:', bg=colorVerde, font=fuenteGeneral)
        lblEdad.place(x=20, y=190)

        # Input
        inputNombre = tk.Entry(self.root, width=20)
        inputNombre.place(x=100,y=110)

        inputApellido = tk.Entry(self.root)
        inputApellido.place(x=100,y=150)

        inputEdad = tk.Entry(self.root)
        inputEdad.place(x=100,y=190)

        # Combobox
        


        def guardarInformacion2():
             print(f'Información {inputNombre.get()} {inputApellido.get()} {inputEdad.get()}')


        # Boton
        # width de los botones es un numero
        btnGuardar = tk.Button(self.root, text='Guardar\nInformación', font=fuenteGeneral, 
                    command=guardarInformacion2, width=15, height=2, bd=2,
                    bg=colorNegro, fg=colorBlanco,
                    relief=SUNKEN)
        btnGuardar.place(x=250,y=300)
             
        # Main loop
        self.root.mainloop()

ventana = Ventana()