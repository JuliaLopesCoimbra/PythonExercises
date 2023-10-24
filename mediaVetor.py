from random import randint

def soma(vet):
    soma = int(0)
    for i in range(0,len(vet)):
        soma = soma+vet[i]
    return soma

def media(vet):
    cont = int(0)
    a = int(0)
    for i in range(0,len(vet)):
        cont = cont+1
    somar = soma(vet)
    media = somar/cont
    return media

vet = []
for i in range(5):
    vet.append(randint(1,100))
    print(vet[i])

resp = soma(vet)
resp1 = media(vet)
print("a soma dos números é",resp)
print("a media do vetor é",resp1)