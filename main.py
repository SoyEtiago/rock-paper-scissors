user_option = input('piedra, papel o tijera => ').lower()
computer_option = 'papel' # Opción fija por el momento

# Validaciones
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

