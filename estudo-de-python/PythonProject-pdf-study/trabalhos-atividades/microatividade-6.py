#Funções com argumentos e .lower()
'''
Uma função que verifica se o usuario
tem a permissão de pescar
'''

def verificar_permissao(nivel_acesso):
    if nivel_acesso.lower() == 'ver_hab':
        print('Você está habilitado para pescar, Pescador Profissional!')
    else:
        print('Habilitado apenas para pesca desembarcada. Boa Pescaria')
#Testando a função com diferentes entradas
verificar_permissao('Ver_hab')
verificar_permissao('ver_hab')
verificar_permissao('VER_HAB')
verificar_permissao('Convidado')
    #.lower() Converte a entrada para a minuscula
    #para comparação simples