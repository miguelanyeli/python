from src.database.db import prestamos

def buscar():
    print("\nBuscar Préstamo 🔎")
    nombre = input("Nombre del prestatario: ")
    encontrados = False
    for p in prestamos:
        if p['nombre'].lower() == nombre.lower():
            print(
                f"ID: {p['id']} | Monto: {p['monto']:.2f} | Interés: {p['interes']:.2f} | "
                f"Total a pagar: {p['total_a_pagar']:.2f} | Fecha: {p['fecha']} | Estado: {p['estado']}"
            )
            encontrados = True
    if not encontrados:
        print("No se encontraron préstamos ❌\n")
