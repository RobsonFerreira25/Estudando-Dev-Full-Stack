print('Modulo KM por Litro Importado.')

def calc_km_l(distancia_km: float, litros_gastos: float):

# Validação das entradas
    if distancia_km <= 0:
        raise ValueError(' A distância tem que ser maior que zero.')
    if litros_gastos <= 0:
        raise ValueError('Os litros gastos tem que ser maiores que zero.')
    
    # Formula: km por litro
    km_por_litro = distancia_km / litros_gastos
    return km_por_litro

# Definindo a função
def calc_litros_100km(distancia_km: float, litros_grastos: float):

# Validando as entradas
    if distancia_km <= 0:
        raise ValueError('A distância em km tem que ser maior que zero')
    if litros_grastos <= 0:
        raise ValueError('Os litros gastos nao podem ser menor que zero.')
    
# Formula litros por 100 km
    calc_litros_100km = (litros_grastos / distancia_km) *100
    return calc_litros_100km

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

# Definindo a função
def calc_custo_km(distancia_km: float, litros_gastos: float, preco_por_litro: float):
    if distancia_km <= 0:
        raise ValueError('A distancia por km tem queser maior que zero')
    if litros_gastos <= 0:
        raise ValueError('Os litros gastos tem que ser maior que zero')
    if preco_por_litro <= 0:
        raise ValueError('O preço por litro tem que ser maior que zero')
    
# Formula: custo por km
    custo_total = (preco_por_litro * litros_gastos) / distancia_km
    return custo_total

# Definindo a função
def estimar_autonomia(litros_tanque: float, km_por_litro: float, ):
    if litros_tanque <= 0:
        raise ValueError('Os litros no tanque tem que ser maior que zero')
    if km_por_litro <= 0:
        raise ValueError('Os litros por km tem que ser maior que zero')
    
# Formula: estimar autonomia
    autonomia_km = litros_tanque * km_por_litro
    return autonomia_km

# Definindo a função
def estimar_litros_necessarios(distancia_km: float, km_por_litro: float):
    if distancia_km <= 0:
        raise ValueError('A distância por km tem que ser maior que zero')
    if km_por_litro <= 0:
        raise ValueError('O km por litro tem que ser maior que zero')
    
# Formula: estimar litros necessarios
    litros_necessarios = distancia_km / km_por_litro
    return litros_necessarios 
