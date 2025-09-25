# Definindo a função
def calc_custo_total(litros_gastos: float, preco_por_litro: float):

# Validando as entradas
    if litros_gastos <= 0:
        raise ValueError('Os litros gastos tem que ser maior que zero')
    if preco_por_litro <= 0:
        raise ValueError('O preço por litro deve ser maior que zero')
    
# Formula: custo total
    custo_total = preco_por_litro * litros_gastos
    return custo_total
