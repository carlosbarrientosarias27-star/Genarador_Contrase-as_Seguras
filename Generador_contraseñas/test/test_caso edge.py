import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# 1. Calculamos la raíz del proyecto (subiendo dos niveles desde la carpeta test)
# De: .../Generador_contraseñas/test/test_caso_edge.py
# A: .../Generador_contraseñas/
ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# 2. Insertamos la ruta al principio para que Python encuentre 'main' y 'src'
if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

# 3. Ahora las importaciones funcionarán en cadena
from main import menu_principal

class TestMainPasswordGenerator(unittest.TestCase):

    @patch('main.limpiar_pantalla') # Evitamos que limpie la consola real
    @patch('main.generar_password')
    @patch('main.evaluar_fortaleza')
    @patch('main.guardar_en_archivo')
    @patch('builtins.input')
    def test_caso_longitud_minima(self, mock_input, mock_save, mock_fort, mock_gen, mock_clear):
        """
        Caso Edge: Longitud mínima (8).
        Simulación: Opción 1 -> Lon 8 -> Mayus s -> Nums s -> Syms s -> Ambig n -> Cantidad 1 -> Guardar n -> Salir 3
        """
        mock_input.side_effect = ['1', '8', 's', 's', 's', 'n', '1', 'n', '', '3']
        mock_gen.return_value = "Abc1234!"
        mock_fort.return_value = "Fuerte"

        menu_principal()

        # Verificamos que se llamó a generar_password con longitud 8
        mock_gen.assert_called_with(8, True, True, True, False)

    @patch('main.limpiar_pantalla')
    @patch('main.generar_password')
    @patch('main.evaluar_fortaleza')
    @patch('builtins.input')
    def test_caso_sin_simbolos_y_numeros(self, mock_input, mock_fort, mock_gen, mock_clear):
        """
        Caso Edge: Solo letras (sin símbolos ni números).
        Simulación: Opción 1 -> Lon 16 -> Mayus s -> Nums n -> Syms n -> Ambig n -> Cantidad 1 -> Guardar n -> Salir 3
        """
        mock_input.side_effect = ['1', '16', 's', 'n', 'n', 'n', '1', 'n', '', '3']
        mock_gen.return_value = "SoloLetrasMayusYMin"
        
        menu_principal()

        # Verificamos que se llamó con nums=False y syms=False
        mock_gen.assert_called_with(16, True, False, False, False)

    @patch('main.limpiar_pantalla')
    @patch('main.generar_password')
    @patch('main.evaluar_fortaleza')
    @patch('builtins.input')
    def test_maxima_cantidad_contrasenas(self, mock_input, mock_fort, mock_gen, mock_clear):
        """
        Caso Edge: Límite máximo de generación (10).
        Simulación: Opción 1 -> Lon 16 -> Defaults -> Cantidad 10 -> Guardar n -> Salir 3
        """
        # Entradas: 1(menu), 16(lon), s, s, s, n, 10(cant), n(guardar), ''(enter), 3(salir)
        mock_input.side_effect = ['1', '16', 's', 's', 's', 'n', '10', 'n', '', '3']
        
        menu_principal()

        # Verificar que generar_password se ejecutó exactamente 10 veces
        self.assertEqual(mock_gen.call_count, 10)

    @patch('main.limpiar_pantalla')
    @patch('builtins.input')
    def test_validacion_rango_incorrecto(self, mock_input, mock_clear):
        """
        Caso Edge: Longitud fuera de rango (ej. 5) debe resetear a 16.
        """
        # Ingresamos 5 (inválido), debería tomar 16 por defecto según tu lógica en main.py
        mock_input.side_effect = ['1', '5', 's', 's', 's', 'n', '1', 'n', '', '3']
        
        with patch('main.generar_password') as mock_gen:
            menu_principal()
            # Comprobamos que aunque el usuario puso 5, el sistema usó 16
            mock_gen.assert_called_with(16, True, True, True, False)