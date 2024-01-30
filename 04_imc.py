import math

def clasificar_imc(imc):
    """
    Clasifica el IMC según los criterios de la OMS.
    """
    if imc < 18.5:
        return "Bajo Peso"
    elif 18.5 <= imc < 25:
        return "Adecuado"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado I"
    elif 35 <= imc < 40:
        return "Obesidad Grado II"
    else:
        return "Obesidad Grado III"
    

W = float(input("Ingrese su peso en Kg: \n"))
H = float(input("Ingrese su altura en Centímetros: \n"))
IMC = W / ((H/100) **2)

print("su IMC es : ", round(IMC,2) )
print("Según la OMS, su clasificación de IMC es:", clasificar_imc(IMC))
