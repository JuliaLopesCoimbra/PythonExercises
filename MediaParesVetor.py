vet = []
soma = int(0)
qnt = int(0)
N = int(input("entre com o tamanho do vetor"))
for i in range(N):
    vet.append(int(input('Entre com um número: ')))
    if(vet[i]%2==0):
        soma = soma+vet[i]
        qnt = qnt+1
print("a media dos elementos pares do vetor é ", soma/qnt)