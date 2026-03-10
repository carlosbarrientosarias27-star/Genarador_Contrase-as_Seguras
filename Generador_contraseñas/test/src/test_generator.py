import sys
import os
import unittest
import string

# Sube dos niveles para llegar a la raíz 'Generador_contraseñas'
# Nivel 1: de 'src' a 'test'
# Nivel 2: de 'test' a la raíz
raiz_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, raiz_proyecto)

from src.generator import generar_password

class TestGeneradorPassword(unittest.TestCase):

    def test_longitud_correcta(self):
        """Verifica que la contraseña tenga el largo solicitado."""
        largo = 20
        pwd = generar_password(longitud=largo)
        self.assertEqual(len(pwd), largo)

    def test_solo_minusculas(self):
        """Verifica que si desactivamos todo, solo use minúsculas."""
        pwd = generar_password(usar_mayus=False, usar_nums=False, usar_syms=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in pwd))

    def test_excluir_ambiguos(self):
        """Verifica que no contenga caracteres como '0', 'O', 'I', 'l', '1'."""
        ambiguos = "0OI1l"
        # Generamos una contraseña larga para aumentar la probabilidad de detectar errores
        pwd = generar_password(longitud=100, excluir_ambiguos=True)
        for char in ambiguos:
            with self.subTest(char=char):
                self.assertNotIn(char, pwd)

    def test_incluye_numeros(self):
        """Verifica que incluya números cuando se solicita (prueba de probabilidad)."""
        # Nota: Al ser aleatorio, probamos con una longitud mayor
        pwd = generar_password(longitud=50, usar_nums=True, usar_mayus=False, usar_syms=False)
        tiene_numero = any(c.isdigit() for c in pwd)
        self.assertTrue(tiene_numero)

if __name__ == '__main__':
    unittest.main()