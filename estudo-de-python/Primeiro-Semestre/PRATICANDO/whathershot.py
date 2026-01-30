# Definindo atrubutos do personagem
mana_total = 100
mana_atual = 100

# Grimorio de magias (dicionário)
magias = {
    'whathershot': 40

}

# Criar função para lançar magias
def lancar_magia(nome_magia, mana_atual):
    if nome_magia in magias:
        custo = magias[nome_magia]
        if mana_atual >= custo:
            mana_atual -= custo
            print(f'Você lancou {nome_magia}!(-{custo} mana)')
        else:
            print('Mana insuficiente para lançar essa magia!')
    else:
        print('Essa magia nao existe.')

    return mana_atual


print(f'Mana inicial: {mana_atual}')
mana_atual = lancar_magia('whathershot', mana_atual)
print(f'Mana restante: {mana_atual}')
mana_atual  = lancar_magia('whathershot', mana_atual)
print(f'Mana restante: {mana_atual}')
