from msilib.schema import Error
from tkinter import messagebox
import re

def center(win): 
    """ centers a tkinter window :param win: the main window or Toplevel window to center """ 
    win.update_idletasks() 
    width = win.winfo_width() 
    frm_width = win.winfo_rootx() - win.winfo_x() 
    win_width = width + 2 * frm_width 
    height = win.winfo_height() 
    titlebar_height = win.winfo_rooty() - win.winfo_y() 
    win_height = height + titlebar_height + frm_width 
    x = win.winfo_screenwidth() // 2 - win_width // 2 
    y = win.winfo_screenheight() // 2 - win_height // 2 
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y)) 
    win.deiconify()

def validarNumero(texto, campo):
    try:
        return int(texto)
    except:
        messagebox.showwarning(message='Solo se aceptan números', title=f'Error en el campo {campo}') 

def validarTexto(texto, campo):
    try:
        return str(texto)
    except:
        messagebox.showwarning(message='Solo se aceptan números', title=f'Error en el campo {campo}') 

def validarCorreoElectronico(correo, campo='Correo electrónico'):
    try:
        emailRegex = r'(^[\w]+)@(\w)+'
        match = re.search(emailRegex, correo)
        if match:
            return correo
        else:
            messagebox.showerror(message='Formato no válido de correo', title=f'Error en el campo {campo}')
            raise Error('error')
    except ValueError:
        print('Error')

         