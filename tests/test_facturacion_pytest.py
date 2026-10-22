from src.logica_negocio import calcular_descuento, validar_numero_positivo

# Pytest simplifica la lectura usando la palabra clave de Python 'assert'


def test_descuento_vip_bajo():
    # Cliente VIP gasta menos de S/500 -> 10% de S/200 = S/20
    assert calcular_descuento(200.0, "VIP") == 20.0


def test_descuento_regular_alto():
    # Cliente Regular gasta más de S/500 -> 8% de S/1000 = S/80
    assert calcular_descuento(1000.0, "REGULAR") == 80.0


def test_validador_monto_negativo_falla():
    # Un monto negativo no debe ser permitido por la regla del negocio
    assert validar_numero_positivo("-50.5") is False
