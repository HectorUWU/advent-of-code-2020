dataset = []
with open("input.txt","r") as f:
    for line in f.readlines():
        tmp = line.rstrip()
        dataset.append((tmp[0], int(tmp[1:])))

cordenadas = {'N':0, 'E':0, 'S':0, 'W':0}
direcciones = ["N","E","S","W"]
dirMirando =1
nueva_direccion=direcciones[dirMirando]
for direccion, numero in dataset:
    if(direccion=="F"):
        cordenadas[nueva_direccion]+=numero
    elif(direccion in ["L","R"]):
        if(direccion=="L"):
            numero= 360 - numero
        dirMirando += (numero//90)
        dirMirando %= 4
        nueva_direccion=direcciones[dirMirando]
    else:
        cordenadas[direccion] +=numero
        
print(abs(cordenadas["N"]-cordenadas["S"]) + abs(cordenadas["E"]-cordenadas["W"]))

wx,wy= 10,1
x=y=0
cordenadas = {'N':1, 'E':1, 'S':-1, 'W':-1}
for direccion, numero in dataset:
    if(direccion == "N" or direccion =="S"):
        wy += numero*cordenadas[direccion]
    if(direccion == "E" or direccion =="W"):
        wx += numero*cordenadas[direccion]
    elif(direccion == "F"):
            x += wx * numero
            y += wy * numero
    elif(direccion=="R" or direccion== "L"):
        for a in range(numero//90):
            if(direccion=="R"):
                wx,wy= wy,-wx
            else:
                wx, wy = -wy, wx
print(abs(x)+abs(y))
        