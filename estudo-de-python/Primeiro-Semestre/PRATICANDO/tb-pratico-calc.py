#Trabalho prático: Calculadora Refatorada.

#1. Funções de Operações
def adicao(n1, n2): return n1 + n2
def subtracao(n1, n2): return n1 - n2
def multiplicacao(n1, n2): return n1 * n2
def divisao(n1, n2):
    if n2 == 0: return 'Erro: dividão por zero!'
    else: return n1 /n2

#2. Função Principaç
def calculadora(num1, num2, op):
    op = op.lower() #Normaliza a operação
    if op == '+' or op == 'adicao':
        return adicao(num1, num2)
    elif op == '-' or op == 'subtracao':
        return subtracao(num1, num2)
    elif op == '*' or op == 'multiplicacao':
        return multiplicacao(num1, num2)
    elif op == '/' or op == 'divisao':
        return divisao(num1, num2)
    else:
        return 'Operação inválida.'
    
#Loop Principal de interação
saida = '' #Variável para controlar o loop while

while saida.lower() != 'n': #Continua enquanto a saída nao for 'n' (insensivel a maiúsculas/minusculas).
    try:
        #solicita a entrada, converte para float e trata os erros
        num1 = float(input('Diite o primeiro número:'))
        num2 = float(input('Digite o segundo número:'))
        operacao = input('Digite a operação (+, -, *, / ou nome:): ')

        resultado = calculadora(num1, num2, operacao)
        print(f'Resultado: {resultado}')

    except ValueError:
        print('Entrada inválida. Por favor digite apenas números.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
    
    #Pergunta se quer continuar
    saida = input('Deseja realizar outra operação? (s/n): ')
    if saida.lower() != 's':
        saida = 'n' #Se nao for 's', força a saída

print('Calculadora encerrada.')
