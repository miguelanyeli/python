from src.database.db import prestamos

def ver_historial():
    print("\n📖 Historial de Préstamos")
    if not prestamos:
        print("No hay préstamos registrados 📭\n")
    else:
        for p in prestamos:
            print(f"ID: {p['id']} | Nombre: {p['nombre']} | Monto: {p['monto']} | Fecha: {p['fecha']} | Estado: {p['estado']}")
        print()
