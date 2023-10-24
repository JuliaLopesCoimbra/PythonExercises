vet = []
vet2 = []
vet3 = []
for i in range(5):
    vet.append(int(input('Entre com um número do primeiro vetor: ')))
for i in range(5):
    vet2.append(int(input('Entre com um número do segundo vetor: ')))
for i in range(5):
    vet3.append(vet[i]+vet2[i])
print(vet3)