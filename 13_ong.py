'''
Apoyo matemático. (4 Puntos)
Otra área en la que la empresa presta soporte es a las ONG. En un programa de ayuda escolar que tiene la esta ONG se está enseñando a programar algunas operaciones avanzadas a niños con alto potencial pero de escasos recursos. Se quiere enseñar dos operaciones conocidas como el factorial y la productoria y se requiere que usted prepare una script que implemente esto.
El factorial se define de la siguiente forma:
𝑛! = 𝑛 ∗ 𝑛−1 ∗ 𝑛 − 2 ∗ ...∗ 2 ∗ 1
En un ejemplo práctico, el factorial de 5 (5!) se calculará como:
5! = 5∗4∗3∗2∗1 = 120
Por otro lado la productoria se define como la multiplicación de elementos.
𝐴= [3,6,4,2,8] Π𝐴𝑖 = 3 ∗ 6 ∗ 4 ∗ 2 ∗ 8
Para resolver este programa se solicita lo siguiente:
● Crear un script llamado ong.py que contenga las siguientes funciones:
○ Una función que calcule el factorial.
○ Una función que calcule la productoria.
○ Una función que permita controlar los cálculos. Esta función se debe invocar de la siguiente manera:
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)


Se ingresarán un valor numérico como argumento con el nombre fact_i cuando se requiera calcular un factorial, y una lista como argumento prod_i cuando se requiera calcular una productoria. Cabe destacar que la función debe permitir ingresar estos argumentos en cualquier orden y en cualquier cantidad. El resultado de la función se debe imprimir en pantalla de la siguiente forma:
El factorial de 5 es 120 La productoria de [4, 6, 7, 4, 3] es 2016 El factorial de 6 es 720
NOTA: Esta función no será ejecutada desde el terminal sino que desde el mismo script utilizando diferentes combinaciones de requerimientos de factorial y productoria.
TIP: El operador in podría ser de utilidad acá ya que es capaz de detectar trozos de string. Por ejemplo:
'gato' in 'hay un gato acá'
True

'''

# ong.py

def factorial(n):
    """
    Calcula el factorial de un número entero n.
    
    Argumentos:
    n (int): El número entero para calcular su factorial.
    
    Retorna:
    int: El factorial de n.
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def productoria(lista):
    """
    Calcula la productoria de una lista de números.
    
    Argumentos:
    lista (list): Una lista de números.
    
    Retorna:
    int: La productoria de los elementos de la lista.
    """
    result = 1
    for num in lista:
        result *= num
    return result

def calcular(**kwargs):
    """
    Función que permite controlar los cálculos de factorial y productoria.
    
    Argumentos:
    kwargs (dict): Un diccionario con los argumentos de las operaciones a realizar.
    """
    for key, value in kwargs.items():
        if "fact" in key:
            print(f"El factorial de {value} es {factorial(value)}")
        elif "prod" in key:
            print(f"La productoria de {value} es {productoria(value)}")

if __name__ == "__main__":
    calcular(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)


