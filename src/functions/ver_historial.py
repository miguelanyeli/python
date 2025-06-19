from src.database.db import prestamos

def ver_historial():
    print("\nHistorial de Préstamos")
    if not prestamos:
        print("No hay préstamos registrados 📭\n")
    else:
        total_prestado = 0
        total_pendiente = 0

        for prestamo in prestamos:
            print(
                f"ID: {prestamo['id']} | Nombre: {prestamo['nombre']} | "
                f"Monto: {prestamo['monto']} | Fecha: {prestamo['fecha']} | "
                f"Estado: {prestamo['estado']}"
            )
            total_prestado += prestamo['monto']
            if prestamo['estado'] == 'pendiente':
                total_pendiente += prestamo['monto']

        print(f"\nTotal Prestado: {total_prestado}")
        print(f" Total Pendiente por Pagar: {total_pendiente}\n")


