# Busca em lista contigua
nomes = ['Ana', 'Pedro', 'Maria', 'Carlos', 'Fernanda']
nome_buscado = 'Maria'

for nome in nomes:
    if nome == nome_buscado:
        print(f'O nome buscado esta na posição {nomes.index(nome_buscado)}')
        break