import os

import os

def limpiar_pantalla():
    """Limpia la consola para mejorar la legibilidad."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Muestra un mensaje y espera a que el usuario presione Enter."""
    input("\nPresione Enter para volver al menú...")

def validar_rango(valor_input, minimo, maximo, defecto):
    """
    Valida que una entrada sea un número entero y esté dentro de un rango.
    """
    try:
        if not valor_input:
            return defecto
        num = int(valor_input)
        if minimo <= num <= maximo:
            return num
        return defecto
    except ValueError:
        return defecto