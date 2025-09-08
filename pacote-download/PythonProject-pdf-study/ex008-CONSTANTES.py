#Constantes em Python
'''
Em Python, constantes são valores que não mudam
durante a execução do programa, e a forma de indicá-las
é usar um nome de variável em letras maiúsculas,
seguindo uma convenção da comunidade de programação,
pois a linguagem não tem uma sintaxe nativa para
forçar a imutabilidade. Estas constantes podem ser
números, strings, ou outras estruturas de dados,
e a convenção é que não se deve alterar o valor
de uma variável nomeada assim, embora tecnicamente
seja possível, o que pode prejudicar a legibilidade
e manutenção do código.

Como usar constantes em Python
Defina em letras maiúsculas: Escreva o nome da constante
em letras maiúsculas. Se o nome tiver várias palavras,
use o formato snake_case
(letras minúsculas separadas por underscores).
'''
#======================================================================
PI = 3.14159
MAX_TENTATIVAS = 3
MENSSAGEM_DE_BOAS_VINDAS = 'Bem Vindo!'
print(MENSSAGEM_DE_BOAS_VINDAS)
#======================================================================
'''
1. Não altere o valor: Evite alterar o valor de variáveis 
nomeadas em maiúsculas durante a execução do programa, 
pois isso vai contra a intenção da convenção e 
pode tornar o código confuso. 
Por que usar constantes?

Legibilidade:
Nomes em maiúsculas para constantes tornam o 
código mais fácil de ler, pois indicam imediatamente 
que se trata de um valor fixo.
 
Manutenção:
Ao usar constantes para valores que não mudam, 
você facilita a manutenção, pois qualquer alteração 
necessária no valor será feita em um único local.

Organização:
As constantes ajudam a organizar o código, 
agrupando valores importantes que são usados 
repetidamente em diferentes partes do programa. 

Exemplos de uso 
Matemática: Valores como PI ou o número de Euler.
Configuração: Limites de tentativas, 
tempo limite ou outras configurações do programa.
Mensagens: Textos de mensagens padrão ou de status.

1. Use maiusculas para constantes (é a convenção universal de Python)
2. Coloque constantes no topo do arquivo ou em um modulo separado
3. Nunca altere apos a definição (mesmo que python permita)
4. para dados imutaveis, use tuplas ao inves de de listas.
'''
#=====================================================================================
#exemplo em um jogo
#Constantes Imutaveis
VIDA_INICIAL = 100
DANO_ESPADA  = 25
DANO_MAGIA = 50
NIVEIS_DIFICULDADE = ('Fácil', 'Médio', 'Difício')

from constantes import *

def atacar_inimigo(tipo_ataque):
    if tipo_ataque == 'espada':
        return DANO_ESPADA
    elif tipo_ataque == 'magia':
        return DANO_MAGIA
dano = atacar_inimigo('magia')
print(f'dano causado: {dano}') #50