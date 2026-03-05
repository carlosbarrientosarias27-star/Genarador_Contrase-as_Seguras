import os
import random
import string

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo detectado (Windows o POSIX)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_bienvenida():
    """Imprime en consola el banner visual de bienvenida del sistema."""
    print("=" * 40)
    print("      SISTEMA DE GESTIÓN DE PASSWORDS")
    print("=" * 40)

def generar_contrasena(longitud=12, usar_simbolos=True):
    """
    Genera una contraseña aleatoria basada en criterios específicos.

    Args:
        longitud (int): Cantidad de caracteres (mínimo 8).
        usar_simbolos (bool): Si debe incluir caracteres especiales.

    Returns:
        str: La contraseña generada.
    """
    if longitud < 8:
        longitud = 8  # Validación de longitud mínima
    
    caracteres = string.ascii_letters + string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    password = "".join(random.choice(caracteres) for _ in range(longitud))
    return password

def mostrar_menu():
    """
    Muestra las opciones del menú principal y captura la entrada del usuario.

    Returns:
        str: El carácter u opción seleccionada por el usuario.
    """
    print("\n1. Generar contraseña")
    print("2. Ver historial")
    print("3. Salir")
    return input("\nSeleccione una opción: ")

def main():
    """
    Controlador principal que gestiona el flujo de navegación de la aplicación.
    
    Mantiene un historial temporal de contraseñas generadas durante la sesión
    y permite la navegación entre la generación, el historial y la salida.
    """
    historial = []
    
    while True:
        limpiar_pantalla()
        mostrar_bienvenida()
        opcion = mostrar_menu()

        if opcion == "1":
            try:
                long = int(input("Longitud (mín. 8): ") or 12)
                simb = input("¿Incluir símbolos? (s/n): ").lower() != 'n'
                
                nueva_pass = generar_contrasena(long, simb)
                historial.append(nueva_pass)
                print(f"\nContraseña generada: {nueva_pass}")
                
            except ValueError:
                print("\nError: Por favor, ingrese un número válido para la longitud.")
            
        elif opcion == "2":
            print("\n--- Historial de Contraseñas ---")
            if not historial:
                print("No hay contraseñas en esta sesión.")
            else:
                for i, p in enumerate(historial, 1):
                    print(f"{i}. {p}")
        
        elif opcion == "3":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida.")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()