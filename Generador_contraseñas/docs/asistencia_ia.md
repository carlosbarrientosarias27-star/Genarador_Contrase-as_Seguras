# Bitácora de Asistencia de IA - Generador de Contraseñas Seguras

Este documento registra la interacción con la IA para la creación y estructuración de este proyecto, detallando los prompts utilizados para cada módulo.

---

## 1. Estructura del Proyecto
**Prompt:** > "Genera una estructura de carpetas profesional para un proyecto de Python llamado 'GENARADOR_CONTRASE-AS_SEGURAS'. Debe incluir una carpeta `src` para el código fuente, `docs` para documentación, `test` para pruebas unitarias y archivos raíz como `README.md` y `requirements.txt`."

---

## 2. Módulo de Lógica Central (`src/core.py`)
**Prompt:** > "Crea una función en Python que genere contraseñas aleatorias permitiendo configurar la longitud y el uso de mayúsculas, minúsculas, números y caracteres especiales. Usa la librería `secrets` para asegurar que sea criptográficamente segura."

---

## 3. Módulo de Evaluación (`src/evaluador.py`)
**Prompt:** > "Escribe un evaluador de fortaleza de contraseñas. Debe recibir un string y retornar un puntaje basado en criterios como longitud, variedad de caracteres y si contiene patrones comunes."

---

## 4. Módulo de Almacenamiento (`src/almacenamiento.py`)
**Prompt:** > "Necesito una clase para manejar el guardado de contraseñas generadas en un archivo local (TXT o JSON). Incluye métodos para guardar con una etiqueta y para leer el historial, asegurándote de manejar errores de permisos de archivo."

---

## 5. Módulo de Validaciones (`src/validaciones.py`)
**Prompt:** > "Crea funciones de validación de entrada para el usuario. Por ejemplo, asegurar que la longitud de la contraseña sea un número entero positivo y que al menos un tipo de carácter esté seleccionado."

---

## 6. Punto de Entrada (`src/main.py`)
**Prompt:** > "Genera un script principal que orqueste los módulos anteriores. Debe presentar una interfaz de línea de comandos (CLI) interactiva que pregunte al usuario sus preferencias y muestre la contraseña generada y su nivel de seguridad."

---

## 7. Documentación y Requisitos
**Prompts:**
- "Genera un archivo `requirements.txt` básico para este proyecto."
- "Escribe un `README.md` con instrucciones de instalación y uso."