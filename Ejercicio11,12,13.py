archivo = open('paises.txt', 'r')

#Cuente e imprima las ciudades que su pais inicie con la letra E
lista=[]
paises=[]
ciudad=[]
otra=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,len(i)):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="E"):
    otra.append(i)
for i in otra:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
    print(i) 
ciudad.append(a)
print(len(ciudad))
archivo.close()

archivo = open('paises.txt', 'r')
#Busque e imprima la Capital de Colombia
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
  if(i[0]=="B") and (i[1]=="o") and (i[2]=="g"):
    print(i)
archivo.close()


archivo = open('paises.txt', 'r')
#imprima la posicion del pais de Uganda
archivo= open('paises.txt')
lista=[]
otra=[]
a=[]
cont=0
for i in archivo:
  a=i.index(":")
  cont+=1
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  #print(a)
  lista=[]
  otra.append(a)
a=otra.index('Uganda')
print(a)
archivo.close()