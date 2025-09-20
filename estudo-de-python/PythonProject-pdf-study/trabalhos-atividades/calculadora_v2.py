saida = ''

def adicao(n1, n2): return n1 + n1
def subtracao(n1, n2): return n1 - n2
def multiplicacao(n1, n2): return n1 * n2
def divisao(n1, n2):
    if n2 == 0: return 'Erro: dividão por zero!'
    else: return n1 /n2

def calculadora(n1, n2, op):
    op = op.lower()
    if op == '+' or op == 'adicao':
        return adicao(n1, n2)
    if op == '-' or op == 'subtracao':
        return subtracao(n1, n2)
    if op == '*' or op == 'multiplicacao':
        return multiplicacao(n1, n2)
    if op == '/' or op == 'divisao':
        return divisao(n1, n2)
    else:
        return 'Operação invalida.'

saida = ''

while saida.lower() != 'n':
    try:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
        operacao = input('Digite a operação desejada (+, -, *, / ou nome):')
    
        resultado = calculadora(n1, n2, operacao)
        print(f'Resultado: {resultado}')
    
    except ValueError:
        print('Entrada invalida. Por favor digite apenas números.')
    except Exception as e:
        print('Ocorreu um erro: {e}')
    
    saida = input('Deseja realizar outra operação s/n: ')
    if saida.lower() != 's':
        saida = 'n'

print('Calculadora Encerrada.')
