'''
Em Python, a conversão de tipos de dados ocorre
através de casting explícito, usando funções como
int(), float(), str(), list() e tuple() para converter um objeto
para o tipo desejado, como, por exemplo, converter a string "10"
para o inteiro 10 com int("10"). Existem também as conversões implícitas,
onde o Python converte automaticamente um tipo para outro mais compatível,
como de int para float, para evitar perda de dados.
Conversões Explícitas (Casting)
Estas são as conversões diretas que você, como programador, solicita:
int(valor): Converte um valor para um número inteiro.
Se a entrada for um float, a parte decimal é removida.
Exemplo: int("123") resulta em 123, e int(3.9) resulta em 3.
float(valor): Converte um valor para um número de ponto flutuante.
Exemplo: float(7) resulta em 7.0, e float("3.14") resulta em 3.14.
str(valor): Converte um valor de qualquer tipo para uma string.
Exemplo: str(42) resulta em '42', e str(2.718) resulta em '2.718'.
list(valor): Converte um valor (como uma string ou tupla) para uma lista.
tuple(valor): Converte um valor para uma tupla.
Conversões Implícitas
Estas são realizadas automaticamente pelo Python quando
um tipo de dado mais pequeno é combinado com um tipo de dado
maior na mesma operação, ou quando é necessário para a execução da operação.
Exemplo: Em uma operação matemática, se você somar um int com um float,
o int será convertido para float para que a operação seja realizada
sem perda de dados, como em 5 + 2.5, onde 5 é implicitamente convertido para 5.0.
Limitações
Nem todas as strings podem ser convertidas para números;
uma string como "abc" resultará num erro.
Ao converter um float para um int, a parte decimal é simplesmente truncada,
não arredondada para o número inteiro mais próximo.
'''
#================================================
'''
Entendendo Facilmente

Metáfora:
Imagine que você tem moedas de ouro (string "100") e quer somá-las com outras moedas. Você precisa convertê-las para números (int) antes, senão o Python vai apenas colar os textos: "100" + "50" = "10050" (e não 150!).

Piada (natural):
— Por que o int() foi parar no hospital?
— Porque ele tentou converter "dois" para número e teve um bug mental! 
=================================================
Explicação Detalhada
1. As Principais Funções de Conversão

Python tem funções built-in para conversão:

Função:  |Converte para: |Exemplo:
int()====|Número inteiro |int('10') == 10
float()==|Número decimal |float('3.14') == 3.14 
str()====|Texto (string) |str(50) =='50'
bool()===|Booleano       |bool(1) == True
'''
#================================================
#2. Conversões Númericas (int e float)
#string para numero
idade = '25'
idade_int = int(idade) # 25 converte para inteiro
print(f'{idade_int}')

preco = '9.99'
preco_float = float(preco) # 9.99 convertifo para decimal
print(f'{preco_float}')

#Número para string
pontos = 1000
pontos_str = str(pontos) #'1000' convertido para string
print(f'{pontos_str}')
#================================================
#3. Conversão para Booleano (Bool)
'''
Valores que viram False:

    0, 0.0, "" (string vazia), None, [] (lista vazia)

Valores que viram True:

    Quase todo o resto!
'''
#================================================
print(bool(0)) #False
print(bool('oi')) #true
print(bool([])) #False
#================================================
#4. Conversões implicitas (Python faz automaticamente)
#Em operações númericas, python converte para o tipo mais 'forte':
#================================================
resultado = 5 + 25 # int + float == float (7.5)
print(resultado)
print(type(resultado))
#================================================
#Cuidado com erros comuns!
#a) Conversão de texto não-numerico
#int('dez') == ValueError
# Solução: Verifique antes com isdigit()
#================================================
texto = 'dez'
if texto.isdigit(): # Verifica se a string e um numero.
    numero = int(texto)
else:
    print('Não é um Número!')
#================================================
# b) Float para Int (perca de precisão)
numero = int(3.99) # 3 (corta decimais, não arredonda!)
print(numero)
#================================================
# c) Conversão de Listas
lista = [1, 2, 3]
lista_str = str(lista) # '[1, 2, 3]'
#================================================
#Exemplo prático (sistema de loja em RPG)

# Input sempre retorna string!
ouro_input = input('Qauntas moedas de ouro? ') # ex: '150'
preco_espada = 75

# Converta para int antes de calcular!
ouro_int = int(ouro_input)
troco = ouro_int - preco_espada

print(f'Você comprou a espada. Troco: {troco} moerdas de ouro')

#================================================
# Técnica Ninja: Try/Except para Conversão Segura

entrada = '123abc'
try:
    numero = int(entrada)
    print('Número convertido', numero)
except ValueError:
    print('Isso não é um numero válido!')

#===============================================
'''
Em Python, a instrução try é usada em conjunto com except, else e finally para o tratamento de exceções (erros) em um programa. O bloco try contém o código que pode gerar um erro, enquanto o bloco except lida com o erro caso ele ocorra, o else executa código sem erro e o finally executa código sempre, independentemente do resultado. 
Como funciona:
try: O código dentro do bloco try é executado. 
except: Se ocorrer uma exceção (um erro) no bloco try, a execução do try é interrompida, o bloco except correspondente é executado para lidar com o erro. 
else: Se nenhuma exceção ocorrer no bloco try, a cláusula else será executada. 
finally: O código dentro do bloco finally é sempre executado, seja após um erro ou sem ele, sendo útil para ações de limpeza, como fechar um arquivo. 
'''
#===============================================
try:
    # Código que pode gerar um erro (ex: divisão por zero)
    resultado = 10 / 0
except ZeroDivisionError:
    # Código para lidar com o erro de divisão por zero
    print("Erro: Divisão por zero não é permitida.")
else:
    # Código que será executado se nenhuma exceção ocorrer no try
    print("A operação foi bem-sucedida, resultado:", resultado)
finally:
    # Código que sempre será executado
    print("Fim do bloco de tratamento de exceções.")

#===============================================
#Desafio Interativo:
#O que acontece se você converter "True" para bool?
texto = "True"
valor_booleano = bool(texto)
print(valor_booleano)  # True ou False?
# Resposta: True (porque qualquer string não vazia vira True)!