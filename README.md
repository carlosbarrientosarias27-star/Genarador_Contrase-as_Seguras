# 🔐 Generador de Contraseñas

Un generador de contraseñas seguro y configurable desarrollado en Python, con soporte para almacenamiento, validación y utilidades auxiliares.

---

# 📋 Descripción del Proyecto

**Generador de Contraseñas** es una aplicación Python modular que permite crear contraseñas seguras de forma personalizada. El proyecto está diseñado con buenas prácticas de software: separación de responsabilidades, cobertura de tests y documentación clara.

# 🎯 Objetivos

- Generar contraseñas aleatorias y seguras según criterios configurables por el usuario.
- Validar la fortaleza de contraseñas existentes.
- Almacenar contraseñas generadas de forma organizada.
- Proveer utilidades reutilizables que soporten la lógica principal.
- Mantener una arquitectura limpia, modular y fácilmente extensible.
- Garantizar la calidad del código mediante tests unitarios y de casos edge.

---

# 📁 Estructura del Proyecto

```
contraseña/                      # Archivos de contraseñas generadas
Generador_contraseñas/
├── docs/                        # Documentación adicional
├── src/                         # Código fuente principal
│   ├── __init__.py
│   ├── generator.py             # Lógica de generación de contraseñas
│   ├── storage.py               # Almacenamiento de contraseñas
│   ├── utils.py                 # Utilidades auxiliares
│   └── validator.py             # Validación de contraseñas
├── test/
│   └── src/                     # Tests unitarios
│       ├── __init__.py
│       ├── test_generator.py
│       ├── test_storage.py
│       ├── test_utils.py
│       ├── test_validator.py
│       ├── test_caso_edge.py    # Casos límite y edge cases
│       └── test_main.py
├── .gitignore
├── LICENSE
├── main.py                      # Punto de entrada de la aplicación
├── README.md
└── requirements.txt
```

---

# 🚀 Instalación

## Prerrequisitos

- Python 3.14


## Pasos

1. **Clona el repositorio:**

```bash
git clone https://github.com/tu-usuario/Generador_contraseñas.git
cd Generador_contraseñas
```

2. **Crea y activa un entorno virtual (recomendado):**

```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

3. **Instala las dependencias:**

```bash
pip install -r requirements.txt
```

---

# 🛠️ Uso

## Ejecutar la aplicación

```
python main.py
```

## Generar una contraseña desde código

```python
from src.generator import PasswordGenerator

# Instancia el generador
gen = PasswordGenerator()

# Genera una contraseña de 16 caracteres con mayúsculas, números y símbolos
password = gen.generate(
    length=16,
    uppercase=True,
    numbers=True,
    symbols=True
)

print(password)
# Ejemplo: "Xk3#mP9$qRv2@Lw8"
```

## Validar una contraseña

```python
from src.validator import PasswordValidator

validator = PasswordValidator()

result = validator.validate("MiContraseña123!")
print(result)
# Ejemplo: {'valid': True, 'strength': 'fuerte', 'score': 85}
```

## Guardar una contraseña

```python
from src.storage import PasswordStorage

storage = PasswordStorage()

storage.save(label="Gmail", password="Xk3#mP9$qRv2@Lw8")
passwords = storage.load_all()
print(passwords)
```

## Usar utilidades auxiliares

```python
from src.utils import entropy, has_repeating_chars

pwd = "MiContraseña@99"
print(entropy(pwd))              # Calcula la entropía de bits
print(has_repeating_chars(pwd))  # Detecta caracteres repetidos
```

---

# 🧪 Tests

El proyecto incluye tests unitarios y casos edge para todos los módulos.

## Ejecutar todos los tests

```
python -m pytest test/ -v
```

## Ejecutar tests de un módulo específico

```bash
python -m pytest test/src/test_generator.py -v
python -m pytest test/src/test_validator.py -v
python -m pytest test/src/test_storage.py -v
python -m pytest test/src/test_utils.py -v
```

### Ejecutar casos edge

```bash
python -m pytest test/src/test_caso_edge.py -v
```

## Ver cobertura de tests

```bash
pip install pytest-cov
python -m pytest test/ --cov=src --cov-report=term-missing
```

---

# ⚙️ Módulos

| Módulo | Descripción |
|---|---|
| `generator.py` | Generación de contraseñas configurables |
| `validator.py` | Evaluación de fortaleza y validación de contraseñas |
| `storage.py` | Guardado y recuperación de contraseñas |
| `utils.py` | Funciones auxiliares: entropía, caracteres repetidos, etc. |

---


# 📄 Licencia

Este proyecto está bajo los términos de la licencia incluida en el archivo [LICENSE](LICENSE).

---