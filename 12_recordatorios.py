recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

'''
Aplicando métodos apropiados para la estructura de datos entregada edite la lista de recordatorios de la siguiente manera:
NOTA: Los eventos deben siempre editarse de tal manera que mantengan su orden en el tiempo. Y el código debe ejecutarse en el orden entregado en las instrucciones dadas a continuación:
1. Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”. 2. Al revisar los eventos, nota un error, ya que el 15 de Julio no es feriado. Editar de tal manera que sea el 16 de Julio. 3. Lamentablemente le tocará trabajar el día del trabajo. Elimine el evento del día del trabajo. 4. Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
Al ejecutar el programa se espera el siguiente output: python recordatorios.py
[['2021-01-01', '11:00', 'Levantarse y ejercitar'], ['2021-01-02', '06:00', 'Empezar el año'], ['2021-07-16', '13:00', 'No hacer nada es feriado'], ['2021-09-18', '16:00', 'Ramadas'], ['2021-12-24', '22:00', 'Cena de Navidad'], ['2021-12-25', '00:00', 'Navidad'], ['2021-12-31', '22:00', 'Cena de Año Nuevo']]


'''
# Agregar evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”
recordatorios.append(['2021-02-02', '06:00', 'Empezar el año'])

# Editar evento del 15 de Julio a las 16:00 para el 16 de Julio
for evento in recordatorios:
    if evento[0] == '2021-07-15':
        evento[0] = '2021-07-16'

# Eliminar evento del día del trabajo
recordatorios = [evento for evento in recordatorios if evento[0] != '2021-05-01']

# Agregar cena de Navidad y de Año Nuevo a las 22 hrs.
recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

# Ordenar la lista de recordatorios por fecha y hora
recordatorios.sort()

# Output
print(*recordatorios, sep='\n')

