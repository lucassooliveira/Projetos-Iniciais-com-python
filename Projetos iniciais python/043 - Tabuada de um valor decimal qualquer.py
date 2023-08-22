n = int(input('Digite um valor: '))
for c in range(1, 10):
    g = c
    c *= n
    print('A tabuada de {} é {}x{} que é igual a {}'.format(n, n, g, c))