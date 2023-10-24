def menor(a,b):
    if(a==b):
        return "iguais"
    if(a<b):
        return a
    else:
        return b

x = int(input("digite o primeiro número"))
y = int(input("digite o segundo número"))

resp = (menor(x,y))
if(resp == "iguais"):
    print("são iguais")
if(resp == x):
    print(x," é o menor")
if(resp == y):
    print(y," é o menor")