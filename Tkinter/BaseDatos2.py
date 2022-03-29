import psycopg2
import uuid

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

    def insertarUsuario(self,nombre, apellido, edad, sexo, correo, formacion):
        idU = str(uuid.uuid4())
        valores = (idU,nombre, apellido,edad, sexo, correo, formacion)
        sentenciaInsert = '''INSERT INTO public."Usuarios"(
            id, nombre, apellido, edad, sexo, correo, formacion)
	        VALUES (%s, %s, %s, %s, %s, %s, %s);
            '''
        self.cursor.execute(sentenciaInsert,valores)
        self.conexion.commit()

    def obtenerDatosUsuarios(self):
        self.cursor.execute('''SELECT nombre, apellido, edad, sexo, correo, formacion
	                    FROM public."Usuarios";''')
        datosUsuarios = self.cursor.fetchall();
        #for data in datosUsuarios:
            #print(data)
        return datosUsuarios
