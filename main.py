
#César

from menu import menu
if __name__ == '__main__':
    names = ('César Willian Pacheco',
            'Otávio Nogueira',
            'Rodrigo Munch')
    print('-=-' * 10)
    print('Projeto Calculadora Massa'.center(30))
    print('-=-' * 10)
    print('Participantes'.center(30))
    for name in names:
        print(name.center(30))
    menu()
