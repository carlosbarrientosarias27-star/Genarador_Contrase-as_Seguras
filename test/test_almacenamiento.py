import unittest
from unittest.mock import patch, mock_open
import sys
import os

# Añade la carpeta raíz del proyecto al path de búsqueda de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.almacenamiento import guardar_contrasena_en_archivo

class TestAlmacenamiento(unittest.TestCase):

    @patch('builtins.input', return_value='s')
    @patch('builtins.open', new_callable=mock_open)
    def test_guardar_exitoso(self, mock_file, mock_input):
        """Prueba que la contraseña se guarde cuando el usuario dice 's'."""
        pass_test = "Password123"
        fortaleza_test = "Alta"
        
        guardar_contrasena_en_archivo(pass_test, fortaleza_test)

        # Verifica que el archivo se abrió en modo append ('a')
        mock_file.assert_called_once_with("contrasenas.txt", "a", encoding="utf-8")
        
        # Verifica que se escribió contenido que incluye la contraseña y la fortaleza
        handle = mock_file()
        args, _ = handle.write.call_args
        contenido_escrito = args[0]
        
        self.assertIn(pass_test, contenido_escrito)
        self.assertIn(fortaleza_test, contenido_escrito)

    @patch('builtins.input', return_value='n')
    @patch('builtins.open', new_callable=mock_open)
    def test_cancelar_guardado(self, mock_file, mock_input):
        """Prueba que NO se escriba nada si el usuario dice 'n'."""
        guardar_contrasena_en_archivo("pass", "Baja")
        
        # Verifica que el archivo nunca se llegó a abrir para escribir
        mock_file.assert_not_called()

if __name__ == '__main__':
    unittest.main()