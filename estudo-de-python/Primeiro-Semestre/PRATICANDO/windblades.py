# Atributos do perssonagem
mana_total = 100
mana_atual = 100

# Criar grimório (dicionário)
magias = {
    'windblades': 40

}

# Criar função lançar magia
def lancar_magia(nome_magia, mana_atual):
    if nome_magia in magias:
        custo = magias[nome_magia]
        if mana_atual >= custo:
            mana_atual -= custo
            print(f'Você lançou {nome_magia}! -{custo} de mana')
        else:
            print('Mana insuficiente para lançar essa magia.')

    return mana_atual


# Exemplo de uso
print(f'Mana inicial: {mana_atual}')
mana_atual = lancar_magia(windblades), mana_atual
print(f'Mana restante: {mana_atual}')
mana_atual = lancar_magia(windblades), mana_atual
print(f'Mana restante: {mana_atual}')

