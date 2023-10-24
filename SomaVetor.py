vet = []
soma = int(0)
N = int(input("entre com o tamanho do vetor"))
for i in range(N):
    vet.append(int(input('Entre com um número: ')))
    soma = soma+vet[i]
print("a soma dos elementos do vetor é ", soma)
