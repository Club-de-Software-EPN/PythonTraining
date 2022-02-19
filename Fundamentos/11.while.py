#x = True

#while x:
    #print('Saludar')


y = 1
while y<5 :
    y+=1
    print(y)

def menu():
    print('1.')
    print('4.Salir')
    opcion = input('Ingresa la opción')
    return opcion

def main():
    terminarJuego = False
    while terminarJuego == False:
        opcionMenu = menu()
        if opcionMenu == '4':
            terminarJuego = True
    

main()
