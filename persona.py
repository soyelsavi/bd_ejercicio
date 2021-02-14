from logger_base import logger

class Persona:
   
        
    def __init__ (self, id_persona = None, nombre = None, apellido = None,email = None):
        
        self.__id_persona = id_persona
        self.__nombre =  nombre
        self.__apellido = apellido
        self.__email = email
    
    def __str__(self):
        return(
            f'Id Persona: {self.__id_persona} '
            f'Nombre: {self.__nombre}, '
            f'Apellido: {self.__apellido}, '
            f'Email: {self.__email} '
        )
    
    def get_id(self):
        return self.__id_persona
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_email(self):
        return self.__email
    def set_id(self,id_persona):
        self.__id_persona = id_persona
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def set_apellido(self,apellido):
        self.__apellido = apellido
    def set_email(self,email):
        self.__email = email

if __name__ == '__main__':
    persona1 = Persona(1,'juan', 'saravia', 'je@gmail')
    logger.debug(persona1)
    persona2 = Persona(nombre='Karla',apellido='Echeverry', email='ke@gmail.com')
    logger.debug(persona2)