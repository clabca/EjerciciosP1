import requests

# Requerimiento 1: Obtener toda la información de los usuarios
response = requests.get("https://reqres.in/api/users")
if response.status_code // 100 == 2:  # Verificar si la solicitud fue exitosa
    users_data = response.json()["data"]
    print("Usuarios:")
    for user in users_data:
        print(user)
else:
    print("No se pudo obtener la información de los usuarios.")

# Requerimiento 2: Crear un usuario llamado Ignacio
new_user_data = {"name": "Ignacio", "job": "Profesor"}
response = requests.post("https://reqres.in/api/users", data=new_user_data)
if response.status_code // 100 == 2:
    created_user = response.json()
    print("Usuario creado:")
    print(created_user)
else:
    print("No se pudo crear el usuario.")

# Requerimiento 3: Actualizar un usuario llamado morpheus
user_to_update = None
for user in users_data:
    if user["first_name"] == "Emma":
        user_to_update = user
        print(f"Usuario llamado Emma encontrado: {user_to_update}")
        break

if user_to_update:
    user_id_to_update = user_to_update["id"]
    updated_user_data = {"residence": "zion"}
    update_url = f"https://reqres.in/api/users/{user_id_to_update}"
    response = requests.put(update_url, data=updated_user_data)
    if response.status_code // 100 == 2:
        updated_user = response.json()
        print("Usuario actualizado:")
        print(updated_user)
    else:
        print("No se pudo actualizar el usuario.")
else:
    print("No se encontró un usuario llamado Morpheus.")




# Requerimiento 4: Eliminar un usuario
# Encontrar el ID del usuario llamado Tracey
tracey_id = None
for user in users_data:
    if user["first_name"] == "Tracey":
        tracey_id = user["id"]
        print(f"ID del usuario llamado Tracey: {tracey_id}")
        break

if tracey_id is not None:
    # Eliminar el usuario Tracey
    delete_url = f"https://reqres.in/api/users/{tracey_id}"
    response = requests.delete(delete_url)
    print(f"Código de respuesta al eliminar el usuario Tracey: {response.status_code}")
else:
    print("No se encontró un usuario llamado Tracey.")



