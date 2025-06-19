from src.database.db import prestamos

def pagar():
    print("\n Marcar Préstamo como Pagado")
    try:
        id_buscar = int(input("ID del préstamo: "))
        for p in prestamos:
            if p['id'] == id_buscar:
                p['estado'] = 'pagado'
                print("Préstamo marcado como pagado ✅\n")
                return
        print("No se encontró ese ID ❌\n")
    except:
        print(" Ingresa un número válido.\n")