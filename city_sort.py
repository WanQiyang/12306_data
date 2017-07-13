#coding=utf-8

data=[]

fp=open("./city_require.txt", "r", encoding="utf-8")
for line in fp:
    line=line.strip()
    if line=="": continue
    data.append(line.encode("GB18030"))
fp.close()

data.sort()

fp=open("./city_sorted.txt", "w", encoding="utf-8")
for each in data:
    if data=="": continue
    fp.write(each.decode("GB18030")+'\n')
fp.close()
