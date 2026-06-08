import logging

logging.basicConfig(
    filename="seguridad_atm.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def registrar_evento(mensaje):

    logging.info(mensaje)