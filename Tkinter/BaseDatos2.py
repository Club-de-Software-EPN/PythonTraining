import psycopg2

class BaseDatos:

    def __init__(self, baseDatos: str)-> None:
        self.cursor = None
        self.baseDatos = baseDatos
        self.conexion = None
        self.conectar()
      
    def conectar(self):
        try:
            print('Base: ',self.baseDatos)
            self.conexion = psycopg2.connect(host='localhost', 
                                            database=str(self.baseDatos),
                                            user='postgres', 
                                            password='anderson', 
                                            port=5432)
            print('La conexión se ha realizado')
            self.cursor = self.conexion.cursor()

        except:
            print('Error no se pudo conectar a esa instancia de la base de datos')

    def insertarUsuario(self,nombre, apellido, edad, sexo):
        valores = (nombre, apellido,edad, sexo)
        sentenciaInsert = '''INSERT INTO public."Usuarios"(
	        nombre, apellido, edad, sexo)
	        VALUES (%s, %s, %s, %s);
            '''
        self.cursor.execute(sentenciaInsert,valores)
        self.conexion.commit()
