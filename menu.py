
from função_segundo_grau import menu_functions_one
from função_exponencial import menu_functions_two
from função_matriz import menu_functions_three
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
                    menu_functions_one()
                    pass
                elif ask == 2:
                    menu_functions_two()
                elif ask == 3:
                    menu_functions_three()
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