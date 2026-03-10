import unittest
from unittest.mock import patch, mock_open
import os
import sys

# Ajuste de ruta para llegar a la raíz desde 'test/src/'
raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, raiz_proyecto)

from src.storage import guardar_en_archivo

class TestStorage(unittest.TestCase):

    @patch('os.makedirs')
    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_guardar_exitoso(self, mock_file, mock_exists, mock_makedirs):
        """Verifica que el archivo se abra en modo 'append' y se cree la carpeta."""
        # Configuración del mock
        mock_exists.return_value = False
        datos_prueba = [("P4ssw0rd!", "Alta"), ("12345", "Baja")]
        
        resultado = guardar_en_archivo(datos_prueba)
        
        # 1. Verificar que intentó crear la carpeta 'Contraseña'
        mock_makedirs.assert_called_with("Contraseña", exist_ok=True)
        
        # 2. Verificar que abrió el archivo correcto en modo 'a' (append)
        ruta_esperada = os.path.join("Contraseña", "Contraseñas.txt")
        mock_file.assert_called_with(ruta_esperada, "a", encoding="utf-8")
        
        # 3. Verificar que devolvió True
        self.assertTrue(resultado)

    @patch('builtins.open', side_effect=Exception("Error de permiso"))
    def test_manejo_errores(self, mock_file):
        """Verifica que la función maneje excepciones y devuelva False."""
        resultado = guardar_en_archivo([("test", "Media")])
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()