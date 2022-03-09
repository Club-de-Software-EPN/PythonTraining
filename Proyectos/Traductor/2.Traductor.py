from googletrans import Translator
import pyttsx3

motorVoz = pyttsx3.init()
traductor = Translator()
motorVoz.setProperty('rate',120)

try:
    with open('Proyectos/Traductor/libro.txt',mode='r') as miArchivo:
        # Realziar traducción
        texto = miArchivo.read()
        textoTraducido = traductor.translate(text=texto).text
        # Escribir la traducción en un txt
        txtsalida = open('Proyectos/Traductor/libroTraducido.txt','w')
        txtsalida.write(textoTraducido)
        # Lee el audiolibro
        motorVoz.say('Audiolibro traducido de 100 años de soledad')
        motorVoz.say(textoTraducido)
        motorVoz.runAndWait()
except FileNotFoundError as error:
    print('Error: ', error)
