

## preguntas_seleccionadas = set()  # Conjunto para mantener registro de preguntas seleccionadas

def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    # Verificar que p_level sea 1, 2 o 3
    if p_level not in [1, 2, 3]:
        raise ValueError("El número de preguntas por nivel debe ser 1, 2 o 3.")

    # Determinar el nivel basado en el número de pregunta y la cantidad de preguntas por nivel

    if p_level == 1:
        if n_pregunta == 1:
            level = 'basicas'
        elif n_pregunta == 2:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    elif p_level == 2:
        if n_pregunta <= 2:
            level = 'basicas'
        elif n_pregunta <= 4:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    elif p_level == 3:
        if n_pregunta <= 3:
            level = 'basicas'
        elif n_pregunta <= 6:
            level = 'intermedias'
        else:
            level = 'avanzadas'
    ##################################################
    return level



if __name__ == '__main__':
    # Verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias



    '''
    print() 
    print(choose_level(1, 1)) # básicas
    print(choose_level(2, 1)) # intermedias
    print(choose_level(3, 1)) # avanzadas
    print(choose_level(4, 1)) # avanzadas
    print() 
    print(choose_level(1, 2)) # básicas
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(4, 2)) # intermedias
    print(choose_level(5, 2)) # avanzadas
    print(choose_level(6, 2)) # avanzadas
    print() 
    print(choose_level(1, 3)) # básicas
    print(choose_level(2, 3)) # básicas
    print(choose_level(3, 3)) # básicas
    print(choose_level(4, 3)) # intermedias
    print(choose_level(5, 3)) # intermedias
    print(choose_level(6, 3)) # intermedias
    print(choose_level(7, 3)) # avanzadas
    print(choose_level(8, 3)) # avanzadas
    print(choose_level(9, 3)) # avanzadas
    print(choose_level(10, 3)) # avanzadas
    '''