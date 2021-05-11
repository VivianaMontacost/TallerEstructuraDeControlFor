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
archivo.close()