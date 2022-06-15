
from função_segundo_grau import menu_functions
from time import sleep

def menu():
    ops = ('[1] - Função do Segundo Grau.',
    '[2] - Funções Exponenciais.',
    '[3] - Matrizes.',
    '[4] - Sair do Programa.')
    while True:
        print('Operações:'.center(30))
        for op in ops:
            print(op)
        print('-=-' * 10)
        try:
            ask = int(input('Digite uma Opção Válida: '))
        except ValueError:
            print('\033[31mERRO!\033[m')
            sleep(1)
        else:
            if ask not in [1, 2, 3, 4]:
                print('\033[31mOPÇÃO INVÁLIDA\033[m')
                sleep(1)
            else:
                if ask == 1:
                    menu_functions()
                    pass
                elif ask == 2:
                    pass
                elif ask == 3:
                    pass
                elif ask == 4:
                    print('Até Breve!')
                    break

def information():
    part = ('César Willian Pacheco',
            'Otávio Carneiro Nogueira',
            'Rodrigo Munch')
    print('-=-' * 10)
    print('RMC CALCULADORA'.center(30))
    print('-=-' * 10)
    sleep(.5)
    for n in part:
        print(n.center(30))
        sleep(.5)
    print('-=-' * 10)
    sleep(.5)