import tkinter as tk
from tkinter import GROOVE, SUNKEN, Frame, ttk, NO, messagebox
from BaseDatos2 import BaseDatos
from utilidades import center, validarTexto, validarNumero, \
                        validarCorreoElectronico

colorVerde = '#b4ffff'
colorVerdeOscuro = '#003d33'
colorAzul = '#042E6C'
colorAmarillo = '#F1E790'
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

    def mostrarFrameRegistro(self):
        #print('Mostrando frame registro')
        self.ocultarTodosFrames()
        self.frameRegistro.place(x=0,y=100)

    def mostrarFrameUsuarios(self):
        #print('Mostrando frame usuarios')
        self.ocultarTodosFrames()
        self.frameUsuarios.place(x=0,y=100)

    def ocultarTodosFrames(self):
        #print('Ocultando todos los frames')
        self.frameRegistro.place_forget()
        self.frameUsuarios.place_forget()

    def dibujar(self):

# ---------------------  Encabezado -----------------------------#
        titulo = tk.Label(self.root,text='Sistema Manejo Usuarios', bg=colorVerde, font=fuenteTitulos)    
        titulo.place(x=170,y=15)

        btnRegistro = tk.Button(self.root, text='Registrar Usuarios', font=fuenteGeneral, 
                    command=self.mostrarFrameRegistro, width=15, height=1, bd=2,
                    bg=colorVerdeOscuro, fg=colorBlanco,relief=SUNKEN)
        btnRegistro.place(x=40,y=55)

        btnUsuarios= tk.Button(self.root, text='Usuarios', font=fuenteGeneral, 
                    command=self.mostrarFrameUsuarios, width=15, height=1, bd=2,
                    bg=colorVerdeOscuro, fg=colorBlanco,relief=SUNKEN)
        btnUsuarios.place(x=240,y=55)

        btnSalir= tk.Button(self.root, text='Salir', font=fuenteGeneral, 
                    command=self.root.destroy, width=15, height=1, bd=2,
                    bg=colorVerdeOscuro, fg=colorBlanco,relief=SUNKEN)
        btnSalir.place(x=440,y=55)
        

# ---------------------  Frame Usuario -----------------------------#    
        self.frameUsuarios = Frame(self.root, width=600, height=400, bg=colorVerde, relief='sunken')
        self.frameUsuarios.place(x=0,y=100)

        texto1 = tk.Label(self.frameUsuarios, text='Datos de los usuarios', bg=colorVerde,
                font=fuenteGeneral, fg=colorAzul)
        texto1.place(x=20, y=20)

        # Tabla
        columnas = ('nombre','apellido','edad','sexo','correo','formacion')
        tblUsr = ttk.Treeview(self.frameUsuarios, height=15, columns=columnas, show='headings')
        tblUsr.place(x=15, y=60)

        for heading in columnas:
            tblUsr.heading(heading, text=heading)
            tblUsr.column(heading, minwidth=95, width=95, stretch=NO)

        def llenarDatos():
            data = self.conexionDatos.obtenerDatosUsuarios()
            for fila in data:
                tblUsr.insert('','end', values=fila)

        btnLlenarDatos= tk.Button(self.frameUsuarios, text='Cargar Usuario', font=('Courie',10,'normal'), 
                    command=llenarDatos, height=1, bd=2,bg=colorVerdeOscuro, fg=colorBlanco,relief=SUNKEN)
        btnLlenarDatos.place(x=300,y=20)


# ---------------------  Frame Registro -----------------------------#

        self.frameRegistro = Frame(self.root, width=600, height=400, bg=colorVerde, relief='sunken')
        self.frameRegistro.place(x=0,y=100)

        texto1 = tk.Label(self.frameRegistro, text='Ingrese los datos a continuación', bg=colorVerde,
                font=fuenteGeneral, fg=colorAzul)
        texto1.place(x=20, y=60)

        lblNombre = tk.Label(self.frameRegistro, text='Nombre:', bg=colorVerde, font=fuenteGeneral)
        lblNombre.place(x=20, y=110)

        lblApellido = tk.Label(self.frameRegistro, text='Apellido:', bg=colorVerde, font=fuenteGeneral)
        lblApellido.place(x=20, y=150)

        lblEdad = tk.Label(self.frameRegistro, text='Edad:', bg=colorVerde, font=fuenteGeneral)
        lblEdad.place(x=20, y=190)
        
        lblSexo = tk.Label(self.frameRegistro, text='Sexo:', bg=colorVerde, font=fuenteGeneral)
        lblSexo.place(x=20, y=230)

        lblCorreo = tk.Label(self.frameRegistro, text='Correo:', bg=colorVerde, font=fuenteGeneral)
        lblCorreo.place(x=20, y=270)

        lblFormacion = tk.Label(self.frameRegistro, text='Formación:', bg=colorVerde, font=fuenteGeneral)
        lblFormacion.place(x=20, y=310)

        # Input
        inputNombre = tk.Entry(self.frameRegistro, width=20)
        inputNombre.place(x=100,y=110)

        inputApellido = tk.Entry(self.frameRegistro)
        inputApellido.place(x=100,y=150)

        inputEdad = tk.Entry(self.frameRegistro)
        inputEdad.place(x=100,y=190)

        inputCorreo = tk.Entry(self.frameRegistro)
        inputCorreo.place(x=100,y=270)

        # Radio Button
        radioSexo = tk.StringVar()
        def selectSexo():
            print(f'Opcion sexo seleccionada: {radioSexo.get()}')

        radioM = tk.Radiobutton(self.frameRegistro, text='Masculino', value='M', bg=colorVerde, 
                                variable=radioSexo, command=selectSexo, tristatevalue=0)
        radioM.place(x=100, y=230)

        radioF = tk.Radiobutton(self.frameRegistro, text='Femenino', value='F', bg=colorVerde, 
                                variable=radioSexo, command=selectSexo, tristatevalue=0)
        radioF.place(x=200, y=230)

        # Combobox Formación Academica
        listaFormacionAcademica = ['Educación Primaria','Educación Secundaria','Tecnología','Superior']
        cmbFormacion = tk.ttk.Combobox(self.frameRegistro, values=listaFormacionAcademica, width=21)
        cmbFormacion.place(x=100, y=310)

        def guardarInformacion2():                        
            try:
                # Validar
                validarCorreoElectronico(inputCorreo.get())
                validarNumero(inputEdad.get(), 'Edad')
                validarTexto(inputNombre.get(), 'Nombre')
                validarTexto(inputApellido.get(), 'Apellido')               
                # Guardar
                self.conexionDatos.insertarUsuario(inputNombre.get(), inputApellido.get(), 
                                                    inputEdad.get(), radioSexo.get(),inputCorreo.get(),
                                                    cmbFormacion.get())
                messagebox.showinfo(message=f'El usuario {inputNombre.get()} ha sido registrado', 
                                    title=f'Usario Registrado') 
            except:
                messagebox.showwarning(message='Usuario no registrado', title=f'No se registró el usuario') 

        # width de los botones es un numero
        btnGuardar = tk.Button(self.frameRegistro, text='Guardar\nInformación', font=fuenteGeneral, 
                    command=guardarInformacion2, width=15, height=2, bd=2,
                    bg=colorNegro, fg=colorBlanco,
                    relief=SUNKEN)
        btnGuardar.place(x=400,y=200)
             

# Main loop
        self.root.mainloop()

ventana = Ventana()