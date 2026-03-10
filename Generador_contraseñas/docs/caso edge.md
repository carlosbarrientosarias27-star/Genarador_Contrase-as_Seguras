# 🛠️ Casos de Prueba Edge (Edge Cases)

## 1. Longitud mínima ("a", "1234", " " )
La mayoría de los sistemas fallan aquí por no definir qué cuenta como "longitud".

- El Riesgo: Si el requisito es de 8 caracteres, ¿qué pasa si el usuario pone 8 espacios en blanco? Si no haces un trim() (quitar espacios), el sistema podría aceptarlo.

- La Prueba: Intenta registrar una contraseña con un solo carácter o exactamente uno menos del límite permitido (si el mínimo es 8, prueba con 7).

## 2. Sin símbolos ("Password123")
Este es un caso de "clase de caracteres". Evalúa si el sistema realmente obliga a la complejidad o si se puede engañar.

- El Riesgo: Muchos algoritmos de validación usan expresiones regulares (Regex) que pueden ser permisivas.

- La Prueba: Crea una contraseña larga y alfanumérica, pero sin un solo carácter especial (como !, @, #). Si el sistema la acepta a pesar de que la regla dice "requiere símbolos", hay un fallo en la lógica booleana del código.

## 3. Máximas contraseñas (Límites de almacenamiento)
Aquí pasamos de la validación de forma a la validación de capacidad y seguridad.

- El Límite de Longitud: ¿Qué pasa si envío una contraseña de 10,000 caracteres? Algunos hashes (como BCrypt) tienen un límite de entrada (72 caracteres en algunos casos). Si envías más, el resto se ignora, lo cual es un riesgo de seguridad.

- El Límite de Intentos: ¿Cuántas veces puedo intentar ingresar una contraseña antes de que el sistema me bloquee?La Prueba: Intentar un ataque de "fuerza bruta" controlado para ver si el sistema activa el rate limiting (limitación de tasa) o el bloqueo de cuenta después de $N$ intentos fallidos.