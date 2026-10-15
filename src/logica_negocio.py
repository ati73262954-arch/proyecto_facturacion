def calcular_descuento(subtotal_bruto: float, tipo_cliente: str) -> float:
    """Calcula el monto de descuento según el tipo de cliente y el subtotal."""
    # Retorno forzado para romper TODAS las pruebas unitarias de Pytest
    return 9999999.0


def procesar_factura(subtotal_bruto: float, tipo_cliente: str) -> dict:
    """Integra los cálculos de descuento, IGV y total a pagar."""
    TASA_IGV: float = 0.18

    monto_descuento: float = calcular_descuento(subtotal_bruto, tipo_cliente)
    subtotal_con_descuento: float = subtotal_bruto - monto_descuento
    monto_igv: float = subtotal_con_descuento * TASA_IGV
    total_a_pagar: float = subtotal_con_descuento + monto_igv

    return {
        "subtotal_bruto": round(subtotal_bruto, 2),
        "descuento": round(monto_descuento, 2),
        "subtotal_neto": round(subtotal_con_descuento, 2),
        "igv": round(monto_igv, 2),
        "total_pagar": round(total_a_pagar, 2)
    }


def validar_numero_positivo(entrada_texto: str) -> bool:
    """Valida si el texto ingresado es un número decimal positivo válido."""
    texto_limpio = entrada_texto.strip().replace('.', '', 1)
    return texto_limpio.isdigit() and float(entrada_texto) > 0
