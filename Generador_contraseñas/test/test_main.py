import unittest
import string
import sys
import os

# Añade la carpeta raíz del proyecto al sistema de rutas de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ahora ya puedes importar
from Generador_contraseñas.main import generar_contrasena

class TestPasswordManager(unittest.TestCase):

    def test_longitud_minima(self):
        """Verifica que no se generen contraseñas de menos de 8 caracteres."""
        # Si pedimos 5, el código debería forzar el mínimo de 8
        resultado = generar_contrasena(longitud=5)
        self.assertGreaterEqual(len(resultado), 8)

    def test_longitud_personalizada(self):
        """Verifica que respete longitudes mayores al mínimo."""
        largo = 15
        resultado = generar_contrasena(longitud=largo)
        self.assertEqual(len(resultado), largo)

    def test_sin_simbolos(self):
        """Verifica que no incluya símbolos si se desactiva la opción."""
        resultado = generar_contrasena(usar_simbolos=False)
        # Comprobamos que ningún caracter sea de puntuación
        for char in resultado:
            self.assertNotIn(char, string.punctuation)

    def test_con_simbolos(self):
        """Verifica que la contraseña pueda contener símbolos (probabilidad)."""
        # Generamos una larga para asegurar que aparezcan símbolos
        resultado = generar_contrasena(longitud=50, usar_simbolos=True)
        tiene_simbolo = any(char in string.punctuation for char in resultado)
        self.assertTrue(tiene_simbolo, "La contraseña debería contener al menos un símbolo")

    def test_tipo_retorno(self):
        """Asegura que el resultado sea siempre una cadena de texto."""
        resultado = generar_contrasena()
        self.assertIsInstance(resultado, str)

if __name__ == '__main__':
    unittest.main()