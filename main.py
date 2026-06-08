from cuenta import Cuenta
from atm import ATM
from seguridad import autenticar, encriptar_pin

cuenta = Cuenta(
    "4532015112830366",
    encriptar_pin("1234"),
    500
)

atm = ATM(cuenta)

if not autenticar(cuenta):
    exit()

while True:

    print("\n===== CAJERO AUTOMÁTICO =====")
    print("1️⃣  Consultar saldo")
    print("2️⃣  Depositar")
    print("3️⃣  Retirar")
    print("4️⃣  Historial")
    print("5️⃣  Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        atm.consultar_saldo()

    elif opcion == "2":

        atm.depositar()

    elif opcion == "3":

        atm.retirar()

    elif opcion == "4":

        atm.mostrar_historial()

    elif opcion == "5":

        print(" 👋 Gracias por usar el ATM")
        break

    else:

        print("Opción inválida")
        
        