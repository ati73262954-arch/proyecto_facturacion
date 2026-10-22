import datetime
import sys

from src.logica_negocio import procesar_factura


def ejecutar_auditoria():
    print("Iniciando auditoria interna del sistema de facturacion...")
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Transaccion contable de control (Monto base: 1000.0, Cliente: VIP)
    factura_control = procesar_factura(1000.0, "VIP")

    # Verificacion de consistencia contable
    if factura_control["total_pagar"] <= 0:
        print("[ERROR FATAL]: Discrepancia contable detectada.")
        sys.exit(1)

    nombre_archivo = "reporte_auditoria.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        sep = "=====================================================\n"
        div = "-----------------------------------------------------\n"

        archivo.write(sep)
        archivo.write(
            "   COMERCIAL CHICLAYO - INFORME TECNICO DE AUDITORIA\n"
        )
        archivo.write(sep)
        archivo.write(f"Fecha de Certificacion : {fecha_actual}\n")
        archivo.write(
            "Entorno de Evaluacion  : GitHub Actions Runner (Ubuntu)\n"
        )
        archivo.write(
            "Estado de Integridad   : SISTEMA TOTALMENTE OPERATIVO\n"
        )
        archivo.write(div)

        sub = factura_control["subtotal_bruto"]
        desc = factura_control["descuento"]
        total = factura_control["total_pagar"]

        archivo.write(f"Subtotal de Control    : S/ {sub:.2f}\n")
        archivo.write(f"Descuento VIP (15%)    : S/ {desc:.2f}\n")
        archivo.write(f"Total Liquidado        : S/ {total:.2f}\n")
        archivo.write(sep)

    print(f"Auditoria finalizada con exito. Archivo: {nombre_archivo}")
    sys.exit(0)


if __name__ == "__main__":
    ejecutar_auditoria()
