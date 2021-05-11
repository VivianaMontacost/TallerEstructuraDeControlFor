archivo = open('paises.txt', 'r')
#Cuente e imprima cuantas capitales inician con la latra M
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="M"):
    print(i)
archivo.close()