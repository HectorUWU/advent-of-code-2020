from itertools import combinations

numeros = []
archivo = open("Xmas.txt","r")
for line in archivo.readlines():
    numeros.append(int(line))

for i,n in(enumerate(numeros[25:])):
    posiblesValores =[sum(grupo) for grupo in combinations(numeros[i:i+25],2)]
    if(n not in posiblesValores):
        invalido = n
        
print(type(numeros))
for i in range(len(numeros)):
    for j in range(i+1, len(numeros)):
        if(sum(numeros[i:j])==invalido):
            print(min(numeros[i:j])+max(numeros[i:j]))
