from src.database.db import prestamos

def pagar():
    print("\nMarcar Préstamo como Pagado ")
    try:
        id_buscar = int(input("ID del préstamo: "))
    except ValueError:
        print("Ingresa un número válido.\n")
        return

    for p in prestamos:
        if p['id'] == id_buscar:
            if p['estado'] == 'pagado':
                print("Este préstamo ya está marcado como pagado ✅\n")
                return
            p['estado'] = 'pagado'
            print("Préstamo marcado como pagado ✅\n")
            return
    print("No se encontró ese ID ❌\n")
