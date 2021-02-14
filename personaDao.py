from persona import Persona
from conexion import Conexion
from logger_base import logger

class PersonaDao:
    
    __SELECIONAR = 'SELECT * FROM persona  ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre,apelido,email) VALUES(%s,%s,%s)  '
    @classmethod
    def seleccionar(cls):
        cursor = Conexion.obtenerCursor()
        logger.debug(cursor.mogrify(cls.__SELECIONAR))
        cursor.execute(cls.__SELECIONAR)
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            persona = Persona(registro[0],registro[1],registro[2],registro[3])
            personas.append(persona)
        Conexion.cerrar()
        return personas
        
    @classmethod
    def insertar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email())
            cursor.execute(cls.__INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepción al insertar persona:{e}') 
        finally:
            Conexion.cerrar()
        
           
if __name__ == '__main__':
    #personas = PersonaDao.seleccionar()
    #for persona in personas:
     #   logger.debug(persona)
      #  logger.debug(persona.get_id())
    persona = Persona(nombre='Pedro', apellido='Najera', email='pnajera@mail.com')
    personas_insertadas = PersonaDao.insertar(persona)
    logger.debug(f'Personas insertados: {personas_insertadas}')
    