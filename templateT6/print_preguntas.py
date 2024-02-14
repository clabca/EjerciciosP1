import preguntas as p
'''
Crear un programa llamado print_preguntas.py, el cual permitirá mostrar en la app las preguntas de acuerdo a un formato: ● El programa debe contener la función print_pregunta() que tome como argumentos un enunciado y sus alternativas, y que les aplique formato.
● Esta función no debe retornar ningún objeto, sólo imprimir en pantalla.
● El formato a utilizar es imprimir el enunciado, seguido de un salto de línea.
● Luego cada alternativa irá acompañada una letra asociada, una por cada línea de la siguiente manera:
○ A. Alternativa 1
○ B. Alternativa 2
○ C. Alternativa 3
○ D. Alternativa 4
'''
def print_pregunta(enunciado, alternativas):
    # Imprimir enunciado y alternativas
    ###############################################################
    print(enunciado[0])  # Imprimir enunciado
    print()  # Salto de línea
    
    letras = ['A', 'B', 'C', 'D']
    for i, alternativa in enumerate(alternativas):
        print(f"{letras[i]}. {alternativa[0]}")  # Imprimir letra y alternativa

    
    
    
    
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    
    # Enunciado básico 1

    # A. alt_1
    # B. alt_2
    # C. alt_3
    # D. alt_4