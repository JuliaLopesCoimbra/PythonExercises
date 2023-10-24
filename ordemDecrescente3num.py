num1 = int(input("digite o primeiro número"))
num2 = int(input("digite o segundo número"))
num3 = int(input("digite o terceiro número"))
if num1 > num2 and num2>num3:
    print("Ordem decrescente: ", num1," ", num2," ", num3)
elif num1 > num2 and num3>num2:
    print("Ordem decrescente: ", num1, " ", num3, " ", num2)
elif num2 > num1 and num1>num3:
    print("Ordem decrescente: ", num2, " ", num1, " ", num3)
elif num2 > num3 and num3>num1:
    print("Ordem decrescente: ", num2, " ", num3, " ", num1)
elif num3 > num2 and num2>num1:
    print("Ordem decrescente: ", num3, " ", num2, " ", num1)
elif num3 > num1 and num1>num2:
    print("Ordem decrescente: ", num3, " ", num1, " ", num2)
if num1==num2==num3:
    print("os numeros sao iguais")
