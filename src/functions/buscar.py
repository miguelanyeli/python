from src.database.db import prestamos

def buscar():
    print("\n Buscar Préstamo 🔎")
    nombre = input("Nombre del prestatario: ")
    encontrados = False
    for p in prestamos:
        if p['nombre'].lower() == nombre.lower():
            print(f"ID: {p['id']} | Monto: {p['monto']} | Fecha: {p['fecha']} | Estado: {p['estado']}")
            encontrados = True
    if not encontrados:
        print("No se encontraron préstamos ❌\n")