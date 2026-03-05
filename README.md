# 🔐 Generador de Contraseñas Seguras

Un generador de contraseñas seguras desarrollado en Python, con evaluación de fortaleza, almacenamiento persistente y validaciones integradas.

---

## 📋 Descripción

Este proyecto proporciona una herramienta completa para la **generación, evaluación y almacenamiento de contraseñas seguras**. Está diseñado con una arquitectura modular que separa claramente las responsabilidades: generación de contraseñas, evaluación de su fortaleza, almacenamiento y validación de entradas.

---

## 🎯 Objetivos

- **Generar contraseñas seguras** con criterios configurables (longitud, caracteres especiales, mayúsculas, números, etc.)
- **Evaluar la fortaleza** de contraseñas existentes o generadas mediante métricas definidas
- **Almacenar contraseñas** de forma organizada y recuperable entre sesiones
- **Validar entradas del usuario** para garantizar parámetros correctos antes de procesar
- **Ofrecer una interfaz clara** desde línea de comandos para uso inmediato

---

## 🗂️ Estructura del Proyecto

```
GENERADOR_CONTRASE-AS_S.../
│
├── .qodo/
│
├── docs/
│   ├── asistencia_ia.md
│   └── caso edge.md
│
├── src/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── almacenamiento.py
│   ├── core.py
│   ├── evaluador.py
│   ├── main.py
│   └── validaciones.py
│
├── test/
│   ├── __init__.py
│   ├── test_almacenamiento.py
│   ├── test_caso edge.py
│   ├── test_core.py
│   ├── test_evaluador.py
│   ├── test_main.py
│   └── test_validaciones.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🚀 Instalación

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd GENARADOR_CONTRASE-AS_S

# Instalar dependencias
pip install -r requirements.txt
```

---

## 💻 Instrucciones de Uso
El punto de entrada principal del proyecto es main.py. Puedes ejecutarlo directamente desde la raíz:

Bash
python src/main.py

## Ejemplo de uso rápido:
Si deseas integrar la lógica en tu propio script, puedes importar los módulos de src:

Python
from src.core import generar_password
from src.evaluador import evaluar_seguridad

## Generar una contraseña de 16 caracteres
password = generar_password(longitud=16)
print(f"Contraseña generada: {password}")

## Evaluar su fortaleza
resultado = evaluar_seguridad(password)
print(f"Nivel de seguridad: {resultado}")

## 🧪 Pruebas (Testing)

El proyecto cuenta con una suite completa de pruebas unitarias localizadas en la carpeta test/. Para ejecutarlas, asegúrate de tener pytest instalado y corre:

Bash
pytest test/
Esto ejecutará todas las validaciones para el core, el almacenamiento y los casos borde definidos en test_caso_edge.py.

---

## 🧩 Módulos Principales

| Módulo | Descripción |
|---|---|
| `core.py` | Algoritmos de generación de contraseñas |
| `evaluador.py` | Análisis y puntuación de fortaleza |
| `almacenamiento.py` | Guardado y recuperación de contraseñas |
| `validaciones.py` | Validación de parámetros de entrada |

---

## 🧪 Tests

```bash
python -m pytest test/
```

---

## 📄 Licencia

Este proyecto está bajo los términos descritos en el archivo [LICENSE](LICENSE).