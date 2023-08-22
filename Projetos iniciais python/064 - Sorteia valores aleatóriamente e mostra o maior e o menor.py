from random import randint as x

sort = (x(1, 10), x(1, 10), x(1, 10), x(1, 10), x(1, 10))
print(f'Os valores sorteados foram: {sort[0]} {sort[1]} {sort[2]} {sort[3]} {sort[4]}')
mm = sorted(sort)
menor = mm[0]
maior = mm[-1]
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')