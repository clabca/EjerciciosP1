def contar_caracteres_distintos(texto):
    caracteres_distintos = set(texto)
    return len(caracteres_distintos)

def contar_palabras_distintas(texto):
    palabras = texto.split()
    palabras_distintas = set(palabras)
    return len(palabras_distintas)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python word_count.py <nombre_archivo>")
    else:
        nombre_archivo = sys.argv[1]

        try:
            with open(nombre_archivo, "r", encoding="utf-8") as file:
                texto = file.read()

            caracteres_distintos = contar_caracteres_distintos(texto)
            palabras_distintas = contar_palabras_distintas(texto)

            print(f"El número de caracteres distintos es: {caracteres_distintos}")
            print(f"El número de palabras distintas es: {palabras_distintas}")

        except FileNotFoundError:
            print(f"Error: El archivo '{nombre_archivo}' no existe.")
        except Exception as e:
            print(f"Error: {e}")
