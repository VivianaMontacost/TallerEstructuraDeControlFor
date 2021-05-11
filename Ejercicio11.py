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