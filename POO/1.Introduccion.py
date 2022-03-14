# POO
# Prototipo, plantilla

# Clase 
# Atributos (caracterísctica y métodos)
# ADT -> Abstract Data Type

class Curso:
    # Atributos
    # Métodos
    pass

class Alumno:
    pass

# Instanciar una clase -> objeto
curso1 = Curso()
curso2 = Curso()

print(type(curso1))

cursos = [curso1, curso2]
print(cursos)


texto = 'anderson'
print(texto.capitalize())

# POO en python
print('Comprobar si curso1 es instancia de Curso: ', isinstance(curso1,Curso))
print('Comprobar si curso1 es instancia de Alumno: ', isinstance(curso1,Alumno))
