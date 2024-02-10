import sys

nombre = sys.argv[1]
apellido = sys.argv[2]
edad = sys.argv[3]

print(f"Mi nombre es {nombre}")
print(f"Mi apellido es {apellido}")
print(f"Mi edad es {edad}")
print(f"El nombre del archivo es {sys.argv[0]}")

print(type(sys.argv))

'''
ejecutar desde consola:
python 10_argumentos.py nombre apellido edad

Ejemplo:
python 10_argumentos.py Clara Ceballos 28

'''