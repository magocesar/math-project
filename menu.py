
#César

def menu():
    ops = ('[1] - Função do Segundo Grau.',
    '[2] - Funções Exponenciais.',
    '[3] - Matrizes.',
    '[4] - Sair do Programa.')
    print('Operações'.center(30))
    for op in ops:
        print(op)
    print('-=-' * 10)
    while True:
        try:
            ask = int(input('Digite uma Opção Válida: '))
        except ValueError:
            print('\033[31mERRO!\033[m')
        else:
            if ask not in [1, 2, 3]:
                print('\033[31mOPÇÃO INVÁLIDA\033[m')
            else:
                if ask == 1:
                    pass
                elif ask == 2:
                    pass
                elif ask == 3:
                    pass
                elif ask == 4:
                    print('Até Breve!')
                    break
                