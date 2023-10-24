from random import randint

def soma(vet):
    soma = int(0)
    for i in range(0,len(vet)):
        soma = soma+vet[i]
    return soma

vet = []
for i in range(5):
    vet.append(randint(1,100))
    print(vet[i])

resp = soma(vet)
print("a soma dos números é",resp)
