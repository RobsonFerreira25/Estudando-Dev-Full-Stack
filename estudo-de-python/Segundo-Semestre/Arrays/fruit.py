from os import system
system('cls')

fruits = []
fruits.append('orange')
fruits.append('apple')
fruits.append('banana')
fruits.append('grape')
fruits.sort()
fruits.pop(1)
fruits.insert(0, 'orange')
c = fruits.count('orange')

print(f'Esses são os itens do nosso Array:{fruits}')
print(f'A orange aparece {c} vezes no Array')