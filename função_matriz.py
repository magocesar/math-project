
from msilib.schema import Error
from time import sleep
from urllib import robotparser
import numpy as np
from pyparsing import col

def inform_matrix():
    while True:
        try:
            rows = int(input('Informe o Número de Linhas: '))
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            break
    while True:
        try:
            columns = int(input('Informe o Número de Colunas: '))
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            break
    final_list = []
    for r in range(rows):
        temporary_list = []
        for c in range(columns):
            while True:
                try:
                    n = int(input(f'Digite o Valor de: [{r}, {c}]'))
                except ValueError:
                    print('\033[31mErro, Tente Novamente\033[m')
                else:
                    break
            temporary_list.append(n)
        final_list.append(temporary_list)
    m = np.array(final_list)
    print(m)
    return m, rows, columns

def menu_functions_three():
    ops = ('[1] - Verificar Determinante',
    '[2] - Multiplicação de Matrizes',
    '[3] - Matriz Transposta',
    '[4] - Mudar Matriz',
    '[5] - Sair do Submenu')
    m, rows, columns = inform_matrix()
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
            if ask not in [1, 2, 3, 4, 5]:
                print('\033[31mOpção Inválida\033[m')
                sleep(1)
            else:
                if ask == 1:
                    option_one(m, rows, columns)
                    sleep(1)
                elif ask == 2:
                    option_two(m)
                    sleep(1)
                elif ask == 3:
                    option_three(m)
                    sleep(1)
                elif ask == 4:
                    m, rows, columns = inform_matrix()
                    sleep(1)
                elif ask == 5:
                    print('-=-' * 10)
                    sleep(1)
                    break

           

def option_one(matrix, rows, columns):
    if rows == columns:
        print('A Matriz é Quadrada')
        print(f'O determinante dessa Matriz {rows}x{columns} é: ')
        det = np.linalg.det(matrix)
        print(det)
        sleep(1)
    elif rows != columns:
        print('A Matriz não é Quadrada')
        sleep(1)

def option_two(matrix):
    print('Por Favor, Insira as Informações da Segunda Matriz')
    second_matrix, second_row, second_column = inform_matrix()
    print('Primeira Matriz:')
    print(matrix)
    print('-=-' * 10)
    print('Segunda Matriz:')
    print(second_matrix)
    print('-=-' * 10)
    try:
        result = np.dot(matrix, second_matrix)
    except Error:
        print('As Condições de Multiplicação Não Foram Atendidas')
        sleep(1)
    else:
        print('O resultado da Multiplicação é:')
        print(result)
        sleep(1)

def option_three(matrix):
    print(f'A Matriz Trasposta é: ')
    print(matrix.T)

