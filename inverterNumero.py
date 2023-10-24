num = int(input("Digite um número de 3 digitos para invertelo"))
centena = int(num/100)
dezena = int(num/10)
unidade = int((centena*100)+(dezena*10))-num
print(unidade, dezena, centena)