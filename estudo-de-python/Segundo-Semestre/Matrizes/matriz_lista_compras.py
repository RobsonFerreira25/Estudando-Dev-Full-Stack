from os import system
system('cls')

lista_compras = [
    ['pao', 10, 16.30],
    ['leite', 2, 6.80],
    ['ovo', 12, 19.90],
    ['carne', 2.5, 80.79]
]

print('Esses são os itens da primeira linha')
for item in lista_compras[0]:
    print(item, end=' ')
    
print()

print('Esses são todos os itens da matriz')
for itens in lista_compras:
    for item in itens:
        print(item, end=' ')
    print()
    
print('Um elemento da matriz: ')
print('O elemento escolhido foi: ', lista_compras[2][1])
