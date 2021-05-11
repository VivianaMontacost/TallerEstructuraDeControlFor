archivo = open('paises.txt', 'r')
#imprima la posicion de colombia
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)

#Imprima todos los paises

lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]

#Imprima todas las Capitales

lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
  
#Imprimir todos los paises que inicien con la letra C

lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
  
#imprima todas las capitales que inicien con la leta B

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
  if(i[0]=="B"):
    print(i)  

#Cuente e imprima cuantas ciudades inician con la latra M
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
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U

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
  if(i[0]=="U"):
    print(i)
archivo = open('paises.txt', 'r')
lista2=[]
pais=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista2.append(i[r])
  a="".join(lista2)
  pais.append(a)
  lista2=[]
for i in pais:
  if(i[0]=="U"):
    print(i)

#Cuente e imprima cuantos paises que hay en el archivo
P=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  P=P+1 
  if(a=="Paises\n"):
    break
  lista=[]   
print(P)

#Busque e imprima la ciudad de Singapur
 
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Singapur: Singapur\n"):
    break
  lista=[]   
print(a)

#Busque e imprima el pais de Venezuela y su capital

lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Venezuela: Caracas\n"):
    break
  lista=[]   
print(a)

#Cuente e imprima las ciudades que su pais inicie con la letra E

#Buesque e imprima la Capiltal de Colombia
archivo = open('paises.txt', 'r')
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(a)

#imprima la posicion del pais de Uganda
Uga=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  Uga=Uga+1 
  if(a=="Uganda: Kampala\n"):
    break
  lista=[]   
print(Uga)

#imprima la posicion del pais de Mexico
M=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  M=M+1 
  if(a=="México: Ciudad de México \n"):
    break
  lista=[]   
print(M)


#Agregue un país que no esté en la lista 
#H
archivo.close()