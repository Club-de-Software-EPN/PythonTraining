import tkinter as tk
from tkinter import GROOVE, SUNKEN, Button, Frame, ttk
from tkinter import messagebox
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
        root.configure(bg=colorGris)
        center(root)

        labelTitulo = tk.Label(root, text='Ejercicio 1', bg=colorAmarilloOscuro, 
                                fg=colorBlanco, font = ('Courie', 14, 'bold'),
                                width=20
                                )
        labelTitulo.place(x=280,y=10)

        # Frames -> estáticos


        # Frame 1
        frame1 = Frame(root, width=250, height=250, bd=3,
                        bg=colorGris, relief='groove')
        frame1.place(x=15,y=55)
        
        titFrame1 = tk.Label(root, text='Suma', bg='mintcream', font=('Courie',11))
        titFrame1.place(x=30,y=45)

        entryValor1 = ttk.Entry(frame1)
        entryValor1.place(x=30, y=50)

        entryValor2 = ttk.Entry(frame1)
        entryValor2.place(x=30, y=80)

       
        resultado = 0

        lblResultado = tk.Label(frame1, text='La suma es: '+str(resultado), 
                    bg= colorAmarilloOscuro, font=('Courie',10))
        lblResultado.place(x=50, y=115)

        def validarNumero(texto, campo):
            try:
                return int(texto)
            except:
                messagebox.showwarning(message='Solo se aceptan números', title=f'Error en el campo {campo}')            
        def sumar():
            try:
                x1 = validarNumero(entryValor1.get(),'Valor 1')
                x2 = validarNumero(entryValor2.get(),'Valor 2')                
                lblResultado.config(text='La suma es: '+str(x1+x2))
            except:
                messagebox.showerror(message='Error al sumar', title=f'Error')

        btnSumar = Button(frame1, text='Sumar', command=sumar, width=10, bd=2,
                            bg=colorBlanco
                            )
        btnSumar.place(x=60,y=150)


        root.mainloop()

ventana = Ventana('Ejercicio 1')

