from src.database.db import prestamos

def registrar():
    print("Registrar Préstamo")

    nombre_prestatario = input("Nombre del prestatario: ")

    # Validar monto principal
    while True:
        entrada_monto = input("Monto del préstamo: ")
        try:
            monto_principal = float(entrada_monto)
            if monto_principal <= 0:
                print("El monto debe ser mayor que cero.")
                continue
            break
        except ValueError:
            print("Ingresa un número válido para el monto.")

    # Validar tasa de interés
    while True:
        entrada_tasa = input("Tasa de interés anual (%) (ej. 5): ")
        try:
            tasa_interes = float(entrada_tasa)
            if tasa_interes < 0:
                print("La tasa no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Ingresa una tasa válida.")

    # Validar duración del préstamo
    while True:
        entrada_duracion = input("Duración del préstamo (en años): ")
        try:
            duracion_anios = float(entrada_duracion)
            if duracion_anios <= 0:
                print(" La duración debe ser mayor que cero.")
                continue
            break
        except ValueError:
            print("Ingresa un número válido para la duración.")

    fecha_prestamo = input("Fecha del préstamo (YYYY-MM-DD): ")

    # Cálculo del interés simple: 
    interes_generado = monto_principal * (tasa_interes / 100) * duracion_anios
    total_a_pagar = monto_principal + interes_generado

    prestamo = {
        'id': len(prestamos) + 1,
        'nombre': nombre_prestatario,
        'monto': monto_principal,
        'tasa': tasa_interes,
        'tiempo': duracion_anios,
        'interes': interes_generado,
        'total_a_pagar': total_a_pagar,
        'fecha': fecha_prestamo,
        'estado': 'pendiente'
    }

    prestamos.append(prestamo)
    print(f"Préstamo registrado con éxito. Total a pagar: {total_a_pagar:.2f}\n")
