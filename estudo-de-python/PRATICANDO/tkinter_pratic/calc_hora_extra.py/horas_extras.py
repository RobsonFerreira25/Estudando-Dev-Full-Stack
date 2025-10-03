def calc_hora_extra(valor_hora: float, adicional: float):
# Calcula o valor da uma hora com adicional (ex.: 0.6 = 60%)
    if valor_hora <= 0:
        raise ValueError('O valor da hora extra deve ser maior que zero.')
    if adicional <= 0:
        raise ValueError('O adicional deve ser negativo.')
    return valor_hora * (1 + adicional)

def calc_bruto_hora_extra(horas_sabado: float, Horas_domingo: float, valor_hora: float):
# Calcula o valor bruto totalç das horas extra.
    valor_sabado = calc_hora_extra(valor_hora, 0.60)
    valor_domingo = calc_hora_extra(valor_hora, 1.00)
    return (horas_sabado * valor_sabado) + (Horas_domingo * valor_domingo)

def calc_descontos(salario_bruto_mensal: float, percentual: float, fixo: float):
# Calcula os descontos (percentual + valor fixo sobre o salário bruto.)
    desconto_percentual = salario_bruto_mensal * percentual
    return desconto_percentual + fixo

def calc_salario_liq(salario_base: float, total_extra_bruto: float, percentual_desconto: float, descoto_fixo: float):
# Retorna salário bruto, descontos e salário liquido final.
    salario_bruto_total = salario_base + total_extra_bruto
    descontos_totais = calc_descontos(salario_bruto_total, percentual_desconto, descoto_fixo)
    slario_liquido_final = salario_bruto_total - descontos_totais

    return{
        'salario_bruto_total': salario_bruto_total,
        'descontos_totais': descontos_totais,
        'salario_liquido_final': slario_liquido_final
    }