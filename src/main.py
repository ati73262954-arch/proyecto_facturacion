import sys
from src.logica_negocio import validar_numero_positivo, procesar_factura


def ejecutar_interfaz_cajero():
    print("=== SISTEMA DE FACTURACIÓN COMERCIAL ===")
    monto_input = input("Ingrese el subtotal bruto de la compra (S/): ")

    if validar_numero_positivo(monto_input):
        subtotal_ingresado = float(monto_input)
        cliente_input = input("Ingrese tipo de cliente (VIP / REGULAR): ")

        factura = procesar_factura(subtotal_ingresado, cliente_input)

        print("\n--- RESUMEN DE COMPROBANTE DE VENTA ---")
        print(f"Subtotal Bruto : S/ {factura['subtotal_bruto']:.2f}")
        print(f"Descuento      : S/ {factura['descuento']:.2f}")
        print(f"Subtotal Neto  : S/ {factura['subtotal_neto']:.2f}")
        print(f"IGV (18%)      : S/ {factura['igv']:.2f}")
        print(f"TOTAL A PAYAR  : S/ {factura['total_pagar']:.2f}")

        sys.exit(0)
    else:
        print(
            "\n[ERROR CRÍTICO]: El monto ingresado debe ser un número decimal positivo.")
        sys.exit(1)


if __name__ == "__main__":
    ejecutar_interfaz_cajero()
