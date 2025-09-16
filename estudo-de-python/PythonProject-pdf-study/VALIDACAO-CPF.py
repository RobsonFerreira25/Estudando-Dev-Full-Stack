'''
Para realizar o exercício proposto, siga o passo a passo.

    Crie um arquivo fonte chamado validacpf.
     
    Crie uma função que:

    2.1. Remova os caracteres não numéricos.

    2.2. Valide a quantidade de dígitos do CPF.

    2.3 Valide se todos os dígitos não são iguais.

    2.4. Calcule o primeiro dígito verificador e o valide.

    2.5. Calcule o segundo dígito verificador e o valide.
     
    Teste a função passando um CPF como parâmetro.
'''
def validar_cpf(cpf):
    #Removendo caracteres não númerico
    cpf = ''.join(filter(str.isdigit, cpf))

    #Verificando se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    #Verificando se todos os dígitos são iguais (caso raro mais inválido)
    if cpf == cpf[0] * 11:
        return False

    #Calculando o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i)for i in range(9))
    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    #Verificando o primeiro dígito verificador
    if int(cpf[9]) != digito_verificador_1:
        return False

    #Calculando o segundo digito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma %  11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    #Verificando o segundo dígito verificador
    if int(cpf[10]) != digito_verificador_2:
        return False

    #CPF Válido
        return True

#Testando a função
cpf = '123.456.789-09'
if validar_cpf(cpf):
    print(f'O CPF {cpf} é válido.')
else:
    print(f'O CPF {cpf} é válido.')