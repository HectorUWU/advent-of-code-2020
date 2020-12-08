archivo = open("instruciones.txt","r")
lista = archivo.readlines()
archivo.close()

archivo = []
pila = []
acumulador=0
instrucciones = []
for jump in range(len(lista)):
    print
    pila = []
    archivo = open("instruciones.txt","r")
    lista = archivo.readlines()
    archivo.close()
    listaaux=lista
    inst,n = listaaux[jump].split(" ")
    if(inst=="jmp"):
        listaaux[jump] = ("nop "+n)
        i=0
        acumulador=0
        for j in range(10000000):
            instruccion,num = listaaux[i].split(" ")
            if(instruccion == "acc"):
                acumulador+=int(num)
                i+=1
            elif(instruccion == "jmp"):
                i+=int(num)
            elif(instruccion == "nop"):
                i+=1
            if(i in pila):
                break
            elif(i==(len(lista))):
                print(acumulador)
                break
            else:
                 pila.append(i)

print("sali")
