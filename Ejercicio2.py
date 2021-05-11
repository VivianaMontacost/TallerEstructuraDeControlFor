archivo = open('paises.txt', 'r')
#Imprima todos los paises
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
archivo.close()