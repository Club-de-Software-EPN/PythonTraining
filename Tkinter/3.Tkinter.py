import tkinter as tk
from tkinter import GROOVE, SUNKEN, ttk

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

colorGris = '#B8B9AA'
colorBlanco = '#F7F7F7'
colorVerde = '#1BE518'
colorAmarillo = '#F7FF00'

def main():
    root = tk.Tk()
    root.title('Ejercicio 1')
    root.geometry('800x550')
    root.resizable(width=True, height=True)
