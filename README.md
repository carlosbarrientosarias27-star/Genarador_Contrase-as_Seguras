# 🔐 Generador de Contraseñas

Proyecto completo para la generación, validación y almacenamiento seguro de contraseñas, acompañado de un proyecto de prueba independiente para demostración rápida del generador.

---

# 📁 Estructura del Repositorio

```
├── Generador_contraseñas/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── generator.py       # Lógica principal de generación de contraseñas
│   │   ├── storage.py         # Almacenamiento y gestión de contraseñas
│   │   ├── utils.py           # Utilidades y funciones auxiliares
│   │   └── validator.py       # Validación de contraseñas
│   ├── test/
│   │   └── src/
│   │       ├── __init__.py
│   │       ├── test_generator.py
│   │       ├── test_storage.py
│   │       ├── test_utils.py
│   │       └── test_validator.py
│   │   ├── __init__.py
│   │   └── test_main.py
│   ├── docs/
│   ├── __init__.py
│   ├── .gitignore
│   ├── LICENSE
│   ├── main.py                # Punto de entrada principal
│   ├── README.md
│   └── requirements.txt
│
└── Proyecto de Prueba/
    ├── __init__.py
    ├── generador.py           # Ejemplo de uso del generador
    └── Readme.md
```

---

# 🚀 Módulos Principales — `Generador_contraseñas`

## `generator.py`
Núcleo del proyecto. Contiene la lógica para generar contraseñas aleatorias y seguras con parámetros configurables como longitud, uso de mayúsculas, números y caracteres especiales.

## `validator.py`
Valida que una contraseña cumpla con criterios de seguridad definidos (longitud mínima, complejidad, entropía, etc.).

## `storage.py`
Gestiona el guardado y recuperación de contraseñas generadas, pudiendo persistirlas de forma local o cifrada.

## `utils.py`
Funciones auxiliares reutilizables a lo largo del proyecto: formateo, logging, cálculo de entropía, entre otras.

## `main.py`
Punto de entrada para ejecutar el generador desde la línea de comandos.

---

# 🧪 Tests — `Generador_contraseñas/test`

El proyecto incluye una suite de pruebas unitarias organizada por módulo:

| Archivo              | Módulo probado    |
|----------------------|-------------------|
| `test_generator.py`  | `generator.py`    |
| `test_storage.py`    | `storage.py`      |
| `test_utils.py`      | `utils.py`        |
| `test_validator.py`  | `validator.py`    |
| `test_main.py`       | `main.py`         |

## Ejecutar los tests

```
# Desde la raíz del proyecto Generador_contraseñas
python -m pytest test/
```

---

# 🧩 Proyecto de Prueba

Carpeta independiente que sirve como demostración rápida y ejemplo de integración del generador de contraseñas.

## Archivos

- **`generador.py`** — Script de ejemplo que importa y utiliza el módulo principal para generar contraseñas de forma sencilla.
- **`__init__.py`** — Inicialización del módulo.
- **`Readme.md`** — Documentación específica del proyecto de prueba.

## Uso

```
cd "Proyecto de Prueba"
python generador.py
```

---

# ⚙️ Instalación

## Requisitos previos

- Python 3.14

## Pasos

```
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/generador-contraseñas.git
cd generador-contraseñas

---

# 💻 Uso básico

```
## Ejecutar el generador principal
cd Generador_contraseñas
python main.py

## Ejecutar el ejemplo del Proyecto de Prueba
cd "Proyecto de Prueba"
python generador.py
```

---

# 📄 License

Este proyecto está bajo la licencia especificada en el archivo [LICENSE](Generador_contraseñas/LICENSE MIT).

---
