num = int(1)
soma = int(0)
for num in range(1,500, 1):
    if num%2!=0 and num%3==0:
        soma+=num
print("a soma dos numeros impares e multiplos de 3 do intervalo de 1 a 500 é", soma)