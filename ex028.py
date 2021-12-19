from random import randint
computador = randint(0,5)
print('-=- ' *20)
print('o computador esta pensando em um numero de 0 a 5 consegue descobrir qual?')
print('-=- ' *20)
usuario = int(input('digite um numero para jogar'))
if computador == usuario:
    print(' Parabens você acertou, o numero que o computador pensou é {}  !'.format(computador))
else:
    print('o computador ganhou ele pensou no valor {}! e você o {}!'.format(computador, usuario))
