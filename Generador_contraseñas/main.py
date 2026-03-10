import os
from src.generator import generar_password
from src.validator import evaluar_fortaleza
from src.storage import guardar_en_archivo
# IMPORTANTE: Importar desde tu nuevo archivo utils
from src.utils import limpiar_pantalla, pausar, validar_rango

def limpiar_pantalla():
    """Limpia la consola para mejorar la legibilidad[cite: 129, 132]."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    """
    Gestiona el bucle principal de la aplicación y la interfaz de usuario.
    
    Muestra el menú interactivo, captura las preferencias del usuario para 
    la generación de contraseñas y coordina el flujo entre los módulos 
    de generación, validación y almacenamiento.
    """
    while True:
        limpiar_pantalla()  # Usa la función de utils.py
        print("========================================")
        print("   GENERADOR DE CONTRASEÑAS SEGURAS    ") 
        print("========================================")
        print("1. Generar contraseñas")
        print("2. Ver historial (Próximamente)")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "3":
            print("¡Hasta luego!")
            break
        
        if opcion == "1":
            try:
                # Uso de validar_rango para simplificar la lógica
                lon_in = input("Longitud (8-128) [16]: ")
                lon = validar_rango(lon_in, 8, 128, 16)
                
                mayus = input("¿Incluir mayúsculas? (s/n) [s]: ").lower() != 'n'
                nums = input("¿Incluir números? (s/n) [s]: ").lower() != 'n'
                syms = input("¿Incluir símbolos? (s/n) [s]: ").lower() != 'n'
                ambig = input("¿Excluir ambiguos (0,O,1,l)? (s/n) [n]: ").lower() == 's'
                
                cant_in = input("¿Cuántas generar? (1-10) [1]: ")
                cantidad = validar_rango(cant_in, 1, 10, 1)
                
                resultados = []
                print("\nContraseñas generadas:")
                for i in range(1, cantidad + 1):
                    pw = generar_password(lon, mayus, nums, syms, ambig)
                    fort = evaluar_fortaleza(pw)
                    resultados.append((pw, fort))
                    print(f"{i}. {pw} -> [{fort}]") 

                if input("\n¿Guardar en archivo? (s/n): ").lower() == 's':
                    guardar_en_archivo(resultados)
                
                pausar()  # Usa la función de utils.py
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
                pausar()

if __name__ == "__main__":
    menu_principal()