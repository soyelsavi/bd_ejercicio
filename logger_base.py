import logging
# Variable a importar

logger = logging

logger.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s ] %(message)s ',
                   datefmt='%I: %M: %S: %p ',
                   handlers=[
                       logging.FileHandler('capa_datos.log'),
                       logging.StreamHandler()
                   ])
if __name__ == '__main__':
    logging.warning('Mesaje a nivel WarningS')
    logging.info('Mensaje a nivel info')
    logging.debug('Mensaje a nivel debug')
    logging.error('Ocurrion un error en la base de datos')
