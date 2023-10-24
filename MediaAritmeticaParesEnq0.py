soma = int(0)
acm = int(0)
num = int(input("Digite um número"))
while num!=0:
    num = int(input("Digite um número"))
    if num%2==0:
        soma = soma + num
        acm=acm+1
print(" a média dos pares é ", soma/acm)