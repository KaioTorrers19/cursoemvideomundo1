distancia = float(input('Quantos km é a sua viajem?'))

if distancia <= 200:
    preço = distancia * 0.45

else:
    preço = distancia * 0.50
print('A sua viajem é de {}KM e o preço dessa viajem sera de R${:.2f}'.format(distancia, preço))