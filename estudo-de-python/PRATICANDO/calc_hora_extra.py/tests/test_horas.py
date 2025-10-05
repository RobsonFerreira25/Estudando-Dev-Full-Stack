import pytest
import horas_extras as he


def test_calc_valor_hora_extra():
    assert he.calc_hora_extra(14.38, 0.6) == pytest.approx(23.008)


def test_calc_total_bruto_extra():
    total = he.calc_bruto_hora_extra(10, 6, 14.38)
    assert total == pytest.approx(402.64)


def test_calc_descontos():
    assert he.calc_descontos(4000.00, 0.17, 150.00) == pytest.approx(830.00)


def test_calc_salario_liq_integra():
    extras_bruto = he.calc_bruto_hora_extra(10, 6, 14.38)
    resultado = he.calc_salario_liq(3165.00, extras_bruto, 0.17, )


    assert 'salario_liqui_final' in resultado
    assert resultado['salario_bruto_total'] == pytest.approx(3567.64)
    assert resultado ['descontos_totais'] == pytest.approx(756.4988)
    assert resultado['salario_liquido_final'] == pytest.approx(2811.1412)


def teste_calc_valor_hora_extra_raises_on_invalid():
    with pytest.raises(ValueError):
        he.calc_hora_extra(0, 0.6)


def test_type_error_on_non_numeric_inputs():
    with pytest.raises(TypeError):
        he.calc_hora_extra('14.38', 0.6)

