n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite sua razão: '))
t1 = (r * 1)
t = (n - t1) + (r * 11)
c = 1
nat = n
while c < 10:
    print('Os termos até o {}° da PA é igual a {}'.format(c, nat))
    nat += r
    c += 1