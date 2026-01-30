print('Módulo IMC importado')

def calcula_imc(peso, altura):
    print('Parâmetro peso:', peso)
    print('Parâmetro altura:', altura)
    imc = peso / altura **2
    return imc

print('Função Classifica importada')

def classifica_imc(indice):
    if indice < 18.5:
        return 'Baixo peso'
    elif indice < 25:
        return 'Peso adequado'
    elif indice < 30:
        return 'Sobrepeso'
    else:
        return 'Obeso'
    