a = int(input('digite um numero'))
b = int(input('digite outro numero'))
c = int(input('digite o ultimo numero '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

print('o numero menor é {}'.format(menor))

maior = a

if b>a and b>c:
    maior= b

if c>a and c>b:
    maior = c

print(' o maior numero é {}'.format(maior))