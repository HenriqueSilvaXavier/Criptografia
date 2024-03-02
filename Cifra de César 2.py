alfa=["a", "b", "c", "d", "e" ,"f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nome2=[]
nome=input("Digite o nome: ")
nome=nome.lower()
for n in range(0, len(nome)):
	nome2.append(nome[n])
for n in range(0, len(nome2)):
	if nome2[n]!=" ":
		c=alfa.index(nome2[n])
		if c<=22:
			nome2[n]=alfa[c+3]
		elif c>22:
			c=c-23
			nome2[n]=alfa[c]
	else:
		nome2[n]=" "
nome=""
for n in nome2:
	nome="{}{}".format(nome, n)
print(nome.title())