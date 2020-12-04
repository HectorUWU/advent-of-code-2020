import numpy as np

def hacer_camino(movx,movy,lista):
    x=0
    y=0
    arboles = 0
    try:
        for i in range(len(lista)):
            x+=movx
            if(lista[i+movy][x]=="#"):
                arboles+=movy
            i+=movy
    except IndexError:
        pass
    return arboles

def hacer_camino_con2(movx,lista):
    x=0
    y=0
    arboles = 0
    try:
        for i in range(len(lista)):
          x+=movx
          y+=2
          if(lista[y][x]=="#"):
              arboles+=1
    except IndexError:
        pass
    return arboles
    
if __name__ == "__main__":   
    archivo = open("arboles.txt","r")
    lista = archivo.readlines()
    archivo.close()
    for i in range(len(lista)):
        lista[i]=lista[i].replace("\n","") 
        lista[i]=lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]+lista[i]

    print(len(lista))
    lista = np.asarray(lista)
    a=hacer_camino(1,1,lista)
    b=hacer_camino(3,1,lista)
    c=hacer_camino(5,1,lista)
    d=hacer_camino(7,1,lista)
    e=hacer_camino_con2(1,lista)
    print(a*b*c*d*e)
