import pyttsx3

motorVoz = pyttsx3.init()
motorVoz.setProperty('rate',120)
texto = 'Hoy es el día de la mujer'
motorVoz.say(texto)
motorVoz.runAndWait()
