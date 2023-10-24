minutos = int(10)
segundos = int(59)
print("10:00")
for minutos in range(9,-1,-1):
    for segundos in range(59,-1,-1):
        print(minutos,":",segundos)
        if(segundos == 0):
            minutos -=minutos

