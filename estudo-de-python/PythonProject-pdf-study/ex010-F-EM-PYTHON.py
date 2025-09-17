'''
Em Python, um "f" antes de uma string indica uma f-string 
(literal de string formatada), um recurso introduzido no 
Python 3.6 para incorporar expressões e variáveis 
diretamente dentro de strings de maneira concisa e 
legível. Para usá-las, basta prefixar a string com 
"f" ou "F" e envolver as expressões desejadas entre chaves {}. 
Como usar f-strings
Prefixar a string: Adicione um "f" ou "F" 
imediatamente antes das aspas iniciais da sua string. 
Inserir expressões entre chaves: Coloque qualquer 
expressão Python válida (como nomes de variáveis, 
chamadas de funções ou operações matemáticas) dentro de chaves {}. 
'''
#====================================================================
nome = 'mundo'
mensagem = f'Olá, {nome}'
print(mensagem) # Saída: Olá Mundo!

#================================================
'''
Entendendo Facilmente

Metáfora:
Imagine que você está preenchendo um contrato de missão. Em vez de escrever:

    "Olá, [Nome]. Sua missão em [Local] começa agora."

Você tem um contrato inteligente que preenche sozinho:

    f"Olá, {nome}. Sua missão em {local} começa agora."

O f na frente da string é o que ativa essa "mágica"!
'''
#=====================================================
'''
Explicação Detalhada
1. Sintaxe Básica das f-strings

Basta colocar f antes das aspas e usar {variavel} dentro da string:
'''
#=====================================================
nome = 'Arya'
nivel = 5
mensagem = f'jogador {nome} está no nivel {nivel}'
print(mensagem) # O jogador Arya está no nivel 5

#=====================================================
# 2. Vantagens sobre outros Métodos
# Método antigo Concatenação
mensagem = 'jogador' + nome + 'está no nivel' + str(nivel)

#=====================================================
# Método format()
mensagem = f'jogador {nome} está no nivel {nivel}'

#=====================================================
# 3. Operação direto na f-striing
# Você pode fazer calculos dentro das chaves
vida = 100
dano = 25
status = f'Vida restantes: {vida - dano}'
print(status) # Vida restante: 75

#=====================================================
# Formatação de números
# Controlar casas decimais, largura, etc
preco = 50.785
mensagem = f'Preço: R$ {preco:.2f}' # 2 casas decimais
print(mensagem) # Preço: R$ 50.78

#=====================================================
# Chamadas de funções
def calcular_xp(nivel):
    return nivel * 100
mensagem = f'XP necessário: {calcular_xp(5)}'
print(mensagem) # XP necessário: 500

#=====================================================
# Exemplo prático (Sistema de status)
personagem = {
    'nome': 'Malof',
    'classe': 'mago',
    'vida': 80,
    'mana': 150

}

status = f'''
=== STATUS ===
Nome: {personagem['nome']}
Classe: {personagem['classe']}
Vida: {personagem['vida']}/100
Mana: {personagem['mana']}/200
==============
'''


print(status)