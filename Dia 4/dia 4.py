import string 
def ishexdigit( char ):
    result = ( char in string.hexdigits )
    return result
def ishexstring( str ):
    resultmap = map( ishexdigit, str )
    result = ( False not in resultmap )
    return result
def ver(hexa):
    if(hexa[0]=="#"):
        return ishexstring(hexa[1:])

def heigt(hgt):
    try:
        if(hgt[-2:]=="cm"):
            value = int(hgt[:3])
            if(value<=193 and value>=150):
                return True
            else:
                return False
        elif(hgt[-2:]=="in"):
            value = int(hgt[:2])
            if(value<=76 and value>=59):
                return True
            else:
                return False
        else:
            return False
    except(ValueError):
        return False


if __name__ == "__main__":   
    archivo = open("pasaportes.txt","r")
    lista = archivo.read()
    archivo.close()
    
    lista = lista.split("\n")
    lista.append("")
    new_list=[]
    aux=""
    for element in lista:
        if (element != ''):
            aux+=element
            aux+=" "
        elif(element==lista[len(lista)-1]):
            new_list.append(aux)
            aux=""
    
    print(new_list[0].split(" "))
    
    listadef=[]
    for element in new_list:
        dic = {}
        aux = element.split(" ")
        aux.pop()
        for i in range(len(aux)):
            dic[aux[i][:3]]=aux[i][4:]
        listadef.append(dic)
    i=0
    for element in listadef:
        try:
            if(element['ecl']=="amb" or element['ecl']=="blu" or element['ecl']=="brn" or element['ecl']=="gry" or element['ecl']=="grn" or element['ecl']=="hzl" or element['ecl']=="oth"):
                if(len(element['pid'])==9):
                    if((len(element['eyr'])==4) and (int(element['eyr'])>=2020) and (int(element['eyr'])<=2030)):
                        if(ver(element['hcl'])):
                            if((len(element['byr'])==4) and (int(element['byr'])>=1920) and (int(element['byr'])<=2002)):
                                if((len(element['iyr'])==4) and (int(element['iyr'])>=2010) and (int(element['iyr'])<=2020)):
                                    if(heigt(element['hgt'])):
                                        i+=1
        except(KeyError):
            pass    
    print(i)
            