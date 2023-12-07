import random

# Tupla de opciones dentro del juego
options = ('piedra', 'papel', 'tijera')
rounds = 1
computer_wins = 0
user_wins = 0



while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    print('')
    
    print('computer_wins =>', computer_wins)
    print('user_wins =>', user_wins)
    print('')
    
    # Input del user
    user_option = input('piedra, papel o tijera => ').lower()
    
    rounds += 1
    # Validación sencilla de las opciones del user
    if not user_option in options:
        print('No es una opción válida...')
        continue
    
    # Aleatorización de la opción escogida por el computer
    computer_option = random.choice(options)
    
    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    print('')
    
    # Validaciones lógicas del juego
    if user_option == computer_option :
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'papel':
            print('Papel gana a piedra')
            print('El computador ganó!')
            computer_wins += 1
        else:
            print('Piedra gana a tijera')
            print('El user ganó!')
            user_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('El user ganó!')
            user_wins += 1
        else:
            print('Tijera gana a papel')
            print('El computador ganó!')
            computer_wins += 1
    elif user_option == 'tijera':
            if computer_option == 'piedra':
                print('Piedra gana a tijera')
                print('El computador ganó!')
                computer_wins += 1
            else:
                print('Tijera gana a papel')
                print('El user ganó!')
                user_wins += 1
    
    if computer_wins == 2:
        print('El ganador definitivo fue la computadora!!')
        break
    
    if user_wins == 2:
        print('El ganador definitivo fue el usuario!!')
        break

