# Função iterativa para calcular o fatorial de um número
# Como funciona o fatorial: 5! = 5 * 4 * 3 * 2 * 1 = 120
def fatorial_iterativa(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

# Exemplo de uso
numero = 5
resultado = fatorial_iterativa(numero)
print(f'O fatorial de {numero}! = {resultado}')
