# Definir atributos do jogador
mana_total = 100
mana_atual = 100

# criar o grimório (dicionários)
magias = {
    'siesmicwave': 35

}

# Criar a função lançar magia.
def lancar_magia(nome_magia, mana_atual):
    if nome_magia in magias:
        custo = magias[nome_magia]
        if mana_atual >= custo:
            mana_atual -= custo
        print(f'Você lançou {nome_magia}! -{custo} de mana ')
    else:
        print('Mana insuficiente para lançar essa magia.')

    return mana_atual

# Exemplo de uso
print(f'Mana inicial: {mana_atual}')
mana_atual = lancar_magia('siesmicwave', mana_atual)
print(f'Mnana atual: {mana_atual}')
mana_atual = lancar_magia('siesmicwave', mana_atual)
print(f'Resta: {mana_atual} de mana.')
