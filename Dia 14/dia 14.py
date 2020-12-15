from itertools import product
dataset = []
with open("input.txt", "r") as f:
        for line in f.readlines():
            tmp = line.strip().split(" = ")
            if tmp[0] == "mask":
                dataset.append(["mask", list(tmp[1])])
            else:
                mem_address = int(tmp[0][tmp[0].index("[") + 1: -1])
                dataset.append([mem_address, int(tmp[1])])

memory = {}
mask = ["X" for _ in range(36)]
for instruccion, numero in dataset:
    if(instruccion == "mask"):
        mask = numero 
    else:
        binario = list(format(numero, "036b"))
        for i, bit in enumerate(mask):
            if(bit != "X"):
                binario[i] = bit
        memory[instruccion] = int("".join(binario), 2)
res = 0
for item in memory.items():
    res += item[1]
print(res)

memory = {}
mask = ["X" for _ in range(36)]
for instruccion, numero in dataset:
    if(instruccion == "mask"):
        mask = numero 
    else:
        binario = list(format(instruccion, "036b"))
        for i, bit in enumerate(mask):
            if(bit!="0"):
                binario[i]=bit
            direccion = binario
        direcciones = []
        numero_X = direccion.count("X")
        indices = [indice for indice, x in enumerate(direccion) if(x=="X")]
        for combinaciones in product("01", repeat=numero_X):
            nueva_direccion = direccion
            for i, combi in enumerate(combinaciones):
                nueva_direccion[indices[i]]= combi
            direcciones.append(int("".join(nueva_direccion),2))
        for direccion in direcciones:
            memory[direccion]=numero
res=0
for item in memory.items():
    res+=item[1]
print(res)