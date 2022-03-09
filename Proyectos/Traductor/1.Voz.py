import pyttsx3

motorVoz = pyttsx3.init()
voices = motorVoz.getProperty('voices')
print(voices)
motorVoz.setProperty('rate',120)
motorVoz.setProperty('voice',voices[0].id)
texto = 'Hoy es el día de la mujer'
motorVoz.say(texto)
motorVoz.runAndWait()
