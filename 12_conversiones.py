import sys

def convertir_pesos_chilenos(tasas, monto):
    soles = monto * tasas[0]
    pesos_argentinos = monto * tasas[1]
    dolares = monto * tasas[2]
    return soles, pesos_argentinos, dolares

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python conversiones.py <tasa_sol> <tasa_peso_argentino> <tasa_dolar> <monto_en_pesos_chilenos>")
    else:
        tasas_conversion = [float(arg) for arg in sys.argv[1:4]]
        monto_en_pesos_chilenos = float(sys.argv[4])

        soles, pesos_argentinos, dolares = convertir_pesos_chilenos(tasas_conversion, monto_en_pesos_chilenos)

        print(f"Los {monto_en_pesos_chilenos} pesos chilenos equivalen a:\n {soles} Soles \n {pesos_argentinos} Pesos Argentinos \n {dolares} Dólares")


