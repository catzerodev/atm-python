class Cuenta:

    def __init__(self, tarjeta, pin, saldo):

        self.tarjeta = tarjeta
        self.pin = pin
        self.saldo = saldo

        self.historial = []

        self.intentos = 0

        self.bloqueada = False

        self.retiro_diario = 0