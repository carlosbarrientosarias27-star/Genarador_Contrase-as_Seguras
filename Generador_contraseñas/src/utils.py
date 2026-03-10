import os

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo del usuario."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    """Detiene la ejecución y espera a que el usuario presione una tecla."""
    input("\nPresione Enter para volver al menú...")

def validar_rango(valor_input, minimo, maximo, defecto):
    """Valida que un valor de entrada sea un entero dentro de un rango específico.

    Args:
        valor_input (str): El texto ingresado por el usuario.
        minimo (int): El valor mínimo permitido.
        maximo (int): El valor máximo permitido.
        defecto (int): El valor a retornar si la validación falla o la entrada es vacía.

    Returns:
        int: El número validado o el valor por defecto.
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