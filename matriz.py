mat = []
qtd = int(input('Digite a quantidade de linhas: '))
colunas = int(input('Digite a quantidade de colunas: '))
for i in range(qtd):
    mat.append([])
    for l in range(colunas):
        num = int(input('Digite os valores em ordem da matriz: '))
        mat[i].append(num)
print(mat)

def menu():
    print('1 - Determinante da Matriz',
          '2 - Multiplicacao da Matriz',
          '3 - Matriz Transposta',
          '4 - Voltar ao menu')
    while True:
        try:
            op = int(input('Digite uma opcao Valida: '))
        except:
            print('Erro, Tente Novamente ! ')
        else:
            if op not in [1,2,3,4]:
                print('Operacao Invalida ! ')
            else:
                if op ==1:
                    pass
                if op ==2:
                    pass
                if op ==3:
                    matriz_transposta(qtd,colunas)
                if op == 4:
                    print('Voltando ao menu principal !')
                    break

def matriz_transposta(qtd,colunas):
    matt = []
    print(mat)
    for i in range(colunas):
        matt.append([])
        for j in range(qtd):
            num = int(input('Digite os numeros das colunas da matriz em ordem: '))
            matt[i].append(num)
    print(matt)
