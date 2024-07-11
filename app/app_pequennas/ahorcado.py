def jugar():
    print("Esto es un juego para dos jugadores que consiste en adivinar una palabra.")
    print('Escoge una palabra para que la adivine tu compañero.')

    palabra = input("Introduce una palabra: ").lower()
    
    contador = sum(1 for letra in palabra if letra.isalpha())
    print(f"La palabra tiene {contador} letras.")
    
    errores = 0
    letras_adivinadas = set()
    resultado = ['_' for _ in palabra]

    while errores < 6:
        print(' '.join(resultado))
        print(f'Errores: {errores}/6')
        print('Escoge una letra:')
        letra_user = input().lower()

        if len(letra_user) != 1 or not letra_user.isalpha():
            print('Por favor, introduce una sola letra.')
            continue

        if letra_user in letras_adivinadas:
            print('Ya has intentado con esa letra. Prueba otra.')
            continue

        letras_adivinadas.add(letra_user)

        if letra_user in palabra:
            print('¡La letra se encuentra en la palabra!')
            for i, letra in enumerate(palabra):
                if letra == letra_user:
                    resultado[i] = letra_user
        else:
            errores += 1
            print('La letra no se encuentra en la palabra.')

        if '_' not in resultado:
            print('¡Felicidades! Has adivinado la palabra:', palabra)
            return

    print(f'¡Game Over! La palabra era: {palabra}')

jugar()