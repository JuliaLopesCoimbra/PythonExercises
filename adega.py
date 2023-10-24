acmT = int(0)
acmB = int(0)
acmR = int(0)
acm = int(0)
porcT = int(0)
porcB = int(0)
porcR = int(0)
opcao = input("Digite o tipo de vinho 'T' para tinto, 'B' para branco, 'R' para rose ou F para finalizar")
if(opcao == "T"):
    acmT = acmT+1
if (opcao == "B"):
    acmB = acmB + 1
if (opcao == "R"):
    acmR = acmR + 1
acm = acm+1
while opcao != "F":
    opcao = input("Digite o tipo de vinho ou F para finalizar")
    if(opcao == "T"):
        acmT = acmT+1
    if (opcao == "B"):
        acmB = acmB + 1
    if (opcao == "R"):
        acmR = acmR + 1
    acm = acm+1
porcT = (acmT*100)/acm
porcB = (acmB*100)/acm
porcR = (acmR*100)/acm
print("A porcentagem do tipo Tinto sobre o total de vinho é", porcT, "%")
print("A porcentagem do tipo Branco sobre o total de vinho é", porcB, "%")
print("A porcentagem do tipo Rose sobre o total de vinho é", porcR, "%")