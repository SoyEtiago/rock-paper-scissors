import random

# Tupla de opciones dentro del juego
options = ('piedra', 'papel', 'tijera')

# Input del user
user_option = input('piedra, papel o tijera => ').lower()

# Validación sencilla de las opciones del user
if not user_option in options:
    print('Por favor, elige una opción válida...')
    exit()

# Aleatorización de la opción escogida por el computer
computer_option = random.choice(options)

print('User option =>', user_option)
print('Computer option =>', computer_option)

# Validaciones lógicas del juego
if user_option == computer_option :
    print('Empate')
elif user_option == 'piedra':
    if computer_option == 'papel':
        print('Papel gana a piedra')
        print('El computador ganó')
    else:
        print('Piedra gana a tijera')
        print('El user ganó!')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('Papel gana a piedra')
        print('El user ganó!')
    else:
        print('Tijera gana a papel')
        print('El computador ganó')
elif user_option == 'tijera':
        if computer_option == 'piedra':
            print('Piedra gana a tijera')
            print('El computador ganó')
        else:
            print('Tijera gana a papel')
            print('El user ganó!')

