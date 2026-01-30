import consumo_combustivel as cc

# Dados de exemple
distancia = 500      # km
litros = 40          # L
preco_litro = 6.59   # R$
tanque = 60          # L


# Calculos
consumo_km_l = cc.calc_km_l(distancia, litros)
consumo_l_100 = cc.calc_litros_100km(distancia, litros)
custo_total = cc.calc_custo_total(litros, preco_litro)
custo_km = cc.calc_custo_km(distancia, litros, preco_litro)
autonomia = cc.estimar_autonomia(tanque, consumo_km_l)
litros_viagem = cc.estimar_litros_necessarios(800, consumo_km_l)

# Exibindo resultado
print(f'Consumo: {consumo_km_l:.2f} km/L')
print(f'Consumo: {consumo_l_100:.2f} L/100km')
print(f'Custo total: R$: {custo_total:.2f}')
print(f'Custo por km: R$: {custo_km:.2f}')
print(f'Autonimia com tanque cheio: {autonomia:.2f} km')
print(f'Litros necessários para 800 km: {litros_viagem:.2f} L')
