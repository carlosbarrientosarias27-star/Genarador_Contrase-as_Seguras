import string
import secrets

def generar_password(longitud=12, usar_mayus=True, usar_nums=True, usar_simbs=True, excluir_confusos=False):
    # Definir los sets básicos
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    numeros = string.digits
    simbolos = string.punctuation
    
    # Construir el pool de caracteres dinámicamente
    caracteres = minusculas
    if usar_mayus:
        caracteres += mayusculas
    if usar_nums:
        caracteres += numeros
    if usar_simbs:
        caracteres += simbolos
        
    # Filtrar caracteres confusos: 0, O, l, I, 1
    if excluir_confusos:
        confusos = "0OlI1"
        caracteres = "".join(c for c in caracteres if c not in confusos)
    
    # Mostrar estadísticas del pool
    print(f"\n--- Info: Tienes {len(caracteres)} caracteres disponibles en el conjunto ---")
    
    # Generar la contraseña usando secrets para seguridad
    password = "".join(secrets.choice(caracteres) for _ in range(longitud))
    return password

def ejecutar_interfaz():
    print("--- Generador de Contraseñas Seguras ---")
    
    # Inputs del usuario
    while True:
        u_mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
        u_nums = input("¿Incluir números? (s/n): ").lower() == 's'
        u_simbs = input("¿Incluir símbolos? (s/n): ").lower() == 's'
        
        # Validación: Garantizar que al menos un tipo esté activado
        if not (u_mayus or u_nums or u_simbs):
            print("¡Error! Debes seleccionar al menos un tipo de carácter (mayúsculas, números o símbolos).")
            continue
        break
        n
    u_confusos = input("¿Excluir caracteres confusos (0, O, l, I, 1)? (s/n): ").lower() == 's'
    
    # Generación y salida
    password_final = generar_password(
        usar_mayus=u_mayus, 
        usar_nums=u_nums, 
        usar_simbs=u_simbs, 
        excluir_confusos=u_confusos
    )
    
    print(f"Tu contraseña generada es: {password_final}")
    print("-" * 40)

if __name__ == "__main__":
    ejecutar_interfaz()