num1 = int(input("digite o primeiro lado do triangulo "))
num2 = int(input("digite o segundo lado do triangulo "))
num3 = int(input("digite o terceiro lado do triangulo "))
if num3<num1+num2 and num2<num1+num3 and num1<num2+num3:
    if num3==num2 and num3==num1:
        print("Triângulo Equilátero")
    if num3==num2 or num3==num1 or num1==num2 or num2==num1:
        print("Triângulo Isósceles")
    if num1 != num2 and num2 !=num3:
        print("Triângulo Escaleno")
else:
    print("Não é um Triângulo")