'''

Un emprendedor quiere crear una app que provea un servicio de entrega de comida para mascotas.
Este proyecto tiene buenos pronósticos, pero su éxito dependerá de cuántos usuarios pueda alcanzar.
La manera en la que se medirá esto es calculando las utilidades del proyecto. 
Estas utilidades se pueden calcular mediante la siguiente fórmula:

𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 ∗ 𝑈 − 𝐺𝑇
Donde:
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales
Para ello, se te pide desarrollar este cálculo en tres versiones.

Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente
para calcular las utilidades de un proyecto. Para ello utiliza input() 
para solicitar como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.
(5 Puntos)
'''

import math

P = float(input("Ingrese el precio de suscripción: \n"))
UN = float(input("Ingrese el numero de usuarios normales: \n"))
UP = float(input("Ingrese el numero de usuarios premium: \n"))
GT = float(input("Ingrese el gasto total: \n"))
UT = (P*UN + 1.5*P*UP) - GT
print("Las utilidades son :", UT)