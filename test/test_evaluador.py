import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.evaluador import evaluar_fortaleza


class TestEvaluarFortaleza(unittest.TestCase):

    # --- Contraseñas DÉBILES ---

    def test_password_muy_corta(self):
        """Menos de 8 caracteres → Débil"""
        self.assertEqual(evaluar_fortaleza("abc"), "Débil")

    def test_password_solo_minusculas_corta(self):
        """Solo minúsculas y longitud < 8 → Débil"""
        self.assertEqual(evaluar_fortaleza("pass"), "Débil")

    def test_password_solo_numeros(self):
        """Solo números, sin otros criterios → Débil"""
        self.assertEqual(evaluar_fortaleza("1234"), "Débil")

    # --- Contraseñas MEDIAS ---

    def test_password_minusculas_y_numeros(self):
        """Minúsculas + números + longitud >= 8 → Media"""
        self.assertEqual(evaluar_fortaleza("password1"), "Media")

    def test_password_mayusculas_y_minusculas(self):
        """Mayúsculas + minúsculas + longitud >= 8 → Media"""
        self.assertEqual(evaluar_fortaleza("Password"), "Media")

    def test_password_longitud_media_sin_simbolos(self):
        """Longitud >= 8, mayúsculas, minúsculas y números, sin símbolo → Media"""
        self.assertEqual(evaluar_fortaleza("Passw0rd"), "Media")

    # --- Contraseñas FUERTES ---

    def test_password_con_simbolo_y_numero(self):
        """Longitud >= 8, mayúsculas, minúsculas, número y símbolo → Fuerte"""
        self.assertEqual(evaluar_fortaleza("P4ssw0rd!"), "Fuerte")

    def test_password_fuerte_variante(self):
        """Otra combinación fuerte"""
        self.assertEqual(evaluar_fortaleza("Hello@1a"), "Fuerte")

    # --- Contraseñas MUY FUERTES ---

    def test_password_muy_fuerte(self):
        """Longitud >= 12 + mayúsculas + minúsculas + número + símbolo → Muy fuerte"""
        self.assertEqual(evaluar_fortaleza("P4ssw0rdSegur@!"), "Muy fuerte")

    def test_password_muy_larga_y_compleja(self):
        """Contraseña larga y con todos los criterios → Muy fuerte"""
        self.assertEqual(evaluar_fortaleza("MyStr0ng&SecurePass!"), "Muy fuerte")

    def test_password_exactamente_12_caracteres_completa(self):
        """Exactamente 12 caracteres con todos los criterios → Muy fuerte"""
        self.assertEqual(evaluar_fortaleza("Abcdef1@ghij"), "Muy fuerte")

    # --- Casos borde ---

    def test_password_vacia(self):
        """Contraseña vacía → Débil"""
        self.assertEqual(evaluar_fortaleza(""), "Débil")

    def test_password_solo_espacios(self):
        """Solo espacios → Débil (sin caracteres válidos)"""
        self.assertEqual(evaluar_fortaleza("        "), "Débil")

    def test_password_exactamente_8_caracteres(self):
        """Exactamente 8 caracteres con criterios básicos → Media"""
        self.assertEqual(evaluar_fortaleza("Abcde1fg"), "Media")

    def test_password_exactamente_12_caracteres_sin_simbolo(self):
        """12 caracteres sin símbolo → Fuerte"""
        self.assertEqual(evaluar_fortaleza("Abcdefgh1234"), "Fuerte")


if __name__ == "__main__":
    unittest.main(verbosity=2)