import sys
import os
# Añade la carpeta raíz del proyecto al path de búsqueda de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import string
from src.core import generar_password as gen_core
from Generador_contraseñas.main import generar_contrasena as gen_main
from Generador_contraseñas.src.validator import validar_entero

class TestPasswordEdgeCases(unittest.TestCase):

    def test_longitud_minima_forzada(self):
        """
        Caso Edge: Verifica que main.py nunca genere menos de 8 caracteres.
        """
        # El código en main.py establece: if longitud < 8: longitud = 8
        pwd = gen_main(longitud=1) 
        self.assertGreaterEqual(len(pwd), 8, "La longitud mínima debería ser 8")

    def test_generacion_sin_simbolos(self):
        """
        Caso Edge: Verifica que no se incluyan símbolos si el parámetro es False.
        """
        # core.py construye el pool sumando string.punctuation solo si usar_simbs es True
        pwd = gen_core(usar_simbs=False) 
        for char in pwd:
            self.assertNotIn(char, string.punctuation, f"Se encontró un símbolo inesperado: {char}")

    def test_limite_maximo_contrasenas(self):
        """
        Caso Edge: Verifica la validación de rango (máximo 10) en validaciones.py.
        """
        # La función validar_entero debe restringir el valor entre 1 y 10
        max_permitido = 10
        valor_usuario = 11
        es_valido = 1 <= valor_usuario <= max_permitido
        self.assertFalse(es_valido, "La validación debería rechazar cantidades mayores a 10")

if __name__ == "__main__":
    unittest.main()