from persona import Persona
from conexion import Conexion
from logger_base import logger

class PersonaDao:
    
    __SELECIONAR = 'SELECT * FROM persona  ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s,%s,%s)  '
    __ACTUALIZAR = 'UPDATE persona  SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s '
    __ELIMINAR = 'DELETE FROM persona  WHERE id_persona=%s'
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
    @classmethod
    def actualizar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email(), persona.get_id())
            cursor.execute(cls.__ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepción al actualizar persona:{e}') 
        finally:
            Conexion.cerrar()
    @classmethod
    def eliminar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            valores = (persona.get_id(),)
            cursor.execute(cls.__ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepción al eliminar persona:{e}') 
        finally:
            Conexion.cerrar()
        
           
if __name__ == '__main__':
    #personas = PersonaDao.seleccionar()
    #for persona in personas:
     #   logger.debug(persona)
      #  logger.debug(persona.get_id())
    #persona2 = Persona(nombre='Juans', apellido='Acosta', email='Joder@mail.com')
    #personas_insertadas = PersonaDao.insertar(persona2)
    #logger.debug(f'Personas insertados: {personas_insertadas}')
    #persona = Persona(nombre='Daniel',apellido='contreras',email='dcontreras@gmail.com',id_persona=15)
    #personas_actualizadas=  PersonaDao.actualizar(persona)
    #logger.debug(f'Personas Actualizadas {personas_actualizadas}')
    persona = Persona(16)
    persona_eliminada = PersonaDao.eliminar(persona)
    logger.debug('Persona eliminada {persona_eliminada}')
    