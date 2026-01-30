from os import system
system('cls')

nomes = []
nomes.append('Maria')
nomes.append('José')
nomes.append('Mario')
nomes.append('Roberto')
nomes.sort()
nomes.pop(1)
nomes.insert(0, 'José')
c = nomes.count('José')

print(f'Os nomes no Array são {nomes}')
print(f'O nome José aparece {c} vezes em nosso Array')