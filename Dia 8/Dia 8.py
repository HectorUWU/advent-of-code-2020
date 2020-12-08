archivo = open("instruccion.txt","r")
lista = archivo.readlines()
archivo.close()
archivo = []
pila = []
acumulador=0
i=0
for j in range(10000000):
    instruccion,num = lista[i].split(" ")
    if(instruccion == "acc"):
        acumulador+=int(num)
        i+=1
    elif(instruccion == "jmp"):
        i+=int(num)
    elif(instruccion == "nop"):
        i+=1
    if(i in pila):
        print(acumulador)
        break
    else: 
         pila.append(i)


print("sali")