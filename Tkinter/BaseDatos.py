import psycopg2

# 1. Establecer la conexión con la base de datos
conexion = psycopg2.connect(host='localhost', database='Usuarios', user='postgres', password='anderson', port=5432)
# 2. Creamos el cursos
cursor = conexion.cursor()
# Ejecutamos
cursor.execute('SELECT * FROM public."Usuarios";')
# Visualizar los resultados
for data in cursor.fetchall():
    print(data)

# Insert (sentencia insert) (valores)

sentenciaInsert = '''INSERT INTO public."Usuarios"(
	nombre, apellido, edad, sexo)
	VALUES (%s, %s, %s, %s);
    '''
valores = ('Anderson2','Cardenas',22,'M')
valores2 = ('Anderson3','Cardenas',22,'M')
cursor.execute(sentenciaInsert,valores)
cursor.execute(sentenciaInsert,valores2)
conexion.commit()
registrosInsertados = cursor.rowcount
print('Se insertaron ', registrosInsertados)



