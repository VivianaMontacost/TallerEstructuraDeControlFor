archivo = open('paises.txt', 'r')
#Busque e imprima la ciudad de Singapur
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
  if(i[0]=="S") and (i[1]=="i"):
    print(i)
archivo.close()