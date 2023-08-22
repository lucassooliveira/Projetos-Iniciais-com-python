soma = 0
mult = 1
maior = 0
for c in range(2):
    n = int(input('Digite um valor inteiro qualquer: '))
    soma += n
    mult *= n
    if c == 0:
        maior = n
    else:
        if n > maior:
            maior = n
print('[1] Somar\n', '[2] Multiplicar\n', '[3] Maior\n', '[4] Novos números\n', '[5] Sair do programa\n')
j = 0
while 5 >= j >= 0:
    j = int(input('Digite o número da operação solicitada: '))
    if j == 1:
        print(soma)
    elif j == 2:
        print(mult)
    elif j == 3:  # mostra qual é o maior
        print(maior)
    elif j == 4:  # cria novas variaveis
        n1 = int(input('Digite um valor inteiro qualquer: '))
        n2 = int(input('Digite um valor inteiro qualquer: '))
        soma = n1 + n2
        mult = n1 * n2
        maior = n1 if n1 > n2 else n2
    elif j == 5:  # encerra o programa
        print('Encerrando o programa...')
        break
    else:
        print('Opção invalida, digite um número de 1 a 5.')
