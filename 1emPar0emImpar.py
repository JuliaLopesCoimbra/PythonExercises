vet = []
for i in range(100):
    vet.append(int(input('Entre com o número do vetor: ')))
for i in range(100):
    if(vet[i]%2==0):
        vet[i]=1
    else:
        vet[i]=0
for i in range(100):
 print(vet[i])
