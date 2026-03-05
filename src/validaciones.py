import secrets
import string

def validar_entero(mensaje, minimo, maximo, defecto=None):
    """
    Solicita un número al usuario y valida que esté en el rango permitido.
    Permite un valor por defecto si el usuario presiona Enter.
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
    Determina la robustez de la contraseña según su longitud.
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
    Crea una cadena aleatoria segura usando letras, números y símbolos.
    """
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # secrets es más seguro que el módulo random para contraseñas
    password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return password

def ejecutar_programa():
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