# 🏧 ATM Seguro en Python

Proyecto académico desarrollado en Python que simula el funcionamiento de un Cajero Automático (ATM) incorporando medidas de seguridad, autenticación de usuarios, manejo de excepciones y registro de eventos.

## 📋 Características

### 🔐 Seguridad

* Autenticación mediante número de tarjeta y PIN.
* PIN protegido mediante hash SHA-256.
* Validación de tarjetas utilizando el algoritmo de Luhn.
* Bloqueo automático de cuenta después de 3 intentos fallidos.
* Detección de actividad sospechosa en retiros de alto monto.
* Límite de retiro diario.

### 💳 Operaciones Bancarias

* Consulta de saldo.
* Depósito de dinero.
* Retiro de dinero.
* Historial de transacciones.

### 📝 Auditoría y Logs

* Registro de eventos en un archivo `seguridad_atm.log`.
* Almacenamiento de:

  * Inicios de sesión exitosos.
  * Intentos fallidos.
  * Depósitos.
  * Retiros.
  * Actividades sospechosas.
  * Bloqueos de cuenta.

### ⚠️ Manejo de Errores

* Uso de `try-except` para evitar que la aplicación se cierre por entradas incorrectas del usuario.

---

## 📂 Estructura del Proyecto

```text
ATM/
│
├── main.py
├── atm.py
├── cuenta.py
├── seguridad.py
├── logger_config.py
├── seguridad_atm.log
└── README.md
```

### Descripción de archivos

| Archivo            | Función                                         |
| ------------------ | ----------------------------------------------- |
| `main.py`          | Menú principal y ejecución del programa         |
| `atm.py`           | Operaciones del cajero automático               |
| `cuenta.py`        | Clase Cuenta                                    |
| `seguridad.py`     | Autenticación, hash SHA-256 y algoritmo de Luhn |
| `logger_config.py` | Configuración de logs                           |

---

## 🚀 Cómo ejecutar

### Requisitos

* Python 3.10 o superior

### Ejecutar

```bash
python main.py
```

---

## 🔑 Credenciales de prueba

Tarjeta:

```text
4532015112830366
```

PIN:

```text
1234
```

---

## 🛡️ Tecnologías y conceptos utilizados

* Python
* Programación Orientada a Objetos (POO)
* Clases y métodos
* Funciones
* Hash SHA-256
* Algoritmo de Luhn
* Manejo de excepciones
* Logging
* Estructuras de datos (listas)

---

## 📚 Objetivos de aprendizaje

Este proyecto fue desarrollado con fines académicos para practicar:

* Diseño modular de aplicaciones.
* Seguridad básica en sistemas bancarios.
* Manejo de errores.
* Programación orientada a objetos.
* Registro y auditoría de eventos.

---

## 🔮 Posibles mejoras futuras

* Persistencia de datos mediante archivos JSON.
* Integración con PostgreSQL.
* Múltiples usuarios y cuentas.
* Interfaz gráfica.
* Registro de fechas para control real de retiros diarios.
* Sistema avanzado de detección de fraude.

---

## 👨‍💻 Autor

Tania Pastor Gaspar
