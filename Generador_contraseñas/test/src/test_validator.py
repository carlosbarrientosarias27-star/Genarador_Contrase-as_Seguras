import unittest
import os
import sys

# Ajuste de ruta para llegar a la raíz desde 'test/src/'
raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, raiz_proyecto)

from src.validator import evaluar_fortaleza

class TestValidator(unittest.TestCase):

    def test_fortaleza_debil(self):
        """Contraseñas cortas o con pocos tipos de caracteres."""
        self.assertEqual(evaluar_fortaleza("abc"), "Débil")
        self.assertEqual(evaluar_fortaleza("123456"), "Débil")

    def test_fortaleza_media(self):
        """Contraseñas con 3 criterios cumplidos."""
        # Ejemplo: Minúsculas (1) + Mayúsculas (1) + Números (1) = 3
        self.assertEqual(evaluar_fortaleza("Ab1"), "Media")

    def test_fortaleza_fuerte(self):
        """Contraseñas con 4 criterios cumplidos."""
        # Ejemplo: Minúsculas + Mayúsculas + Números + Símbolos = 4
        self.assertEqual(evaluar_fortaleza("Ab1!"), "Fuerte")

    def test_fortaleza_muy_fuerte(self):
        """Contraseñas largas con variedad completa."""
        # Longitud >= 12 (1) + Minús (1) + Mayús (1) + Núms (1) + Syms (1) = 5
        self.assertEqual(evaluar_fortaleza("Password2026!"), "Muy fuerte")

    def test_longitud_influye(self):
        """Verifica que la longitud sume el punto extra necesario para 'Muy fuerte'."""
        # Caso: Todas las categorías pero longitud < 12 (Puntuación 4)
        self.assertEqual(evaluar_fortaleza("Ab1!"), "Fuerte")
        # Caso: Mismas categorías pero longitud >= 12 (Puntuación 5)
        self.assertEqual(evaluar_fortaleza("Ab1!longitud12"), "Muy fuerte")

if __name__ == '__main__':
    unittest.main()