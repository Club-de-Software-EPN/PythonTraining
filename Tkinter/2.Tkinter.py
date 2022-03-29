import tkinter as tk
from tkinter import GROOVE, SUNKEN, Frame, ttk
from turtle import color

from sympy import root
from BaseDatos2 import BaseDatos
from utilidades import center

colorVerde = '#C7FF89'
colorAzul = '#042E6C'
colorNegro = '#000000'
colorBlanco = '#FFFFFF'
fuenteTitulos = ('Courie',14,'bold')
fuenteGeneral = ('Courie',11,'normal')

class Ventana:
    def __init__(self) -> None:
        self.conexionDatos = BaseDatos('Usuarios')
        self.root = tk.Tk()
        self.root.title('Usuarios')
        self.root.resizable(True,True)
        self.root.geometry('600x500')
        center(self.root)
        self.root.configure(bg=colorVerde)
        self.frameRegistro = None
        self.frameUsuarios = None
        self.dibujar()
 
      

    def guardarInformacion(self, nombre: str, apellido: str, edad: int):
        print(f'Información {nombre} {apellido} {edad}')

    def saludar(self,texto):
        print('Dices', texto)

    def dibujar(self):
        titulo = tk.Label(self.root,text='Formulario', bg=colorVerde, font=fuenteTitulos)    
        titulo.place(x=220,y=15)

        self.frameRegistro = Frame(self.root, width=600, height=400, bg=colorAzul, relief='sunken')
        self.frameRegistro.place(x=0,y=100)

        texto1 = tk.Label(self.root, text='Ingrese los datos a continuación', bg=colorVerde,
                font=fuenteGeneral, fg=colorAzul)
        texto1.place(x=20, y=60)

        lblNombre = tk.Label(self.root, text='Nombre:', bg=colorVerde, font=fuenteGeneral)
        lblNombre.place(x=20, y=110)

        lblApellido = tk.Label(self.root, text='Apellido:', bg=colorVerde, font=fuenteGeneral)
        lblApellido.place(x=20, y=150)

        lblEdad = tk.Label(self.root, text='Edad:', bg=colorVerde, font=fuenteGeneral)
        lblEdad.place(x=20, y=190)
        
        lblSexo = tk.Label(self.root, text='Sexo:', bg=colorVerde, font=fuenteGeneral)
        lblSexo.place(x=20, y=230)

        lblCorreo = tk.Label(self.root, text='Correo:', bg=colorVerde, font=fuenteGeneral)
        lblCorreo.place(x=20, y=270)

        lblFormacion = tk.Label(self.root, text='Formación:', bg=colorVerde, font=fuenteGeneral)
        lblFormacion.place(x=20, y=310)

        # Input
        inputNombre = tk.Entry(self.root, width=20)
        inputNombre.place(x=100,y=110)

        inputApellido = tk.Entry(self.root)
        inputApellido.place(x=100,y=150)

        inputEdad = tk.Entry(self.root)
        inputEdad.place(x=100,y=190)

        inputCorreo = tk.Entry(self.root)
        inputCorreo.place(x=100,y=270)

        # Radio Button
        radioSexo = tk.StringVar()
        def selectSexo():
            print(f'Opcion sexo seleccionada: {radioSexo.get()}')

        radioM = tk.Radiobutton(self.root, text='Masculino', value='M', bg=colorVerde, 
                                variable=radioSexo, command=selectSexo, tristatevalue=0)
        radioM.place(x=100, y=230)

        radioF = tk.Radiobutton(self.root, text='Femenino', value='F', bg=colorVerde, 
                                variable=radioSexo, command=selectSexo, tristatevalue=0)
        radioF.place(x=200, y=230)

        # Combobox Formación Academica
        listaFormacionAcademica = ['Educación Primaria','Educación Secundaria','Tecnología','Superior']
        cmbFormacion = tk.ttk.Combobox(self.root, values=listaFormacionAcademica, width=21)
        cmbFormacion.place(x=100, y=310)

        def guardarInformacion2():
            print(f'Información {inputNombre.get()} {inputApellido.get()} {inputEdad.get()} {cmbSexo.get()}')
            self.conexionDatos.insertarUsuario(inputNombre.get(), inputApellido.get(), inputEdad.get(), cmbSexo.get())

        # width de los botones es un numero
        btnGuardar = tk.Button(self.root, text='Guardar\nInformación', font=fuenteGeneral, 
                    command=guardarInformacion2, width=15, height=2, bd=2,
                    bg=colorNegro, fg=colorBlanco,
                    relief=SUNKEN)
        btnGuardar.place(x=250,y=330)
             
        # Main loop
        self.root.mainloop()

ventana = Ventana()