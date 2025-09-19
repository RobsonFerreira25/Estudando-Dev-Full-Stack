# Definindo os atributos do personagem
mana_total = 100
mana_atual = 100

#Dicionarios de magia com custo de mana
magias = {
    'firebolt': 20

}

# Criar funçao para lançar magia
def lancar_magia(nome_magia, mana_atual):
    '''
    Para lançar magias.
    Parametros:
        - nome_magia (str): Nome da magia que o jogador
        pretende lançar.
        - mana_atual (int): A quantidade de mana disponivel
        no momento.
    retorno:
        -(mana_atual): A noma quantidade de mana após lançar a magia ou não.
    '''
    if nome_magia in magias: # Verifica se a magia existe no dicionário
        custo = magias[nome_magia] # Pega o custo da magia.
        if mana_atual >= custo: #verificando se a mana suficiente
            mana_atual -= custo # Subtrai o custo da mgia da mana atual
            print(f'Você lançou {nome_magia}! (-{custo} mana)')
        else:
            print('Mana insufucuente para lançar essa magia!')
    else:
        print('Essa magia não existe.')
    
    return mana_atual


# Exemplo de uso
print(f'Mana inicial: {mana_atual}')
mana_atual = lancar_magia('firebolt', mana_atual)
print(f'Mana restante: {mana_atual}')
mana_atual = lancar_magia('firebolt', mana_atual)
print(f'Mana restante: {mana_atual}')
