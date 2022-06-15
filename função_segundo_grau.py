

from cProfile import label
from time import sleep
from cmath import sqrt
import numpy as np
import matplotlib.pyplot as plt


def menu_functions_one():
    ops = ('[1] - Calcular Raizes',
    '[2] - Calcular Função em X pedido',
    '[3] - Calcular Vértice',
    '[4] - Gerar Gráfico de Função',
    '[5] - Sair do Submenu')
    while True:
        print('-=-' * 10)
        print('FUNÇÕES DO SEGUNDO GRAU'.center(30))
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
            if ask not in [1, 2, 3, 4, 5]:
                print('\033[31mOpção Inválida\033[m')
                sleep(1)
            else:
                if ask == 1:
                    option_one()
                    sleep(1)
                elif ask == 2:
                    option_two()
                    sleep(1)
                elif ask == 3:
                    option_three()
                    sleep(1)
                elif ask == 4:
                    option_four()
                    sleep(1)
                elif ask == 5:
                    print('-=-' * 10)
                    sleep(1)
                    break


def option_one():
    while True:
        try:
            a = float(input('Digite o coeficiente "A": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente!\033[m')
        else:
            break
    if a > 0:
            while True:
                try:
                    b = float(input('Digite o coeficiente "B": '))
                except ValueError:
                    print('\033[31mErro, Tente Novamente!\033[m')
                else:
                    break
            while True:
                try:
                    c = float(input('Digite o coeficiente "C": '))
                except ValueError:
                    print('\033[31mErro, Tente Novamente!\033[m')
                else:
                    break
            delta = calc_delta(a, b, c)
            if delta < 0:   #usar números complexos
                complex_number_calc_roots(a, b, c, delta)
                sleep(1)
            else:
                calc_roots(a, b, delta)
                sleep(1)
    else:
        print('O valor de "A" deve ser maior que 0!')

def calc_delta(a, b, c):
    return (b ** 2) - (4 * a * c)

def calc_roots(a, b, delta):
    x1 = ((-b) + (delta ** (1/2))) / (2 * a)
    x2 = ((-b) - (delta ** (1/2))) / (2 * a)
    if x1 == x2:
        print(f'O Valor de Delta é: {delta}, portanto, X1 == X2!')
        print(f'O valor de X1 é {x1}, O valor de X2 é {x2}')
    else:
        print(f'O Valor de Delta é: {delta}, portanto, X1 != X2!')
        print(f'O valor de X1 é {x1}, O valor de X2 é {x2}')

def complex_number_calc_roots(a, b, c, delta):
    x1 = ((-b) + (sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
    x2 = ((-b) - (sqrt((b ** 2) - (4 * a * c)))) / (2 * a)
    print(f'O Valor de Delta é: {delta}, portanto, não existem raizes reais')
    print(f'O valor de X1 é {x1}, O valor de X2 é {x2}')


def option_two():
    while True:
        try:
            a = float(input('Digite o coeficiente "A": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente!\033[m')
        else:
            break
    while True:
        try:
            b = float(input('Digite o coeficiente "B": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente!\033[m')
        else:
            break
    while True:
        try:
            c = int(input('Digite o coeficiente "C": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente!\033[m')
        else:
            break
    while True:
        try:
            x = float(input(f'Digite o Valor de "X": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente!\033[m')
        else:
            break
    print(f'f({x}) = {(a * (x ** 2)) + (b * x) + c}')
    sleep(1)


def option_three():
    while True:
        try:
            a = float(input('Digite o coeficiente "A": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente!\033[m')
        else:
            break
    while True:
        try:
            b = float(input('Digite o coeficiente "B": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente!\033[m')
        else:
            break
    while True:
        try:
            c = int(input('Digite o coeficiente "C": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente!\033[m')
        else:
            break
    print(f'XV tem o valor de : {-b / (2 * a)}')
    print(f'YV tem o valor de : {-calc_delta(a, b, c) / (4 * a)}')
    sleep(1)


def option_four():
    while True:
        try:
            a = float(input('Digite o coeficiente "A": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente!\033[m')
        else:
            break
    while True:
        try:
            b = float(input('Digite o coeficiente "B": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente!\033[m')
        else:
            break
    while True:
        try:
            c = float(input('Digite o coeficiente "C": '))
        except ValueError:
            print('\033[31mErro, Tente Novamente!\033[m')
        else:
            break
    x = np.arange(-1000, 1001, 1)
    y = (a * (x * x)) + (b * x) + c
    plt.plot(x, y, 'y', label='ax ** 2 + bx + c')
    plt.legend(loc = 'upper left')
    plt.show()

if __name__ == '__main__':
    pass
