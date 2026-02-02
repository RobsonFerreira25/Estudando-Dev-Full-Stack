# Aplicação em lista contígua
from os import system
system("cls")
produtos = [
    [35, 2, 15], # id, quantidade, estoque indice 0 de produtos
    ['Feijão', 'Palmito', 'Laranja'], # indice 1 de produtos
    [5.00, 20.00, 3.00] # indice 2 de produtos
]

# Inserir um produto na lista
def inserir_produto(produtos):
    print(f'Lista de produtos antes de inserir o novo produto: \n{produtos[0]}\n{produtos[1]}\n{produtos[2]}')
    # Inserir uma ID de produto
    id_produto = input("Digite a ID do produto: ")
    produtos[0].append(id_produto)

    # inserir um produto na lista de produtos
    nome_produto = input("Digite o nome do produto: ")
    produtos[1].append(nome_produto)

    # Inserir um preço de produto
    preco_produto = input('Digite o preço do produto: ')
    produtos[2].append(preco_produto)

    print(f'Lista de produtos depois de inserir o novo produto: \n{produtos[0]}\n{produtos[1]}\n{produtos[2]}')

    return

# Buscar um produto na lista
def busca_produto(produtos):
    # A lista de nomes é o segundo elemento da lista principal (índice 1)
    nomes = produtos[1]
    
    for i in range(len(nomes)):
        if nomes[i] == 'Palmito':
            print(f'O produto {nomes[i]} esta na posição {nomes.index(nomes[i])}')
            # Opcional: mostrar os outros dados relacionados usando o mesmo índice 'i'
            # id_produto = produtos[0][i]
            # preco_produto = produtos[2][i]
    return

# Remover um produto da lista
def remover_produto(produtos):
    print(f'Lista de produtos antes de remover o produto: \n{produtos[0]}\n{produtos[1]}\n{produtos[2]}')
    produtos[0].remove('8')
    produtos[1].remove('Bife')
    produtos[2].remove('55.40')
    print(f'Lista de produtos depois de remover o produto: \n{produtos[0]}\n{produtos[1]}\n{produtos[2]}')
    return


inserir_produto(produtos)
busca_produto(produtos)
remover_produto(produtos)