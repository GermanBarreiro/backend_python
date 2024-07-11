import random

def num_adivina():
    print('dame dos numeros aleatorios para que sean los rangos mio dame un maximo y otro minimo: ')
    maximo = int(input())
    minimo = int(input())
    num_aleatorio = random.randint(minimo, maximo) 
    
    prediccion = minimo - 1
    while num_aleatorio != prediccion:
        prediccion = int(input(f'dame un numero entre : {minimo} y {maximo}: '))

        if prediccion > maximo or prediccion < minimo:
            print('el numero no es valido')
        elif prediccion <= maximo and prediccion >= minimo:
            print('el numero es valido')
            print('que comienze el juego')
            if prediccion > num_aleatorio:
                print('el numero es mas bajo')
            elif prediccion < num_aleatorio:
                print('el numero es mas alto')
            else:
                print('acertaste')

num_adivina()