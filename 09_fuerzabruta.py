
'''
Actividad 3 - Fuerza bruta
¿Qué tan seguro es tu password? ¿Intentemos hackear un password? Mediante el siguiente 
desafío se busca utilizar un algoritmo muy sencillo, llamado fuerza bruta para determinar 
cuántos intentos son necesarios para encontrar combinaciones numéricas en minúscula.
Para ello se ingresará un password oculto. Este password puede contener sólo 
combinaciones de letras y se requiere determinar su seguridad. Un mayor número de intentos 
implica un password más seguro:
El programa fuerza_bruta.py debe intentar todas las combinaciones de letras posibles, en 
orden alfabético, hasta que la combinación de letras sea igual a la de la contraseña indicada. 
Deberá hacer este proceso letra por letra, de izquierda a derecha.
Consideraciones
● Utilizar from string import ascii_lowercase
○ ascii_lowercase es un string con todas las letras del abecedario en 
minúsculas (sin la ñ). 
● No considerar la ñ.
● Considera mayúsculas y minúsculas como una misma letra.
● Se considera "intento" cada vez que se compara una letra.
Ejemplo:
○ Usuario ingresa "abc"
○ El computador compara:
■ a es igual a a => Sí (1 intento), continúa con la siguiente letra.
■ b es igual a a => No (2 intentos), prueba otra comparación.
■ b es igual a b => Sí (3 intentos), continúa con la siguiente letra.
■ c es igual a a => No (4 intentos), prueba con otra comparación.
■ c es igual a b => No (5 intentos), prueba con otra comparación.
■ c es igual a c => Sí (6 intentos), continúa con la siguiente letra.
■ No hay más letras. Se adivinó la palabra en 6 intentos.
NOTA: A modo explicativo se mostrará la contraseña a buscar pero la idea es que ésta se 
ingrese de manera oculta.

python fuerza_bruta.py 
Ingrese la contraseña: gato
La contraseña fue forzada en 43 intentos


Determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en 
minúscula. El programa fuerza_bruta.py debe intentar todas las combinaciones de letras 
posibles, en orden alfabético, hasta que la combinación de letras sea igual a la de la 
contraseña indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha.



'''
from string import ascii_lowercase  # Importamos el abecedario en minúsculas

def fuerza_bruta(password):
    intentos = 0  # Inicializamos el contador de intentos
    for longitud in range(1, len(password) + 1):  # Recorremos todas las longitudes posibles de combinaciones
        for combinacion in generar_combinaciones(longitud):  # Generamos todas las combinaciones de la longitud actual
            intentos += 1  # Incrementamos el contador de intentos en cada iteración
            if combinacion == password:  # Si la combinación actual es igual a la contraseña
                return intentos  # Devolvemos el número de intentos

def generar_combinaciones(longitud):
    for letra in ascii_lowercase:  # Iteramos sobre cada letra en minúsculas
        if longitud == 1:  # Si la longitud es 1, solo retornamos la letra
            yield letra
        else:  # Si la longitud es mayor a 1, generamos combinaciones recursivamente
            for combinacion in generar_combinaciones(longitud - 1):
                yield letra + combinacion  # Concatenamos la letra actual con las combinaciones anteriores

if __name__ == "__main__":
    contraseña = input("Ingrese la contraseña: ").lower()  # Solicitamos la contraseña al usuario y la convertimos a minúsculas
    intentos = fuerza_bruta(contraseña)  # Llamamos a la función fuerza_bruta para obtener el número de intentos
    print(f"La contraseña fue forzada en {intentos} intentos")  # Imprimimos el resultado

