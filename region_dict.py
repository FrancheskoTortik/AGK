region_dick = {}
with open('reg.txt', 'r', encoding='UTF-8') as file:
    for i in file.readlines():
        region_dick[int(i.split()[0])] = i.split()[1]
        #print(i.split()[1])
print(region_dick)