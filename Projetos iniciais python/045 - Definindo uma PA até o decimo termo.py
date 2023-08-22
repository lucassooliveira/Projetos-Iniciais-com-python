n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite sua razão: '))
t1 = (r * 1)
t = (n - t1) + (r * 11)
for c in range(n, t, r):
    print('Os termos até o décimo termo da PA é igual a {}'.format(c))