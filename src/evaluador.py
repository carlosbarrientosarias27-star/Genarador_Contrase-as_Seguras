import re

def evaluar_fortaleza(password):
    """
    Evalúa la seguridad de una contraseña basándose en criterios técnicos.
    Retorna: 'Débil', 'Media', 'Fuerte' o 'Muy fuerte'.
    """
    puntuacion = 0
    
    # 1. Criterio de Longitud
    if len(password) >= 8:
        puntuacion += 1
    if len(password) >= 12:
        puntuacion += 1

    # 2. Presencia de Mayúsculas
    if re.search(r'[A-Z]', password):
        puntuacion += 1

    # 3. Presencia de Minúsculas
    if re.search(r'[a-z]', password):
        puntuacion += 1

    # 4. Presencia de Números
    if re.search(r'\d', password):
        puntuacion += 1

    # 5. Presencia de Símbolos (caracteres especiales)
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        puntuacion += 1

    # Mapeo de puntuación a etiquetas
    if puntuacion <= 2:
        return "Débil"
    elif puntuacion <= 4:
        return "Media"
    elif puntuacion == 5:
        return "Fuerte"
    else:
        return "Muy fuerte"

# Ejemplo de integración rápida
if __name__ == "__main__":
    test_pass = "P4ssw0rd!"
    resultado = evaluar_fortaleza(test_pass)
    print(f"Contraseña: {test_pass} | Evaluación: {resultado}")