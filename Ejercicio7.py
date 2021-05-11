archivo = open('paises.txt', 'r')
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U

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
  for q in range(b+2,len(i)):
    lista.append(i[q])
  b="".join(lista)
  ciudad.append(b)
  lista=[]
for i in paises:
  if(i[0]=="U"):
    print(i)
for i in ciudad:
   if(i[0]=="U"):
    print(i)
archivo.close()