frase = str(input('digite uma frase:')).upper()
print('a letra A aparece {} vezes'.format(frase.count('A')))
print('a primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('a ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))