def main_menu(): 
    while True:
        print("\nMenu de opciones:")
        print("1. Crear")
        print("2. Leer")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            print("Opción Crear seleccionada")
        elif choice == '2':
            print("Opción Leer seleccionada")
        elif choice == '3':
            print("Opción Actualizar seleccionada")
        elif choice == '4':
            print("Opción Eliminar seleccionada")
        elif choice == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, elija otra.")    
  
main_menu()

