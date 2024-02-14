import preguntas as p
import random
from shuffle import shuffle_alt


'''
Crear un programa llamado question.py que permita escoger una pregunta que no se haya hecho durante la ejecución del programa dependiendo del nivel de dificultad. ● Cree una función llamada choose_q() que tome como único argumento la dificultad de la pregunta. ● La función debe tomar las preguntas del archivo preguntas.py de acuerdo a la dificultad escogida.
● La función debe escoger una pregunta de las opciones disponibles y eliminar dicha opción para no volverla a escoger.
● La función debe retornar dos elementos separados, el primero debe ser el enunciado escogido y el segundo las alternativas mezcladas de acuerdo a la tarea anterior.



'''
# Opciones dadas para escoger.
###############################################
opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################
import random
preguntas_seleccionadas = set()  # Conjunto para mantener registro de preguntas seleccionadas

def choose_q(dificultad):
    global preguntas_seleccionadas
    # Obtener las preguntas según la dificultad
    preguntas = p.pool_preguntas[dificultad]
    # Obtener una pregunta que no haya sido seleccionada previamente
    pregunta = random.choice(list(preguntas.keys()))
    while (dificultad+pregunta) in preguntas_seleccionadas:
        pregunta = random.choice(list(preguntas.keys()))
    
    # Agregar la pregunta al conjunto de preguntas seleccionadas
    preguntas_seleccionadas.add(dificultad+pregunta)
    
    # Obtener enunciado y alternativas de la pregunta seleccionada
    enunciado = preguntas[pregunta]['enunciado']
    alternativas = preguntas[pregunta]['alternativas']
    
    return enunciado, alternativas    



if __name__ == '__main__':
    # Ejemplo de uso de la función choose_q()
    dificultad_ejemplo = 'basicas'
    enunciado, alternativas = choose_q(dificultad_ejemplo)
    print("Enunciado:", enunciado)
    print("Alternativas:", alternativas)
