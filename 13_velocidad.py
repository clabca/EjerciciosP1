'''
Otra solución que se encuentra pendiente es la encargada por una empresa de flotas que debe medir mediante telemetría las velocidades de cada una de sus correas transportadoras. Una de sus políticas es distribuir su energía de manera eficiente, por lo que, para poder entregar energía a las correas más lentas, es necesario ralentizar las más rápidas, para asegurar una correcta distribución de la energía disponible. Para ello, se requiere levantar una alerta de la posición de las correas transportadoras que están por sobre el promedio.
● Para ello se pide determinar una funcionalidad que calcule el promedio de una lista de velocidades. El servidor donde se pretende instalar esta funcionalidad no cuenta con mucha capacidad por lo que se pide no depender de librerías externas.
● Listar las posiciones de todas las correas transportadoras que están sobre el promedio. ● Implementar la solución mediante una función en un archivo llamado velocidad.py.
Se entrega la siguiente lista con una muestra de velocidades para probar las funcionalidades.
velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]
La salida que se espera en este caso es la siguiente: python velocidad.py
[0, 2, 3, 6, 8, 9, 10, 13, 15, 17, 18, 19, 20, 22, 24, 29, 30, 31, 32, 34, 35, 36, 37, 41, 48, 52, 54, 56, 57, 58, 59]

'''



# velocidad.py

def calcular_promedio(velocidades):
    """
    Calcula el promedio de una lista de velocidades.
    
    Argumentos:
    velocidades (list): Una lista de velocidades.
    
    Retorna:
    float: El promedio de las velocidades.
    """
    return sum(velocidades) / len(velocidades)

def listar_correas_sobre_promedio(velocidades):
    """
    Lista las posiciones de las correas transportadoras que están sobre el promedio de velocidades.
    
    Argumentos:
    velocidades (list): Una lista de velocidades.
    
    Retorna:
    list: Una lista con las posiciones de las correas transportadoras que están sobre el promedio.
    """
    promedio = calcular_promedio(velocidades)
    return [i for i, v in enumerate(velocidades) if v > promedio]

def main():
    velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]
    posiciones_sobre_promedio = listar_correas_sobre_promedio(velocidad)
    print(posiciones_sobre_promedio)

if __name__ == "__main__":
    main()
