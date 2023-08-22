def menu():
    print('='*7, 'LOJA SUPER BARATÃO', '='*7)
    print('-'*20)

    
menu()
contm = contf = 0
preco_barato = float('inf')     #atualiza a variável com o maior valor possivel no tipo float
produto_barato = ''
while True:
    produto = str(input('Nome do produto: ')).upper().strip()
    while True:
        preco = float(input('Preço: R$ '))
        contf += preco

        if preco > 1000:
            contm += 1

        if preco < preco_barato:
            preco_barato = preco
            produto_barato = produto

        so = str(input('Quer continuar? [S/N] ')).upper().strip()
        if so in ['S', 'N']:
            break

    print('-' * 20)

    if so == 'S':
        continue
    elif so == 'N':
        break
menu()
print(f'O total da compra foi R$ {contf}')
print(f'Temos {contm} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi a {produto_barato} que custou R$ {preco_barato:.2f}')