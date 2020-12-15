def checkAsientos(asientos):
    new_asientos=[]
    cambios = 0 
    for i, fila in(enumerate(asientos)):
        new_fila=[]
        for j, asiento in(enumerate(fila)):
            contador = 0
            if(fila[j]=="#"):
                try:
                    if(j+1<len(fila)):
                        if(fila[j+1]=="#"):
                            contador+=1
                        if(i-1>=0):
                            if(asientos[i-1][j+1]=="#"):
                                contador+=1
                        if(i+1<len(asientos)):
                            if(asientos[i+1][j+1]=="#"):
                                contador+=1
                    if((j-1)>=0 and fila[j-1]=="#"):
                        contador+=1
                    if(i-1>=0):
                        if(asientos[i-1][j]=="#"):
                            contador+=1
                        if(j-1>=0 and asientos[i-1][j-1]=="#"):
                            contador+=1
                    if(i+1<len(asientos)):
                        if(asientos[i+1][j]=="#"):
                                contador+=1
                        if(j-1>=0 and asientos[i+1][j-1]=="#"):
                                contador+=1
                    if(contador>=4):
                        new_fila.append("L")
                        cambios+=1
                    else:
                        new_fila.append("#")
                except(IndexError):
                    if(contador>=4):
                        new_fila.append("L")
                        cambios+=1
                    else:
                        new_fila.append("#")
            else:
                new_fila.append(fila[j])
        new_asientos.append(new_fila)
    return new_asientos, cambios
    
def sentarGente(asientos):
        new_asientos=[]
        cambios = 0 
        for i, fila in(enumerate(asientos)):
            new_fila=[]
            for j, asiento in(enumerate(fila)):
                contador = 0
                if(fila[j]=="L"):
                    try: 
                        if(j+1<len(fila)):
                            if(fila[j+1]=="#"):
                                contador+=1
                            if(i-1>=0):
                                if(asientos[i-1][j+1]=="#"):
                                    contador+=1
                            if(i+1<len(asientos)):
                                if(asientos[i+1][j+1]=="#"):
                                    contador+=1
                        if((j-1)>=0 and fila[j-1]=="#"):
                            contador+=1
                        if(i-1>=0):
                            if(asientos[i-1][j]=="#"):
                                contador+=1
                            if(j-1>=0 and asientos[i-1][j-1]=="#"):
                                contador+=1
                        if(i+1<len(asientos)):
                            if(asientos[i+1][j]=="#"):
                                    contador+=1
                            if(j-1>=0 and asientos[i+1][j-1]=="#"):
                                    contador+=1
                        if(contador==0):
                            new_fila.append("#")
                            cambios+=1
                        else:
                            new_fila.append("L")
                    except(IndexError):
                        if(contador==0):
                            new_fila.append("#")
                            cambios+=1
                        else:
                            new_fila.append("L")
                else:
                    new_fila.append(fila[j])
            new_asientos.append(new_fila)
        return new_asientos

def part2(i, j, asientos):
    ocupado = 0
    for ki in range(1, i+1):
        if asientos[i-ki][j] == 'L':
            break
        elif asientos[i-ki][j] == '#':
            ocupado += 1
            break
    for ki in range(1, len(asientos)-i):
        if asientos[i+ki][j] == 'L':
            break
        elif asientos[i+ki][j] == '#':
            ocupado += 1
            break
    for kj in range(1, j+1):
        if asientos[i][j-kj] == 'L':
            break
        elif asientos[i][j-kj] == '#':
            ocupado += 1
            break
    for kj in range(1, len(asientos[i])-j):
        if asientos[i][j+kj] == 'L':
            break
        elif asientos[i][j+kj] == '#':
            ocupado += 1
            break    
    for kd in range(1, min(i+1, len(asientos[i])-j)):
        if asientos[i-kd][j+kd] == 'L':
            break
        elif asientos[i-kd][j+kd] == '#':
            ocupado += 1
            break
    for kd in range(1, min(i+1, j+1)):
        if asientos[i-kd][j-kd] == 'L':
            break
        elif asientos[i-kd][j-kd] == '#':
            ocupado += 1
            break
    for kd in range(1, min(len(asientos)-i, len(asientos[i])-j)):
        if asientos[i+kd][j+kd] == 'L':
            break
        elif asientos[i+kd][j+kd] == '#':
            ocupado += 1
            break
    for kd in range(1, min(len(asientos)-i, j+1)):
        if asientos[i+kd][j-kd] == 'L':
            break
        elif asientos[i+kd][j-kd] == '#':
            ocupado += 1
            break
    return ocupado
    
if __name__ == "__main__":  
    asientos=[]
    archivo = open("input.txt","r")
    for line in archivo.readlines():
        asientos.append(list(line.strip('\n')))
    archivo.close()

    #asientos,cont= checkAsientos(asientos)
    cont=1
    while(cont != 0):
         asientos = sentarGente(asientos)
         asientos,cont= checkAsientos(asientos)
    asientos = sentarGente(asientos)
    asientos,cont= checkAsientos(asientos)
    count = 0
    for fila in asientos:
        count+= fila.count("#")

    count=0
    for i, fila in enumerate(asientos):
        for j, asiento in enumerate(fila):
            count+=part2(i,j,asientos)
    print(count)