import math

radio = float(input("Ingrese el radio en Kilómetros: \n"))
gravedad = float(input("Ingrese la constante g (m/s²): \n"))

print("La velocidad de Escape es ", round(math.sqrt(2*gravedad*radio*1000) ,2) ," m/s"  )
