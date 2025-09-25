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