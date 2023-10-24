tipo = input('Digite o tipo de combustível A-álcool, G-gasolina ')
litro = float(input('Digite a quantidade de litros: '))
if tipo == "A":
    if litro <= 20:
        calc = float(litro*2.10*0.03)
        print("O preço do alcool com 3% de desconto para cada litro de ", litro, " litros colocados ficou ", calc)
    elif litro > 20:
        calc = float(litro * 2.10 * 0.05)
        print("O preço do alcool com 5% de desconto para cada litro de ", litro, " litros colocados ficou ", calc)
elif tipo == "G":
    if litro <= 20.00:
        calc = float(litro * 3.30 * 0.04)
        print("O preço da gasolina com 4% de desconto para cada litro de ", litro, " litros colocados ficou ", calc)
    elif litro > 20:
        calc = float(litro * 3.30 * 0.06)
        print("O preço da gasolina com 6% de desconto para cada litro de ", litro, " litros colocados ficou ", calc)
else:
    print("vc digitou errado")