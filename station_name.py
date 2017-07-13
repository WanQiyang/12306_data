#coding=utf-8

data=[]

fp=open("./station_name.txt","r",encoding="utf-8")
for line in fp:
    line=line.strip()
    if line=="": continue
    data=line.split('@')
fp.close()

for index, each in enumerate(data):
    if each=="": continue
    data[index]=each.split('|')

city=[]

city_require={}

fp=open("./city_sorted.txt","r",encoding="utf-8")
for line in fp:
    line=line.strip()
    if line=="": continue
    city.append(line)
fp.close()

for each in data:
    if each=="": continue
    for c in city:
        if each[1].find(c)!=-1:
            city_require[each[2]]=each[1]

output={}

for each in city:
    if each=="": continue
    output[each]=list()

for each in city_require:
    if each=="": continue
    for c in city:
        if city_require[each].find(c)!=-1:
            output[c].append(each)

for each in output.items():
    print(each)

fp=open("./city.txt","w",encoding="utf-8")
for each in city_require:
    if city_require[each] in city:
        fp.write(each+' '+city_require[each]+'\n')
fp.close()
