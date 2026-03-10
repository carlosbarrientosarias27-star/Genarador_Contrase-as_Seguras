import unittest
from unittest.mock import patch
import os
import sys

# Ajuste de ruta para llegar a la raíz desde 'test/src/'
raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, raiz_proyecto)

from src.utils import validar_rango, limpiar_pantalla, pausar

class TestUtils(unittest.TestCase):

    # --- Pruebas de validar_rango ---
    def test_validar_rango_exitoso(self):
        """Verifica que un número dentro del rango sea aceptado."""
        self.assertEqual(validar_rango("10", 1, 20, 5), 10)

    def test_validar_rango_vacio(self):
        """Verifica que si la entrada es vacía, devuelva el valor por defecto."""
        self.assertEqual(validar_rango("", 1, 20, 5), 5)

    def test_validar_rango_fuera_de_limites(self):
        """Verifica que si el número excede el máximo, devuelva el defecto."""
        self.assertEqual(validar_rango("50", 1, 20, 5), 5)

    def test_validar_rango_no_numerico(self):
        """Verifica que si se ingresan letras, devuelva el defecto."""
        self.assertEqual(validar_rango("abc", 1, 20, 5), 5)

    # --- Pruebas de funciones de sistema ---
    @patch('os.system')
    def test_limpiar_pantalla(self, mock_system):
        """Verifica que se llame al comando correcto del sistema."""
        limpiar_pantalla()
        # Verifica que os.system fue llamado (cls en Windows, clear en Linux/Mac)
        self.assertTrue(mock_system.called)
        comando = mock_system.call_args[0][0]
        self.assertIn(comando, ['cls', 'clear'])

    @patch('builtins.input', return_value='')
    def test_pausar(self, mock_input):
        """Verifica que la función pausar llame a input."""
        pausar()
        mock_input.assert_called_once()

if __name__ == '__main__':
    unittest.main()