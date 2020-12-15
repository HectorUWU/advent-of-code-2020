import operator
with open("input.txt","r") as f:
        lines = f.readlines()
        time = int(lines[0].rstrip())
        dataset = lines[1].strip().split(",")


times = {}
for element in dataset:
    if(element!='x'):
        times[element]=int(element)
        while(times[element]<time):
            times[element]+=int(element)
        times[element]-=time

times = sorted(times.items(),
               key=operator.itemgetter(1))
'''
for item in times:
    print(int(item[0])*(item[1]))
'''
#parte 2    
new_data = [(i, int(element)) for i,element in enumerate(dataset) if(element!='x')]   
salto = new_data[0][1]
tiempo_ocurrido = 0
for delta, bus_id in new_data[1:]:
        while (tiempo_ocurrido + delta) % bus_id != 0:
            tiempo_ocurrido += salto
        salto *= bus_id
print(tiempo_ocurrido)