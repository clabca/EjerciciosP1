'''
Crear un programa llamado shuffle.py que contenga la función shuffle_alt().
● Esta función debe tomar como argumento una pregunta desde el archivo preguntas.py (con un nivel y una pregunta definida) y mezclar las alternativas.
● La función debe retornar las alternativas mezcladas.
Tip: Recordar la función random.shuffle() de la librería random.

'''



import preguntas as p
import random

def shuffle_alt(pregunta):
    #mezclar alternativas
    #######################################################################
    alternativas = pregunta['alternativas']
    random.shuffle(alternativas)
    
    
    
    #######################################################################
    
    return alternativas



'''
if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]
'''




if __name__ == '__main__':


    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    # print(shuffle_alt(p.pool_preguntas['basicas']['pregunta_1'])) 
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]


    pregunta_ejemplo = p.pool_preguntas['basicas']['pregunta_1']
    print("Alternativas antes de mezclar:")
    print(pregunta_ejemplo['alternativas'])
    print("Alternativas después de mezclar:")
    print(shuffle_alt(pregunta_ejemplo))
