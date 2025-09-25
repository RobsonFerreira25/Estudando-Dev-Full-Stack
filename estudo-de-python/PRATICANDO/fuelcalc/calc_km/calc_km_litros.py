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

    

