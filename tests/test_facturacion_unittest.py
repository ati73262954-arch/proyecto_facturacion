import unittest
from src.logica_negocio import calcular_descuento, validar_numero_positivo


class TestModuloFacturacion(unittest.TestCase):

    def test_descuento_vip_alto(self):
        """Escenario: Cliente VIP gasta más de S/500 (Debe recibir 15% de S/600 = S/90)"""
        resultado = calcular_descuento(600.0, "VIP")
        self.assertEqual(resultado, 90.0)

    def test_descuento_regular_bajo(self):
        """Escenario: Cliente Regular gasta S/100 (Debe recibir 3% de S/100 = S/3)"""
        resultado = calcular_descuento(100.0, "REGULAR")
        self.assertEqual(resultado, 3.0)

    def test_validador_monto_letras_falla(self):
        """Escenario: Cajero digita letras por error (Debe retornar False)"""
        self.assertFalse(validar_numero_positivo("cien_soles"))


if __name__ == "__main__":
    unittest.main()
