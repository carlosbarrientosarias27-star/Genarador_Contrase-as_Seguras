import unittest
from unittest.mock import patch
import os
import sys

# 1. Ajuste Dinámico del Path
# Buscamos la carpeta 'Generador_contraseñas' subiendo un nivel desde 'test/'
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

# 2. Importaciones correctas según tus archivos
from main import menu_principal  # En main.py el punto de entrada es menu_principal

class TestMain(unittest.TestCase):

    @patch('builtins.input')
    @patch('os.system') # Mock para limpiar_pantalla
    def test_menu_salir(self, mock_system, mock_input):
        """Verifica que la opción '3' termine el programa."""
        # Simulamos que el usuario escribe '3'
        mock_input.return_value = '3'
        
        with patch('builtins.print') as mock_print:
            menu_principal()
            # Verificamos que se despidió correctamente
            mock_print.assert_any_call("¡Hasta luego!")

    @patch('builtins.input')
    @patch('os.system')
    def test_flujo_incorrecto_manejo_error(self, mock_system, mock_input):
        """Verifica que el programa maneje errores de valor (ValueError)."""
        # 1. Elegir generar ('1')
        # 2. Meter letras ('error_aqui') -> Provoca ValueError
        # 3. Presionar Enter tras el mensaje de error ('')
        # 4. Salir ('3')
        mock_input.side_effect = ['1', 'error_aqui', '', '3']
        
        with patch('builtins.print') as mock_print:
            menu_principal()
            # CORRECCIÓN: Quitamos la 'b' de 'numbero' y añadimos la tilde
            mock_print.assert_any_call("Error: Por favor, ingrese un número entero.")

if __name__ == '__main__':
    unittest.main()