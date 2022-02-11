words=[]

keywords = ["int", "float", "long", "short", "String"]
punctutation = [",", ";"]
arithmetic = ["+", "-", "*", "/", "%"]
relational = [">", "<", ">=", "<=", "==", "!="]
assignment = ["=", "+=", "-=", "*=", "/=", "%="]
logical=["&&", "||", "!"]


with open("sys1.txt", "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		words.append(word)
for j in words:
    for i in j:
        if i in keywords:
            print("< {} , ".format(i),"keywords >")
        elif i in punctutation:
            print("< {} , ".format(i),"punchuations >")
        elif i in arithmetic:
            print("< {} , ".format(i),"arithemetic operators >")
        elif i in relational:
            print("< {} , ".format(i),"relational operators >")
        elif i in assignment:
            print("< {} , ".format(i),"assignment operators >")
        elif i in logical:
            print("< {} , ".format(i),"logical operators >")
        elif i.isnumeric():
            print("< {} , ".format(i),"number >")
        elif i[0].isalpha():
            print("< {} , ".format(i),"variable name >")
