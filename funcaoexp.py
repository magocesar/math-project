import matplotlib.pyplot as plt
import numpy as np
from menu import menu

def tipo(a, b):
    a = int(input('Qual o valor de "a" : '))
    b = int(input('Qual o valor de "b" :'))
    if b < 0 or b == 1 or a == 0:
         print('Função não existe !!')
    else:
        if 0<b<1 :
            print('Essa função é decrescente !!')
        elif b > 1 :
            print('Essa função é cresente !!') 


def calcula_funcao(a, b, x):
    a = int(input('Qual o valor de "a" : '))
    b = int(input('Qual o valor de "b" :'))
    if b < 0 or b == 1 or a == 0 :
         print('Função não existe !!')
    else:
        x = int(input('Digite o valor de "x" desejado :'))
        funcao = a*(b**x)
        print(f'A função com {x} como valor de x resulta em :{funcao}')


def gerar_graph(a, b, x):
    a = int(input('Qual o valor de "a" : '))
    b = int(input('Qual o valor de "b" :'))
    if b < 0 or b == 1 or a == 0:
         print('Função não existe !!')
    else:
        x1 = np.arange(0, b ** x, 1)
        plt.plot(x1, x1 ** b)
        plt.show()



def funcaoexponencial(): 
        ops=('[1] - Verificar se é crescente ou decrescente.',
        '[2] - Calcular função com outro expoente.',
        '[3] - Gerar gráfico da função.',
        '[4] - Voltar')
        for i in ops:
            print(i)
        while True:
            try:
                opt = int(input('Coloque sua opção :'))
            except ValueError:
                print('\033[31mERRO!\033[m')
            else:
                if opt != [1, 2, 3, 4]:
                    print('\033[31mERRO!\033[m')
                elif opt == '4':
                    menu()
                elif opt == 1:
                    tipo()
                elif opt == 2:
                    calcula_funcao()
                elif opt == 3:
                    gerar_graph()