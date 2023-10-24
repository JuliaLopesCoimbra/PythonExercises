num = int(input("Digite um número"))
chute = int(input("Digite um número que vc acha que é "))
if(chute+1== num or chute+2== num or chute+3== num or chute+4== num or chute+5== num or chute-1== num or chute-2== num or chute-3== num or chute-4== num or chute-5 == num or chute == num):
    print("chute baixo")
else:
    print("chute alto")
while chute !=num:
    chute = int(input("Digite um número"))
    if(chute+1== num or chute+2== num or chute+3== num or chute+4== num or chute+5== num or chute-1== num or chute-2== num or chute-3== num or chute-4== num or chute-5 == num or chute == num):
        print("chute baixo")
    else:
        print("chute alto")

print("Acertou!")
