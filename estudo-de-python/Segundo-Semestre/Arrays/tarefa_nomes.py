from os import system
system('cls')

nomes = [] # Variavel vetorial

for i in range(5):
    nome = str(input(f'Digite o {i+1} º nome: '))
    nomes.append(nome)
print('Nomes inseridos no Array')
print(nomes)
nomes.sort()
print(f'Esses sao os nomes em ordem alfabetica: \n{nomes}')
