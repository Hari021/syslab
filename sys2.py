words = []
ans=[]

keywords = ["int", "float", "long", "short", "String","char","double"]

with open("sys2.txt", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		words.append(word)
for i in words:
        if "(" in i:
                value=i[i.index("(")-1]
                retype=i[0]
                typar=''
                count=0
                for j in i[i.index("(")+1:i.index(")")]:
                        if j in keywords:
                                count+=1
                                typar+=j+", "
                typar=typar[:-2]
                ans.append({'id':value,'dtype':'','retype':retype,'iv':'','no':count,'typa':typar})
        else:
                dtype=i[0]
                i.pop(0)
                id=''
                iv=0
                for j in range(i.count(',')+1):
                        if i.count(',')!=0:
                                k=i[:i.index(",")]
                                i.remove(',')
                                value=k[0]
                                iv=''
                                if "=" in k:
                                        if dtype == 'char' or dtype == 'string':
                                                iv=k.index("=")+2
                                        else:
                                                iv=k.index("=")+1
                                        ans.append({'id':value,'dtype':dtype,'retype':'','iv':iv,'no':'','typa':''})
                                else:
                                        ans.append({'id':value,'dtype':dtype,'retype':'','iv':iv,'no':'','typa':''})
                        else:
                                k=i[:i.index(";")]
                                i.remove(';')
                                value=k[0]
                                iv=''
                                if "=" in k:
                                        if dtype == 'char' or dtype == 'string':
                                                iv=k.index("=")+2
                                        else:
                                                iv=k.index("=")+1
                                        ans.append({'id':value,'dtype':dtype,'retype':'','iv':iv,'no':'','typa':''})
                                else:
                                        ans.append({'id':value,'dtype':dtype,'retype':'','iv':iv,'no':'','typa':''})
                        for l in k:
                                i.remove(l)
                                        
print("id \t data type \t return type \t initial value \t no of parameters \t type of parameter")
for i in ans:
        print("{} \t {} \t\t {} \t\t {} \t\t {} \t\t {}".format(i['id'],i['dtype'],i['retype'],i['iv'],i['no'],i['typa']))