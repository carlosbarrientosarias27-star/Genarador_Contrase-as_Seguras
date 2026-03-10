import string

def evaluar_fortaleza(password):
    """Calcula el nivel de seguridad de una contraseña mediante criterios de complejidad.

    Evalúa la longitud y la diversidad de tipos de caracteres (mayúsculas, 
    minúsculas, números y símbolos).

    Args:
        password (str): La contraseña a evaluar.

    Returns:
        str: Etiqueta de fortaleza ('Débil', 'Media', 'Fuerte' o 'Muy fuerte').
    """
    puntuacion = 0
    longitud = len(password)

    # Criterios: longitud, presencia de tipos de caracteres [cite: 85]
    if longitud >= 12: puntuacion += 1
    if any(c in string.ascii_lowercase for c in password): puntuacion += 1
    if any(c in string.ascii_uppercase for c in password): puntuacion += 1
    if any(c in string.digits for c in password): puntuacion += 1
    if any(c in string.punctuation for c in password): puntuacion += 1

    # Devolver una puntuación: Débil / Media / Fuerte / Muy fuerte [cite: 86]
    if puntuacion <= 2: return "Débil"
    if puntuacion == 3: return "Media"
    if puntuacion == 4: return "Fuerte"
    return "Muy fuerte"