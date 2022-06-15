import numpy as np
def menu_matriz():
    a = [np.array()]
    qtd = int(input('Digite a quantidade de linhas da matriz: '))
    coluna = int(input('Digite a quantidade de colunas da matriz: '))
    for i in range(qtd):
        a.append([])
        
menu_matriz()