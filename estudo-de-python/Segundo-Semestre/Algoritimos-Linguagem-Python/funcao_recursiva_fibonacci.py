# Função recursiva para calcular o n-ésimo termo da sequência de Fibonacci
# Como funciona a sequência de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# A sequência de Fibonacci é uma sequência de números inteiros onde cada termo é a soma dos dois termos anteriores.
# A sequência começa com 0 e 1.
def fibonacci_recursivo(n):
    if n == 0: # Caso base, primeiro voce cria o caso base, ou seja, a condicao de parada
        return 0 # Retorna 0, porque 0! = 0
    elif n == 1: # Caso base, primeiro voce cria o caso base, ou seja, a condicao de parada
        return 1 # Retorna 1, porque 1! = 1
    else: # caso recursivo, ou seja, a condicao de repeticao
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2) # Retorna fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2), ou seja, 5 + 4

# Exemplo de uso
numero = 10 # O 10º termo da sequência de Fibonacci é 55
resultado = fibonacci_recursivo(numero)
print(f'O {numero}-ésimo termo da sequência de Fibonacci é {resultado}')
