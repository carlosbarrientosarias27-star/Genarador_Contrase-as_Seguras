# Registro de Asistencia de IA - Generador de Contraseñas
Este documento detalla la secuencia de prompts utilizados para la arquitectura y desarrollo del proyecto, facilitando la reproducibilidad y el entendimiento del flujo de trabajo.

## 1. Definición de Arquitectura y Estructura
Prompt:

"Genera una estructura de proyecto en Python para un generador de contraseñas robusto. La estructura debe separar la lógica de generación, el almacenamiento, la validación y las utilidades. Incluye una carpeta src, una carpeta test que replique la estructura de src, y una carpeta docs."

## 2. Desarrollo del Núcleo (src/)
Para la creación de los módulos principales, se utilizaron los siguientes comandos:

Módulo de Generación (generator.py):

"Crea un script en Python que genere contraseñas aleatorias permitiendo configurar longitud y el uso de mayúsculas, minúsculas, números y símbolos. Usa la librería secrets para seguridad criptográfica."

Módulo de Validación (validator.py):

"Escribe una función que evalúe la fortaleza de una contraseña basándose en longitud y diversidad de caracteres. Debe devolver un puntaje o un nivel (Bajo, Medio, Alto)."

Módulo de Almacenamiento (storage.py):

"Desarrolla una clase para gestionar el guardado de contraseñas de forma local (JSON o TXT), asegurando que el archivo se cree si no existe."

## 3. Implementación de Pruebas Unitarias (test/)
Prompt:

"Utilizando unittest o pytest, genera archivos de prueba para cada módulo en src/. Asegúrate de cubrir casos de borde (longitud cero, sin tipos de caracteres seleccionados) para test_generator.py y validaciones de fortaleza para test_validator.py."

## 4. Integración y Punto de Entrada (main.py)
Prompt:

"Crea el archivo main.py en la raíz del proyecto que sirva como interfaz de línea de comandos (CLI). Debe importar los módulos de src y permitir al usuario generar, validar y guardar una contraseña mediante un menú interactivo."

## 5. Documentación de Casos de Borde
Prompt:

"Ayúdame a redactar un documento caso edge.md que explique cómo el sistema maneja entradas inesperadas del usuario en la CLI y errores de permisos al escribir en el disco."