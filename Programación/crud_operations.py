def show_menu():
    print("\n--- Menú ---")
    print("1. Crear usuario")
    print("2. Leer usuarios")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")

def get_user_input():
    id_usuario = int(input("Ingrese el ID del usuario: "))
    nombre = input("Ingrese el nombre del usuario: ")
    email = input("Ingrese el email del usuario: ")
    fecha_de_nacimiento = input("Ingrese la fecha de nacimiento del usuario (YYYY-MM-DD): ")
    id_genero_musical = int(input("Ingrese el ID del género musical: "))
    return (id_usuario, nombre, email, fecha_de_nacimiento, id_genero_musical)

def create_user(connection, user):
    # Implementación para crear un usuario en la base de datos
    pass

def read_users(connection):
    # Implementación para leer usuarios de la base de datos
    pass

def update_user(connection, user):
    # Implementación para actualizar un usuario en la base de datos
    pass

def delete_user(connection, user_id):
    # Implementación para eliminar un usuario de la base de datos
    pass

