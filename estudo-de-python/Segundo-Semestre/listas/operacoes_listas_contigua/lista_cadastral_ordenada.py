# Lista Cadastral Ordenada
from os import system
from datetime import datetime
system("cls")

clientes = [
    ['Robson Ferreira', 'Ana Silva', 'Pedro Oliveira'],
    ['25/06/1988', '15/07/1992', '20/08/2005'],
    ['02/01/2024', '02/01/2024', '02/01/2024']
]

# Ordenar clientes
def ordenar_clientes():
    for i in range(len(clientes)):
        clientes[i].sort() # Ordena os clientes, o sort() ordena os clientes em ordem alfabética
        print(clientes[i])
    return clientes

# Inserir um cliente na lista
def inserir_cliente():
    print(f'Lista de clientes antes de inserir o novo cliente: \n{clientes[0]}\n{clientes[1]}\n{clientes[2]}')
    nome_cliente = input("Digite o nome do cliente: ")
    clientes[0].append(nome_cliente) # Adiciona o nome do cliente na lista de clientes
    data_nascimento = input("Digite a data de nascimento do cliente: ")
    clientes[1].append(data_nascimento) # Adiciona a data de nascimento do cliente na lista de clientes
    data_ultimma_compra = input("Digite a data de cadastro do cliente: ")
    clientes[2].append(data_ultimma_compra) # Adiciona a data da ultima compra do cliente na lista de clientes
    print(f'Lista de clientes depois de inserir o novo cliente: \n{clientes[0]}\n{clientes[1]}\n{clientes[2]}')
    return clientes

# Busca de clientes
def buscar_cliente():
    for i in range(len(clientes)):
        if clientes[i] == 'Robson Ferreira':
            print(f'O cliente {clientes[i]} esta na posição {clientes.index(clientes[i])}')
    return clientes

# Remover um cliente da lista
def remover_cliente():
    print(f'Lista de clientes antes de remover o cliente: \n{clientes[0]}\n{clientes[1]}\n{clientes[2]}')
    clientes[0].remove('Robson Ferreira')
    clientes[1].remove('25/06/1988')
    clientes[2].remove('02/01/2024')
    print(f'Lista de clientes depois de remover o cliente: \n{clientes[0]}\n{clientes[1]}\n{clientes[2]}')
    return clientes

ordenar_clientes()
inserir_cliente()
buscar_cliente()
remover_cliente()
