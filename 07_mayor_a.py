ventas = { "Enero": 15000, "Febrero": 22000, "Marzo": 12000, "Abril": 17000, "Mayo": 81000, "Junio": 13000, "Julio": 21000, "Agosto": 41200, "Septiembre": 25000, "Octubre": 21500, "Noviembre": 91000, "Diciembre": 21000, }

'''
Actividad 1 - Filtrado compacto
Se solicita devolver un informe resumido que exponga 
los meses que superan un cierto umbral. 
El programa mayor_a.py debe retornar un diccionario 
con el mes y el valor asociado siempre y cuando superen el 
umbral especificado.

Ejemplo: 

python mayor_a.py 40000
{'Mayo': 81000, 'Agosto': 41200, 'Noviembre': 91000}
'''

import sys

# Definir el diccionario de ventas
ventas = { "Enero": 15000, "Febrero": 22000, "Marzo": 12000, "Abril": 17000, "Mayo": 81000, "Junio": 13000, "Julio": 21000, "Agosto": 41200, "Septiembre": 25000, "Octubre": 21500, "Noviembre": 91000, "Diciembre": 21000 }

# Función para filtrar los meses que superan un umbral dado
def filtrar_ventas(ventas, umbral):
    meses_superiores = {}
    for mes, venta in ventas.items():
        if venta > umbral:
            meses_superiores[mes] = venta
    return meses_superiores

if __name__ == "__main__":
    # Verificar que se proporciona un argumento de línea de comandos
    if len(sys.argv) != 2:
        print("Uso: python mayor_a.py <umbral>")
        sys.exit(1)

    # Obtener el umbral del argumento de línea de comandos
    umbral = int(sys.argv[1])

    # Filtrar las ventas
    resultados = filtrar_ventas(ventas, umbral)

    # Imprimir el resultado
    print(resultados)
