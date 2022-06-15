from menu import menu

def tipo(a, b, x):
    x = input('Qual o valor de x :')
    if x < 2 :
        print('Essa função não é exponencial !!')
    else:
        a = int(input('Qual o valor de "a" : '))
        b = int(input('Qual o valor de "b" :'))
        if b == 0 or b < 0 :
            print('Função inválida')
        else:
            pass



def funcaoexponencial(): 
        print('[1] - Verificar se é crescente ou decrescente.',
        '[2] - Calcular função com outro expoente.',
        '[3] - Gerar gráfico da função.',
        '[4] - Voltar')
        while True:
            try:
                opt = int(input('Coloque sua opção :'))
            except ValueError:
                print('\033[31mERRO!\033[m')
            else:
                if opt != [1, 2, 3, 4]:
                    print('\033[31mERRO!\033[m')
                elif opt == '4':
                    return menu
