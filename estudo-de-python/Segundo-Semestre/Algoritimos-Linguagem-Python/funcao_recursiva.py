# Função recursiva para calcular o fatorial de um número
# Como funciona o fatorial: 5! = 5 * 4 * 3 * 2 * 1 = 120
def fatorial_recursivo(n):
    if n == 1 or n == 0: # Caso base, primeiro voce cria o caso base, ou seja, a condicao de parada
        return 1 # Retorna 1, porque 1! = 1
    else: # caso recursivo, ou seja, a condicao de repeticao
        return n * fatorial_recursivo(n-1) # Retorna n * fatorial_recursivo(n-1), ou seja, 5 * fatorial_recursivo(4)
        # 5 * 4 * 3 * 2 * 1 = 120

# Exemplo de uso
numero = 5
resultado = fatorial_recursivo(numero)
print(f'O fatorial de {numero}! = {resultado}')
