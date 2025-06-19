from src.functions.registrar import registrar
from src.functions.ver_historial import ver_historial
from src.functions.buscar import buscar
from src.functions.pagar import pagar

while True:
    print("\nBienvenido al Sistema de Gestión de Préstamos 🧾\n")
    print("1. Registrar préstamo")
    print("2. Ver historial")
    print("3. Buscar por nombre")
    print("4. Marcar como pagado")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar()
    elif opcion == '2':
        ver_historial()
    elif opcion == '3':
        buscar()
    elif opcion == '4':
        pagar()
    elif opcion == '5':
        print("Gracias por utilizar nuestros servicios.")
        break
    else:
        print("Intente de nuevo.\n")