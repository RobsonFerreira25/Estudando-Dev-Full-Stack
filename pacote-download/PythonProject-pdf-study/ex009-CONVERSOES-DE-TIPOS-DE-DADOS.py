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