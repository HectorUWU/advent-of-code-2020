cargadores = []
archivo = open("input.txt","r")
for line in archivo.readlines():
    cargadores.append(int(line.strip()))
cargadores.append(max(cargadores)+3)
cargadores = sorted(cargadores)
diferencias = ""
ultimo_voltaje = 0


    
for cargador in cargadores: 
    diferencia = cargador - ultimo_voltaje 
    diferencias +=str(diferencia)
    ultimo_voltaje = cargador

print(diferencias.count('1')*diferencias.count('3'))


diferencias = diferencias.split("3")
print(diferencias)


print(2**diferencias.count('11')*4**diferencias.count('111')*7**diferencias.count('1111'))
