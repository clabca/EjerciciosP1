import sys
import random

def jugar_cachipun(opcion_usuario):
    opciones_validas = ["piedra", "papel", "tijera"]

    if opcion_usuario not in opciones_validas:
        print("Argumento inválido. Las opciones válidas son: piedra, papel, tijera")
        return

    opcion_computadora = random.choice(opciones_validas)

    print("Tu jugaste:", opcion_usuario.capitalize())
    print("Computador jugó:", opcion_computadora.capitalize())

    if opcion_usuario == opcion_computadora:
        print("Empate!")
    elif (opcion_usuario == "piedra" and opcion_computadora == "tijera") or \
         (opcion_usuario == "papel" and opcion_computadora == "piedra") or \
         (opcion_usuario == "tijera" and opcion_computadora == "papel"):
        print("Ganaste!!")
    else:
        print("Perdiste :(")

def main():
    if len(sys.argv) != 2:
        print("Uso: python cachipun.py [piedra|papel|tijera]")
        return

    opcion_usuario = sys.argv[1].lower()
    jugar_cachipun(opcion_usuario)

if __name__ == "__main__":
    main()

