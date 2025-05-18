from device_manager import DeviceManager
from automation_manager import AutomationManager

device_manager = DeviceManager()
automation_manager = AutomationManager()

while True:
    print("\n--- SmartHome By Ryder ---")
    print("1. Agregar dispositivo")
    print("2. Listar dispositivos")
    print("3. Buscar dispositivo")
    print("4. Eliminar dispositivo")
    print("5. Configurar automatización")
    print("6. Ver automatizaciones")
    print("7. Salir")

# Aqui se muestra el menú de opciones al usuario

    opcion_usuario = input("Seleccione una opción: ")

    if opcion_usuario == "1":
        nombre_dispositivo = input("Nombre del dispositivo: ")
        tipo_dispositivo = input("Tipo de dispositivo: ")
        print(device_manager.agregar_dispositivo(nombre_dispositivo, tipo_dispositivo))

    elif opcion_usuario == "2":
        print(device_manager.listar_dispositivos())

    elif opcion_usuario == "3":
        nombre_dispositivo = input("Nombre del dispositivo a buscar: ")
        print(device_manager.buscar_dispositivo(nombre_dispositivo))

    elif opcion_usuario == "4":
        nombre_dispositivo = input("Nombre del dispositivo a eliminar: ")
        print(device_manager.eliminar_dispositivo(nombre_dispositivo))

    elif opcion_usuario == "5":
        condicion = input("Condición (ejemplo: 'cuando se hace de noche'): ")
        accion = input("Acción (ejemplo: 'encender luces'): ")
        print(automation_manager.configurar_automatizacion(condicion, accion))

    elif opcion_usuario == "6":
        print(automation_manager.obtener_automatizacion())

    elif opcion_usuario == "7":
        print("Saliendo del sistema...")
        break

    else:
        print("La opcion no es válida.")