from src.database.db import prestamos

def registrar():
    print("Registrar Préstamo")
    nombre = input("Nombre del prestatario: ")
    monto = float(input("Monto: "))
    fecha = input("Fecha (YYYY-MM-DD): ")

    prestamo = {
        'id': len(prestamos) + 1,
        'nombre': nombre,
        'monto': monto,
        'fecha': fecha,
        'estado': 'pendiente'
    }

    prestamos.append(prestamo)
    print("Préstamo registrado con éxito ✅\n")