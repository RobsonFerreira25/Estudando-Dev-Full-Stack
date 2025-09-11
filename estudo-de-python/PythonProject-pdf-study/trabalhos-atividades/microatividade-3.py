isca = '' #Vamos começar com uma string vazia para entrar no loop.

while isca != 'fisgou': #Continua enquanto a resposta Nao for 'fisgou'
    isca = input('Digite algo ou "fisgou" para encerrar')
    if isca != 'fisgou': #Só imprime se nao for o comando para fisgar
        print(f'Você digitou {isca}')
print('Peixe fisgado!')