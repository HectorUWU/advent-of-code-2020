import numpy as np

archivo = open("lista dia 1.txt","r")
lista = archivo.readlines()
for i in range(len(lista)):
    lista[i]=(int)(lista[i].replace("\n",""))
lista = np.asarray(lista)
for element in lista:
    for aux in lista:
        for element2 in lista:
            if(element+aux+element2==2020):
                print(element*aux*element2)  