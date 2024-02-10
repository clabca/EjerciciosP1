'''
Se requiere la construcción de una aplicación interactiva primeros_auxilios.py 
que entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega en tiempo real.

'''
print("Bienvenido al primeros auxilios")
print("Comenzaremos evaluando la salud de una persona")
RespEstimulos = input("¿la persona responde a los estímulos ? (s/n) \n")
if(RespEstimulos.lower() != 's'):
    print("Evalúe el traslado de  la persona a un centro medico de urgencia")
else:
    print("La persona responde a los estímulos")
    print("Abra la via Aérea de la persona")
    Respira = input("¿la persona respira ? (s/n) \n")
    if(Respira.lower() == 's' ):
        print("Coloque a la persona en una posición que le permita una buena respiración")
    else:
        print("La persona no respira")
        print("Administre 5 ventilaciones y llame a la ambulancia")
        Ambulancia = 'n'
        while(Ambulancia == 'n'):
            SignosVida = input("¿la persona tiene signos de vida ? (s/n) \n")
            if( SignosVida.lower() == 's'):
                print("Reevaluar a la espera de la ambulancia")
            else:
                print("Administre compresiones torácicas hasta que llegue la ambulancia")
            Ambulancia = input("¿Llego la ambulancia ? (s/n) \n")
        print("Buen Trabajo, deja la persona en manos de los paramedicos")
print("Fin del programa")



