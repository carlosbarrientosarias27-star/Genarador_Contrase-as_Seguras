import sys
import os

# Añade la carpeta raíz del proyecto al path de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core import generar_password
import unittest
import string 

class TestGeneradorPassword(unittest.TestCase):

    def test_longitud_correcta(self):
        """Verifica que la contraseña tenga la longitud solicitada."""
        longitudes = [8, 12, 20, 32]
        for l in longitudes:
            pw = generar_password(longitud=l)
            self.assertEqual(len(pw), l)

    def test_excluir_confusos(self):
        """Verifica que no existan caracteres '0OlI1' si se activa la opción."""
        confusos = set("0OlI1")
        for _ in range(50): # Probamos varias veces por aleatoriedad
            pw = generar_password(excluir_confusos=True)
            self.assertTrue(all(c not in confusos for c in pw), f"Error: Se encontró un carácter confuso en {pw}")

    def test_solo_numeros(self):
        """Verifica que si solo pedimos números, solo devuelva números."""
        pw = generar_password(usar_mayus=False, usar_nums=True, usar_simbs=False)
        self.assertTrue(all(c in string.digits for c in pw))

    def test_sin_mayusculas(self):
        """Verifica que no haya mayúsculas si se deshabilitan."""
        pw = generar_password(usar_mayus=False)
        self.assertFalse(any(c.isupper() for c in pw))

    def test_pool_vacio_fallback(self):
        """
        Verifica el comportamiento cuando todo es False. 
        Nota: Tu función actual usa minúsculas por defecto, este test confirma eso.
        """
        pw = generar_password(usar_mayus=False, usar_nums=False, usar_simbs=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in pw))

if __name__ == "__main__":
    unittest.main()