import json
f=open('./data2.txt','r',encoding="utf-8")
dic={'list':[]}
lstArr=[]
line=True
with open('./data2.json','w',encoding='utf-8') as d:
  while line:
    line=f.readline()
    lst=line.split(',')
    if len(lst)<6:
      continue
    lst[0]=lst[0][0:4]+'/'+lst[0][4:6]+'/'+lst[0][6:8]
    lst[6]=lst[6][:-1]
    lstArr.append(lst)
  dic['list']=lstArr
  json.dump(dic,d)