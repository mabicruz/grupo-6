from db_connection import create_connection
from crud_operations import create_user, read_users, update_user, delete_user, show_menu, get_user_input

def main():
    connection = create_connection()

    if connection is not None:
        try:
            while True:
                show_menu()
                choice = input("Seleccione una opción: ")

                if choice == '1':
                    user = get_user_input()
                    create_user(connection, user)
                elif choice == '2':
                    read_users(connection)
                elif choice == '3':
                    user = get_user_input()
                    update_user(connection, user)
                elif choice == '4':
                    user_id = int(input("Ingrese el ID del usuario a eliminar: "))
                    delete_user(connection, user_id)
                elif choice == '5':
                    connection.close()
                    print("Conexión cerrada. ¡Adiós!")
                    break
                else:
                    print("Opción no válida, intente de nuevo.")

        except Exception as e:
            print(f"Error: {e}")
            connection.close()
            print("Conexión cerrada debido a un error.")

if __name__ == "__main__":
    main()

