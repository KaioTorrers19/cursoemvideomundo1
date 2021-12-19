salario = float(input('qual é o valor do seu salario?'))
if salario <=1250:
    n = salario + (salario * 15/100)
    print('o valor do seu salario com o aumento de 15% sera de R${}'.format(n))
if salario >1250:
    n2 = salario + (salario * 10 /100 )
    print('o valor do seu salario  com aumento de 10 % é de RS${}'.format(n2))