import secrets
import string

def validar_entero(mensaje, minimo, maximo, defecto=None):
    """
    Solicita un número al usuario y valida que esté dentro de un rango específico.

    Args:
        mensaje (str): El prompt que se mostrará al usuario.
        minimo (int): El valor entero mínimo permitido.
        maximo (int): El valor entero máximo permitido.
        defecto (int, optional): Valor a retornar si la entrada está vacía.

    Returns:
        int: El número validado proporcionado por el usuario o el valor por defecto.
    """
    while True:
        sufijo = f" [Por defecto: {defecto}]" if defecto is not None else ""
        entrada = input(f"{mensaje}{sufijo}: ").strip()
        
        if not entrada and defecto is not None:
            return defecto
        
        try:
            valor = int(entrada)
            if minimo <= valor <= maximo:
                return valor
            print(f"❌ Error: El número debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("❌ Error: Por favor, introduce un número entero válido.")

def evaluar_fortaleza(password):
    """
    Determina la robustez cualitativa de la contraseña basándose en su extensión.

    Args:
        password (str): La cadena de texto a evaluar.

    Returns:
        str: Una etiqueta descriptiva con un indicador visual (Débil, Media o Fuerte).
    """
    longitud = len(password)
    if longitud < 10:
        return "Débil 🔴"
    elif longitud < 16:
        return "Media 🟡"
    else:
        return "Fuerte 🟢"

def generar_password(longitud=16):
    """
    Crea una cadena aleatoria criptográficamente segura.

    Args:
        longitud (int): El número de caracteres de la contraseña (por defecto 16).

    Returns:
        str: Contraseña compuesta por letras, números y símbolos.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # secrets es más seguro que el módulo random para contraseñas
    password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return password

def ejecutar_programa():
    """
    Ejecuta el flujo lógico del generador de contraseñas múltiples.
    
    Coordina la captura de parámetros, la generación masiva y la 
    presentación tabulada de resultados con su respectiva fortaleza.
    """
    print("--- 🔐 GENERADOR DE CONTRASEÑAS SEGURAS ---")
    
    # 1. Validar longitud (8 a 128, defecto 16)
    longitud = validar_entero("1. Introduce la longitud deseada", 8, 128, defecto=16)
    
    # 2. Validar cantidad de contraseñas (1 a 10)
    cantidad = validar_entero("2. ¿Cuántas contraseñas quieres generar?", 1, 10)
    
    print(f"\nResultados para {cantidad} contraseñas ({longitud} caracteres):")
    print("-" * 50)
    
    # 3. Generar y mostrar con formato
    for i in range(1, cantidad + 1):
        pwd = generar_password(longitud)
        fortaleza = evaluar_fortaleza(pwd)
        # El formato :<30 alinea el texto a la izquierda con un espacio de 30 caracteres
        print(f"{i:2}. {pwd:<30} | Fortaleza: {fortaleza}")
    
    print("-" * 50)

if __name__ == "__main__":
    ejecutar_programa()