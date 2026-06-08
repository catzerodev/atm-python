from logger_config import registrar_evento


class ATM:

    def __init__(self, cuenta):

        self.cuenta = cuenta

    def consultar_saldo(self):

        print(
            f"💰Saldo actual: S/{self.cuenta.saldo}"
        )

    def depositar(self):

        try:

            monto = float(
                input("💵 Ingrese monto a depositar: ")
            )
            
            self.cuenta.saldo += monto

            self.cuenta.historial.append(
                f"Depósito: S/{monto}"
            )

            registrar_evento(
                f"DEPOSITO - {self.cuenta.tarjeta} - S/{monto}"
            )

            print(
                f"✅ Nuevo saldo: S/{self.cuenta.saldo}"
            )

        except ValueError:

            print("❌Debe ingresar un número.")

    def retirar(self):

        try:

            monto = float(
                input("💸 Ingrese monto a retirar: ")
            )
            
            if monto >= 500:
                
                print(
                    "⚠️  Actividad sospechosa detectada."
                )
                
                registrar_evento(
                    f"ALERTA ACTIVIDAD SOSPECHOSA - {self.cuenta.tarjeta} - S/{monto}"
                )
                

            LIMITE_DIARIO = 1000

            if self.cuenta.retiro_diario + monto > LIMITE_DIARIO:

                print(
                    "🚫 Ha superado el límite diario de retiro."
                )

                return

            if monto <= self.cuenta.saldo:

                self.cuenta.saldo -= monto

                self.cuenta.retiro_diario += monto

                self.cuenta.historial.append(
                    f"Retiro: S/{monto}"
                )

                registrar_evento(
                    f"RETIRO - {self.cuenta.tarjeta} - S/{monto}"
                )

                print(
                    f"✅ Retiro exitoso. Saldo actual: S/{self.cuenta.saldo}"
                )

            else:

                print("🥺 Saldo insuficiente.")

        except ValueError:

            print("Debe ingresar un número.")

    def mostrar_historial(self):

        if len(self.cuenta.historial) == 0:

            print("📭No hay movimientos registrados.")

        else:

            print("\n📋===== HISTORIAL =====")

            for movimiento in self.cuenta.historial:

                print(movimiento)
                