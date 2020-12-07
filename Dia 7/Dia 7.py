from re import sub

def leer_datos(fname):
    bag_map = {}
    with open(fname, "r") as file:
        for line in file.readlines():
            exterior, interior = line.split(" bags contain")
            arreglo_interior = interior.strip(" .\n").split(",")
            arreglo_interior = [sub("(bags|bag)+", "", s).strip().split(" ", 1) for s in arreglo_interior]
            bag_map[exterior] = arreglo_interior
    return bag_map

def encontrar_bolsas_contenedoras(bags, inner_bags):
    nombres = [i[1] for i in inner_bags]
    if "shiny gold" in nombres:
        return True
    elif not (len(nombres) == 1 and nombres[0] == "other"):
        total = False
        while not total:
            for _, nombre in inner_bags:
                total += encontrar_bolsas_contenedoras(bags, bags[nombre])
            break
        return total
    return False

def task_one(bags):
    return sum([bool(encontrar_bolsas_contenedoras(bags, bags[i])) for i in bags])

def count_sub_bags(bags, prev, inner_bags):
    names = [i[1] for i in inner_bags]
    if len(names) != 1 or names[0] != "other":
        total = 0
        for c, n in inner_bags:
            count = [int(b[0]) for b in bags[prev] if n == b[1]][0]
            more_bags = not (len(bags[n]) == 1 and bags[n][0][1] == "other")
            total += int(count) * more_bags + int(c) * count_sub_bags(bags, n, bags[n])
        return total
    else:
        return 1
def task_two(bags):
    return count_sub_bags(bags, "shiny gold", bags["shiny gold"])

if __name__ == "__main__":
    bags = leer_datos("bolsas.txt")
    print(f"Answer for Task One is {task_one(bags)}")
    print(f"Answer for Task Two is {task_two(bags)}")