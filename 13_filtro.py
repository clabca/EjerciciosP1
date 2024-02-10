'''
La empresa tiene un contrato con una tienda de tecnología en la cual quieren implementar un filtrado por precio. Para ello se solicita generar el archivo filtro.py con la solución al problema. Dada una muestra de los productos que actualmente se encuentran disponibles en la tienda (un diccionario), se solicita implementar una función que permita entregar lo siguiente:
● Un diccionario con los productos que cumplen una cierta condición dado un umbral
● La función debe permitir mostrar los valores mayor que o menor que un umbral (siempre estrictos).
● Por defecto la función debe siempre mostrar los valores mayor que el umbral a menos que se indique lo contrario.
Para desarrollar la funcionalidad se le entrega a usted un diccionario de prueba para verificar sus resultados. precios = {'Notebook': 700000, 'Teclado': 25000, 'Mouse': 12000, 'Monitor': 250000, 'Escritorio': 135000, 'Tarjeta de Video': 1500000}


Se espera ejecutar el programa de la siguiente manera:
● Si se especifica un argumento, este debe ser el umbral y por defecto debe calcular los que son estrictamente mayores al umbral.
python filtro.py 30000
Los productos mayores al umbral son: Notebook, Monitor, Escritorio, Tarjeta de Video
● En caso de que se ingresen dos valores, el primero seguirá siendo el umbral, mientras el segundo podrá tomar los valores mayor o menor. Por ejemplo, el siguiente código calculará los que son estrictamente menores.
python filtro.py 30000 menor
Los productos menores al umbral son: Teclado, Mouse
En caso que otro elemento se utilice se debe devolver lo siguiente: python filtro.py 30000 otro
Lo sentimos, no es una operación válida
TIP: El método .join() podría ser de utilidad para este problema:
', '.join(['uno','dos','tres','cuatro']
Donde el string ', ' funcionará como el separador de los elementos de la lista dentro del método join. Es decir, el output será el siguiente:
uno, dos, tres, cuatro



'''


# filtro.py

def filtrar_productos(precios, umbral, comparacion="mayor"):
    """
    Filtra los productos del diccionario precios que cumplen cierta condición basada en un umbral.
    
    Argumentos:
    precios (dict): Un diccionario que contiene los productos como claves y sus precios como valores.
    umbral (int): El umbral para filtrar los productos.
    comparacion (str, opcional): La comparación a realizar, puede ser "mayor" o "menor". Por defecto, es "mayor".
    
    Retorna:
    dict: Un diccionario con los productos que cumplen la condición especificada.
    """
    productos_filtrados = {}
    
    for producto, precio in precios.items():
        if comparacion == "mayor" and precio > umbral:
            productos_filtrados[producto] = precio
        elif comparacion == "menor" and precio < umbral:
            productos_filtrados[producto] = precio
            
    return productos_filtrados

def main():
    import sys

    precios = {
        'Notebook': 700000,
        'Teclado': 25000,
        'Mouse': 12000,
        'Monitor': 250000,
        'Escritorio': 135000,
        'Tarjeta de Video': 1500000
    }

    if len(sys.argv) == 2:
        umbral = int(sys.argv[1])
        productos_filtrados = filtrar_productos(precios, umbral)
        print("Los productos mayores al umbral son:", ', '.join(productos_filtrados.keys()))
    elif len(sys.argv) == 3:
        umbral = int(sys.argv[1])
        comparacion = sys.argv[2].lower()
        if comparacion in ("mayor", "menor"):
            productos_filtrados = filtrar_productos(precios, umbral, comparacion)
            print(f"Los productos {comparacion}es al umbral son:", ', '.join(productos_filtrados.keys()))
        else:
            print("Lo sentimos, no es una operación válida")
    else:
        print("Número incorrecto de argumentos")

if __name__ == "__main__":
    main()
