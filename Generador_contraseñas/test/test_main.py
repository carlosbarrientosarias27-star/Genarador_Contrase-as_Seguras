import unittest
from unittest.mock import patch
import os
import sys

# Ajuste dinámico del path para importar 'main' desde la raíz
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

from main import menu_principal

class TestMain(unittest.TestCase):

    @patch('builtins.input')
    @patch('main.limpiar_pantalla')
    def test_menu_salir(self, mock_limpiar, mock_input):
        """Verifica que la opción '3' termine el programa correctamente."""
        # Simulamos que el usuario selecciona '3' inmediatamente
        mock_input.return_value = '3'
        
        with patch('builtins.print') as mock_print:
            menu_principal()
            # Verificamos que se imprimió el mensaje de despedida
            mock_print.assert_any_call("¡Hasta luego!")

    @patch('builtins.input')
    @patch('main.limpiar_pantalla')
    @patch('main.guardar_en_archivo')
    def test_flujo_generacion_completo(self, mock_guardar, mock_limpiar, mock_input):
        """Simula el flujo completo de generación sin guardar en archivo."""
        # Secuencia de entradas: 
        # 1 (Generar), 16 (Longitud), s (Mayus), s (Nums), s (Syms), n (Ambig), 
        # 1 (Cantidad), n (No guardar), '' (Pausa), 3 (Salir)
        mock_input.side_effect = ['1', '16', 's', 's', 's', 'n', '1', 'n', '', '3']
        
        menu_principal()
        
        # Verificamos que NO se llamó a la función de guardado
        mock_guardar.assert_not_called()

    @patch('builtins.input')
    @patch('main.limpiar_pantalla')
    def test_entrada_invalida_opcion(self, mock_limpiar, mock_input):
        """Verifica que el menú ignore opciones no válidas y permita salir."""
        # Seleccionamos una opción inexistente '9' y luego '3' para salir
        mock_input.side_effect = ['9', '3']
        
        menu_principal()
        # El test pasa si el bucle procesa la entrada inválida y luego sale con '3'

if __name__ == '__main__':
    unittest.main()