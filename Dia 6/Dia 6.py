archivo = open("aduanas.txt","r")
lista = archivo.readlines()
archivo.close()
#primera parte 
'''
lista = lista.split("\n")

lista.append("")
new_list=[]
aux=""
for element in lista:
    if (element != ''):
        aux+=element
    elif(element==lista[len(lista)-1]):
        new_list.append(aux)
        aux=""
res = 0
#primera parte
for group in new_list:
    aux=(group)
    print(aux)
    res+=len(set(aux))

print(res)
'''
lista.append("\n")
listaGlobal=[]
aux=[]
for line in lista:
    if(line!='\n'):
        aux.append(line.replace('\n',''))
    else: 
        listaGlobal.append(aux)
        aux=[]
res=0
for group in listaGlobal:
    aux=""
    for person in group:
        aux+=person
    aux = set(aux)
    for letter in aux:
        intaux=0
        for person in group:
            #print(person)
            if(letter in person):
                intaux+=1
        if(intaux==len(group)):
            res+=1
print(res)
        
    