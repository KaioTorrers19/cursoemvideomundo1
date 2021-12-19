km = float(input('Qual é a velocidade do carro atualmente?'))
multa = (km - 80) * 7
if km <=80:
    print('Tenha um bom dia dirija com segurança')
else:
    print('você foi mutado no valor de R${:.2f}!'.format(multa))

