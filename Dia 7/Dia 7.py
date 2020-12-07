def buscarBolsa(dic, bolsa_buscada):
    res=set()
    for bolsa, bolsaaux in dic.items():
        if(bolsa_buscada in bolsaaux.keys()):
            res.add(bolsa)
            res = res.union(buscarBolsa(dic,bolsa))
    return res

def calcularTotalBolsas(dic, bolsa_buscada):
    count=0
    bolsas_contenidas=dic[bolsa_buscada]
    for bolsa, num in bolsas_contenidas.items():
        count+= num + num*calcularTotalBolsas(dic,bolsa)
    return count

if __name__ == "__main__":
    archivo = open("bolsa.txt","r")
    lista = archivo.readlines()
    archivo.close()
    dic={}
    for line in lista:
        bolsa, bolsas_contendias_str = line.split("contain")
        bolsa = bolsa.strip().rstrip("s")
        bolsas_contenidas=[bolsaaux.strip().strip(".").strip("s") for bolsaaux in bolsas_contendias_str.split(",")]
        if("no other bag" in bolsas_contenidas):
            bolsas_contenidas={}
        else:
            bolsas_contenidas={bolsaaux[2:]: int(bolsaaux[0]) for bolsaaux in bolsas_contenidas}
        dic[bolsa]=bolsas_contenidas
    print((buscarBolsa(dic,"shiny gold bag")))
    print(calcularTotalBolsas(dic,"shiny gold bag"))