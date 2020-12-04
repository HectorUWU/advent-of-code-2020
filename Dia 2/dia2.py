archivo = open("lista 2.txt","r")
lista = archivo.readlines()
archivo.close()
for i in range(len(lista)):
    lista[i]=(lista[i].replace("\n",""))
    lista[i]=(lista[i].replace("-"," "))
    lista[i]=(lista[i].replace(":",""))
    lista[i]=lista[i].split(" ")
print(lista)
i=0
for element in lista:
    try:
        if((element[-1][int((element[0]))-1])==element[-2]):
            if((element[-1][int((element[1]))-1])!=element[-2]):
                i+=1
        elif((element[-1][int((element[1]))-1])==element[-2]):
            if((element[-1][int((element[0]))-1])!=element[-2]):
                i+=1
    except(IndexError):
        pass
print(i)