

preguntas_basicas = {
    'pregunta_1': {'enunciado': ['¿Cuál es la salida del siguiente código Python? (2 * 2) + 3 / 3 '],
                   'alternativas': [['4', 0], 
                                    ['5', 1], 
                                    ['6', 0], 
                                    ['7', 0]]},
    'pregunta_2': {'enunciado': ['¿Qué hace la función `len()` en Python?'],
                   'alternativas': [['Cuenta el número de caracteres en una cadena', 0], 
                                    ['Devuelve el número de elementos en un objeto iterable', 1], 
                                    ['Devuelve el valor máximo en una lista', 0], 
                                    ['Devuelve la longitud de un objeto', 0]]},
    'pregunta_3': {'enunciado': ['¿Cuál es el resultado de la siguiente expresión en Python? `3 * 3 ** 2`'],
                   'alternativas': [['27', 0], 
                                    ['18', 0], 
                                    ['81', 1], 
                                    ['9', 0]]}
}

preguntas_intermedias = {
    'pregunta_1': {'enunciado': ['¿Cuál es la diferencia entre una lista y una tupla en Python?'],
                   'alternativas': [['Una lista es mutable mientras que una tupla es inmutable', 1], 
                                    ['Una lista solo puede contener números mientras que una tupla puede contener cualquier tipo de dato', 0], 
                                    ['Una lista es más eficiente en términos de uso de memoria que una tupla', 0], 
                                    ['Una lista tiene un tamaño fijo mientras que una tupla puede crecer o reducirse dinámicamente', 0]]},
    'pregunta_2': {'enunciado': ['¿Qué hace la función `range()` en Python?'],
                   'alternativas': [['Genera una lista de números desde 0 hasta el número especificado', 0], 
                                    ['Genera un objeto iterable que produce una secuencia de números', 1], 
                                    ['Genera una lista de números desde el número especificado hasta 0', 0], 
                                    ['Genera un rango de números aleatorios', 0]]},
    'pregunta_3': {'enunciado': ['¿Cuál es el resultado de la siguiente expresión en Python? `10 / 3`'],
                   'alternativas': [['3.3333333333333335', 1], 
                                    ['3.0', 0], 
                                    ['3', 0], 
                                    ['3.333333333333333', 0]]}
}

preguntas_avanzadas = {
    'pregunta_1': {'enunciado': ['¿Qué es una comprensión de lista en Python?'],
                   'alternativas': [['Una estructura de control que permite iterar sobre elementos de una lista', 0], 
                                    ['Una forma concisa de crear listas en Python utilizando una expresión iterable', 1], 
                                    ['Una lista que contiene otras listas', 0], 
                                    ['Una lista que no contiene elementos duplicados', 0]]},
    'pregunta_2': {'enunciado': ['¿Cuál es la diferencia entre una clase y un objeto en Python?'],
                   'alternativas': [['Una clase es una instancia de un objeto', 0], 
                                    ['Una clase es un modelo para crear objetos', 1], 
                                    ['Un objeto es una instancia de una clase', 0], 
                                    ['Un objeto es una representación de una clase', 0]]},
    'pregunta_3': {'enunciado': ['¿Cuál es el resultado de la siguiente expresión en Python? `sum(range(1, 101))`'],
                   'alternativas': [['5050', 1], 
                                    ['5000', 0], 
                                    ['505', 0], 
                                    ['100', 0]]}
}


pool_preguntas = {'basicas': preguntas_basicas,
                  'intermedias': preguntas_intermedias,
                  'avanzadas': preguntas_avanzadas}


