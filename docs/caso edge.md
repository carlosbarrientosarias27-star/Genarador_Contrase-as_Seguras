# 🛠️ Casos de Prueba Edge (Edge Cases)
Basado en la lógica de tus archivos, aquí tienes los escenarios críticos a validar:

## 1. Longitud Mínima y Validación de Rango
    
En main.py, la función generar_contrasena establece un piso de 8 caracteres, mientras que validaciones.py permite configurar un rango de 8 a 128.

Prueba: Intentar generar una contraseña de longitud 7 o menor.

Resultado esperado: El sistema debe elevar la longitud a 8 automáticamente o mostrar un error de validación en el ciclo while de validaciones.py.

## 2. Generación sin Símbolos ni Mayúsculas

El archivo core.py requiere que al menos un tipo de carácter esté activado.

Prueba: Seleccionar "n" (no) para mayúsculas, números y símbolos simultáneamente.

Resultado esperado: El programa debe detectar que el pool de caracteres está vacío, mostrar un mensaje de error y solicitar de nuevo los inputs sin romperse.

## 3. Cantidad Máxima de Contraseñas

El archivo validaciones.py limita la generación masiva a un máximo de 10 unidades.

Prueba: Introducir 11 en la pregunta "¿Cuántas contraseñas quieres generar?".

Resultado esperado: La función validar_entero debe rechazar el valor y repetir la pregunta hasta que se ingrese un número entre 1 y 10.