
from time import sleep
import numpy as np

def menu_functions_three():
    ops = ('[1] - Verificar Determinante',
    '[2] - Multiplicação de Matrizes',
    '[3] - Matriz Transposta',
    '[4] - Sair do Submenu')
    while True:
        print('-=-' * 10)
        print('MATRIZES'.center(30))
        print('-=-' * 10)
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
                print('\033[31mOpção Inválida\033[m')
                sleep(1)
            else:
                if ask == 1:
                    pass
                elif ask == 2:
                    pass
                elif ask == 3:
                    pass
                elif ask == 4:
                    print('-=-' * 10)
                    sleep(1)
                    break
