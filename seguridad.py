import hashlib
from logger_config import registrar_evento


def encriptar_pin(pin):
    return hashlib.sha256(
        pin.encode()
    ).hexdigest()


def validar_luhn(numero):

    suma = 0
    invertir = numero[::-1]

    for i in range(len(invertir)):

        digito = int(invertir[i])

        if i % 2 == 1:

            digito *= 2

            if digito > 9:
                digito -= 9

        suma += digito

    return suma % 10 == 0


def autenticar(cuenta):

    print("🏦✨ Bienvenido al sistema bancario ✨🏦")

    while cuenta.intentos < 3:

        tarjeta = input("💳 Ingrese número de tarjeta: ")

        if not validar_luhn(tarjeta):

            print("❌ Número de tarjeta inválido.")

            registrar_evento(
                f"TARJETA INVALIDA - {tarjeta}"
            )

            continue

        pin = input("🔐 Ingrese PIN: ")

        pin_encriptado = encriptar_pin(pin)

        if (
            tarjeta == cuenta.tarjeta
            and pin_encriptado == cuenta.pin
        ):

            registrar_evento(
                f"LOGIN EXITOSO - {cuenta.tarjeta}"
            )

            print("\n✅ Acceso exitoso. ¡Bienvenido!👋🤠")
            return True

        else:

            registrar_evento(
                f"LOGIN FALLIDO - {tarjeta}"
            )

            cuenta.intentos += 1

            print(
                f"⚠️ Credenciales incorrectas. Intento {cuenta.intentos}/3"
            )

    cuenta.bloqueada = True

    registrar_evento(
        f"CUENTA BLOQUEADA - {cuenta.tarjeta}"
    )

    print(
        "🚫 Cuenta bloqueada por demasiados intentos."
    )

    return False