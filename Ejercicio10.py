archivo = open('paises.txt', 'r')
#Busque e imprima el pais de Venezuela y su capital
lista=[]
paises=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
  b=i.index(":")
  for x in range(b+2,len(i)):
    lista.append(i[x])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
for i in paises:
  if(i[0]=="V")and(i[1]=="e") and (i[2]=="n"):
    print(i)
for i in ciudad:
   if(i[0]=="C") and (i[1]=="a") and (i[2]=="r")and (i[3]=="a"):
    print(i)
archivo.close()