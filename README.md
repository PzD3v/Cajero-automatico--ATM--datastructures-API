# 🏦 Cajero Automático (ATM) - API con Estructuras de Datos

Una API REST implementada en Flask que simula un **Cajero Automático** usando estructuras de datos personalizadas. El proyecto demuestra la aplicación práctica de clases y métodos en Python para gestionar operaciones bancarias seguras.

## 📋 Características

✅ **Gestión de Cuentas Bancarias** - Crear y administrar cuentas con PIN seguro  
✅ **Retiros de Dinero** - Con validación de PIN y verificación de saldo  
✅ **Depósitos** - Agregar fondos a la cuenta  
✅ **Consulta de Saldo** - Ver el saldo actual en tiempo real  
✅ **Seguridad** - Bloqueo de cuenta después de 3 intentos fallidos de PIN  
✅ **Manejo de Errores** - Respuestas JSON estructuradas con códigos de estado HTTP

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x** - Lenguaje principal
- **Flask** - Framework web
- **Flask-CORS** - Habilitación de CORS para solicitudes desde otros dominios
- **Estructuras de Datos Personalizadas** - Clase `BankAccount` en `datastructures.py`

---

## 📦 Instalación

### Requisitos previos
- Python 3.7+
- pip o pipenv

### Pasos

1. **Clonar el repositorio:**
```bash
git clone https://github.com/PzD3v/Cajero-automatico--ATM--datastructures-API.git
cd Cajero-automatico--ATM--datastructures-API
```

2. **Instalar dependencias:**
```bash
pipenv install
```

3. **Activar el entorno virtual:**
```bash
pipenv shell
```

4. **Ejecutar el servidor:**
```bash
python src/app.py
```

El servidor se iniciará en `http://0.0.0.0:3000`

---

## 🚀 Uso de la API

### Base URL
```
http://localhost:3000
```

### Endpoints

#### 1️⃣ **Obtener Sitemap (Listar todos los endpoints)**
```
GET /
```
**Respuesta:** Lista de todos los endpoints disponibles

---

#### 2️⃣ **Consultar Saldo**
```
GET /balance
```

**Respuesta (200 OK):**
```json
{
  "balance": 1000.00
}
```

---

#### 3️⃣ **Realizar Retiro**
```
POST /withdraw
```

**Request Body:**
```json
{
  "amount": 100.50,
  "pin": "12345"
}
```

**Respuestas:**

✅ **Retiro Exitoso (200):**
```json
{
  "msg": "Retiro exitoso. Saldo restante: 899.50"
}
```

❌ **PIN Incorrecto (401):**
```json
{
  "msg": "PIN incorrecto. Inténtalo de nuevo"
}
```

❌ **Fondos Insuficientes (400):**
```json
{
  "msg": "Saldo insuficiente para completar el retiro"
}
```

❌ **Cuenta Bloqueada (403):**
```json
{
  "msg": "SEGURIDAD: Cuenta bloqueada por exceso de intentos"
}
```

---

#### 4️⃣ **Realizar Depósito**
```
POST /deposit
```

**Request Body:**
```json
{
  "amount": 500.00
}
```

**Respuesta (200 OK):**
```json
{
  "msg": "Depósito con éxito. Nuevo saldo: 1500.00"
}
```

---

## 📂 Estructura del Proyecto

```
src/
├── app.py                 # API Flask con todos los endpoints
├── datastructures.py      # Clase BankAccount y lógica bancaria
├── utils.py              # Funciones auxiliares (APIException, sitemap)
└── requirements.txt      # Dependencias del proyecto
```

### Archivo Principal: `app.py`

Contiene:
- Inicialización de la aplicación Flask
- Configuración de CORS
- Definición de los 4 endpoints principales
- Manejo de errores y validación de datos
- Instancia de la cuenta bancaria (`my_account`)

---

## 🔐 Seguridad

- **Validación de PIN:** Verifica el PIN antes de permitir retiros
- **Bloqueo por Intentos Fallidos:** Después de 3 intentos fallidos, la cuenta se bloquea
- **Validación de Montos:** Solo permite cantidades mayores a cero
- **Manejo de Excepciones:** Conversión segura de tipos de datos
- **Códigos de Estado HTTP Apropiados:**
  - `200` - Éxito
  - `400` - Solicitud inválida
  - `401` - No autorizado (PIN incorrecto)
  - `403` - Acceso denegado (cuenta bloqueada)

---

## 🧪 Testing

Para ejecutar pruebas (si están disponibles):
```bash
pipenv run test
```

---

## 📝 Ejemplo de Uso Completo

```bash
# 1. Consultar saldo inicial
curl -X GET http://localhost:3000/balance

# 2. Realizar un depósito
curl -X POST http://localhost:3000/deposit \
  -H "Content-Type: application/json" \
  -d '{"amount": 500}'

# 3. Realizar un retiro
curl -X POST http://localhost:3000/withdraw \
  -H "Content-Type: application/json" \
  -d '{"amount": 100, "pin": "12345"}'

# 4. Consultar nuevo saldo
curl -X GET http://localhost:3000/balance
```

---

## 💡 Conceptos de Estructuras de Datos Aplicados

Este proyecto demuestra:
- **Encapsulamiento:** La clase `BankAccount` encapsula el saldo y la lógica de validación
- **Abstracción:** Los métodos ocultan la complejidad de las operaciones bancarias
- **Gestión de Estado:** Mantiene el estado de la cuenta (saldo, PIN, intentos fallidos)
- **Validación de Datos:** Implementa lógica para garantizar operaciones válidas

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios mayores, abre primero un issue para discutir los cambios propuestos.

---

## 📄 Licencia

Este proyecto está disponible bajo la licencia MIT.

---

## 👤 Autor

**PzD3v** - [GitHub Profile](https://github.com/PzD3v)

---

## 📞 Soporte

Si encuentras problemas, abre un [issue](https://github.com/PzD3v/Cajero-automatico--ATM--datastructures-API/issues) en el repositorio.
