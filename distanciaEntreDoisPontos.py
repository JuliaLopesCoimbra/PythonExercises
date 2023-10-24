import math
xa = int(input("Digite o x do primeiro ponto"))
ya = int(input("Digite o y do primeiro ponto"))
xb = int(input("Digite o x do segundo ponto"))2
yb = int(input("Digite o y do segundo ponto"))

dist = int(((xb-xa)**2)+((yb-ya)**2))
result = math.sqrt(dist)
print(f"a distancia entre os pontos é: {result}")