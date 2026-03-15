# 🔐 Generador de Contraseñas

Aplicación Python para generar, validar y almacenar contraseñas seguras, acompañada de un proyecto de prueba independiente para validar la lógica del generador.

---

# 📁 Estructura del Proyecto

```
Generador_contraseñas/
├── docs/
│   ├── asistencia_ia.md
│   └── caso edge.md
├── src/
│   ├── __init__.py
│   ├── generator.py        # Lógica de generación de contraseñas
│   ├── storage.py          # Almacenamiento de contraseñas
│   ├── utils.py            # Funciones auxiliares
│   └── validator.py        # Validación de contraseñas
├── test/
│   └── src/
│       ├── __init__.py
│       ├── test_generator.py
│       ├── test_storage.py
│       ├── test_utils.py
│       └── test_validator.py
│   ├── __init__.py
│   └── test_main.py
├── __init__.py
├── .gitignore
├── LICENSE
├── main.py                 # Punto de entrada principal
├── README.md
└── requirements.txt

Proyecto de Prueba/
├── __init__.py
├── generador.py            # Implementación simplificada del generador
└── Readme.md
```

---

# 🚀 Descripción

## Generador_contraseñas

Proyecto principal que implementa un generador de contraseñas seguras con las siguientes funcionalidades:

- **Generación** (`generator.py`): Crea contraseñas aleatorias con criterios configurables (longitud, caracteres especiales, mayúsculas, números, etc.).
- **Validación** (`validator.py`): Verifica que las contraseñas cumplan con los requisitos de seguridad definidos.
- **Almacenamiento** (`storage.py`): Gestiona el guardado y recuperación de contraseñas de forma segura.
- **Utilidades** (`utils.py`): Funciones de apoyo reutilizables en todo el proyecto.

## Proyecto de Prueba

Proyecto auxiliar e independiente que contiene una implementación simplificada del generador (`generador.py`) para pruebas rápidas o demostraciones.

---

# ⚙️ Requisitos

> Asegúrate de tener **Python 3.14** instalado.

---

# ▶️ Uso

## Ejecutar el proyecto principal

```
python main.py
```

## Ejecutar el generador de prueba

```
cd "Proyecto de Prueba"
python generador.py
```

---

# 🧪 Tests

Los tests se encuentran en la carpeta `test/` y cubren los módulos principales:

```
# Ejecutar todos los tests
python -m pytest test/

# Ejecutar un test específico
python -m pytest test/src/test_generator.py
```

| Archivo de test        | Módulo cubierto  |
|------------------------|------------------|
| `test_generator.py`    | `generator.py`   |
| `test_storage.py`      | `storage.py`     |
| `test_utils.py`        | `utils.py`       |
| `test_validator.py`    | `validator.py`   |
| `test_main.py`         | `main.py`        |

---

# 📄 Documentación

La carpeta `docs/` contiene documentación adicional del proyecto:

- `asistencia_ia.md` — Notas sobre el apoyo de IA en el desarrollo.
- `caso edge.md` — Casos límite identificados y su tratamiento.

---

# 📝 Licencia

Este proyecto está bajo la licencia especificada en el archivo [LICENSE](./LICENSE MIT).

---