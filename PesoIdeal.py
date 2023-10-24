sexo = input('Digite F para sexo feminino ou M para sexo masculino: ')
altura = float(input('Digite a altura: '))
if sexo == "F":
     calc = float((72.7 * altura) - 58)
     print("o peso ideal feminino de acordo com a altura digitada é ", calc)
elif sexo == "M":
    calc = float((62.1 * altura) - 44.7)
    print("o peso ideal masculino de acordo com a altura digitada é ", calc)
else:
    print("vc digitou errado")