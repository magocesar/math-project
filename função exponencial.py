def funcaoexponencial(a, b):
        print('[1] - Verificar se é crescente ou decrescente.',
        '[2] - Calcular função com outro expoente.',
        '[3] - Gerar gráfico da função.',
        '[4] - Voltar')
        while True:
            try:
                opt = int(input('Coloque sua opção :'))
            except ValueError:
                print('\033[31mERRO!\033[m')
