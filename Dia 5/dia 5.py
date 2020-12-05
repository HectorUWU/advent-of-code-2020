import numpy as np
archivo = open("asientos.txt","r")
lista = archivo.readlines()
archivo.close()

for i in range(len(lista)):
    lista[i]=lista[i].replace("F","0").replace("B","1").replace("L","0").replace("R","1").replace("\n","")
    
arr = []
for element in lista:
    aux = str(element[:7])
    aux2 = str(element[7:])
    arr.append((int(aux,2)*8)+int(aux2,2))
arr = np.array(arr)



#Segunda parte
maximo = np.amax(arr)
minimo = np.amin(arr)
arr = set(arr)

for element in arr:
    if(element==minimo):
        minimo+=1
    else: 
        print(minimo)
        minimo+=2