vet = []
media = int(0)
soma = int(0)
qnt = int(0)
N = int(input("entre com a quantidade de alunos"))
for i in range(N):
    vet.append(int(input('Entre com a nota do  aluno: ')))
    soma = soma+vet[i]
media = soma/N
print("a media da classe é ", media)
for i in range(N):
    if(vet[i]>media):
        qnt=qnt+1
print("a quantidade de notas acima da média são ", qnt)

