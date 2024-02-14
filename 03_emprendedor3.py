'''
Considera ahora una tercera versión llamada emprendedor3.py utilizando la fórmula
original de utilidades donde el usuario ingrese el precio de suscripción P, el número de
usuarios normales U y los gastos GT. Adicionalmente, solicita las utilidades del año
anterior Uanterior, todo esto mediante input(). El programa debe calcular las utilidades
actuales y mostrar la razón entre las utilidades actuales y las del año anterior con dos
decimales.
(2 Puntos)
'''

import math

P = float(input("Ingrese el precio de suscripción: \n"))
U = float(input("Ingrese el numero de usuarios: \n"))
GT = float(input("Ingrese el gasto total: \n"))
UTA = float(input("Ingrese las utilidades del año anterior: \n"))
UT = (P*U) - GT
print("Las utilidades de este año son :", UT)
print("Las utilidades del año pasado fueron :", UTA)
print("La razón de Utilidades de este año respecto del anterior  :", round(UT/UTA,2) )
