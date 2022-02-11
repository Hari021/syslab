from gettext import find


w=open('sys3.txt','r').read()
q=g=w.splitlines()

name,para,fun,var=[],[],[],{}

for line in g:
    if '#define' in line:
        if '(' in line:
            g=line.replace('#define','').replace(' ','').replace(';','')
            name.append(g[:g.find('(')])
            fun.append(g[g.find('{')+1:g.find('}')])
            para.append(dict([(x,'') for x in g[g.find('(')+1:g.find(')')].replace(' ','').split(',')]))
        else:
            g.line.replace('#define','').replace(';','').split()
            var.update({g[0]:g[1]})
    
    else:
        fn=line[:line.find('(')]
        if fn in name:
            for v1,v2 in zip(para[name.index(fn)],line[line.find('(')+1:line.find(')')].replace(' ','').split(',')):
                para[name.index(fn)][v1]=v2

            for word in fun[name.index(fn)]:
                if word in para[name.index(fn)]:
                    fun[name.index(fn)]=fun[name.index(fn)].replace(word,para[name.index(fn)][word])

for line in q:
    if '#define' in line:
        continue
    else:
        if line[:line.find('(')] in name:
            print(fun[0].split('(')[2])
        else:
            for val in var:
                line=line.replace(val,var[val])
            print(line)