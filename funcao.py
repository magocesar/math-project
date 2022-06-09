import matplotlib.pyplot

while True:
    try:
        a = int(input('Digite o valor de a: '))
    except:
        print('Erro, Tente Novamente ! ')
        break
while True:
    try:
        b = int(input('Digite o valor de b: '))
    except:
        print('Erro, Tente Novamente ! ')
        break
while True:
    try:
        c = int(input('Digite o valor de c: '))
    except:
        print('Erro, Tente Novamente ! ')
        break
funcao_2grau(a,b,c)
def funcao_2grau(a, b, c):
    while True:
     print('[1] - Calcular raizes',
           '[2] - Calcular funcao',
           '[3] - Calcular vertice',
           '[4] - Imprimir grafico',
           '[5] - Sair')
         while True:
          try:
           op = int(input('Digite uma opcao : '))
           if op == 1:
               calcular_raizes(a, b, c)
           if op ==2:
               calcular_funcao(a,b,c)
           if op == 3:
               calcular_vertice(a,b,c)
           if op == 4:
               #Faltando o import certo na biblioteca 
            if op == 5:
               print('Voltando ao menu principal')
               break
          except:
            print('Erro, Tente Novamente !')
         break


def calcular_raizes(a,b,c):
    delta = (b * b ) - (4 ac)
    if delta < 0:
        abc = print('Com estes valores a equacao nao possui raizes reais.')
        return abc
    raiz = (delta 1/2)
    calculo = -b + raiz/ (2a)
    calculo1 = -b - raiz/ (2a)
    resultado = calculo, calculo1
    return resultado


def calcular_funcao(a,b,c):
    x = int(input('Digite o valor de x: '))
    calculo = (a * (x2)) + (bx) + c
    return calculo


def calcular_vertice(a,b,c):
    delta = (b b) - (4 * a * c)
    vertx = -b/(2a)
    verty = -delta/(4a)
    vertices = vertx, verty
    m = print('Vertices de maximo')
    mm = print('Vertices de minimo')
    if a>0:
        return vertices, m
    else:
        return vertices, mm
        