'''

Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados,
los usuarios normales y los usuarios premium a los cuales se les cobrará una
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que
permita considerar el caso recién expuesto. Para ello modifica la fórmula de utilidades
en la cual se solicite mediante input() los parámetros de entrada precios de
suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT.
(3 Puntos)
'''

import math

P = float(input("Ingrese el precio de suscripción: \n"))
UN = float(input("Ingrese el numero de usuarios normales: \n"))
UP = float(input("Ingrese el numero de usuarios premium: \n"))
GT = float(input("Ingrese el gasto total: \n"))
UT = (P*UN + 1.5*P*UP) - GT
print("Las utilidades son :", UT)