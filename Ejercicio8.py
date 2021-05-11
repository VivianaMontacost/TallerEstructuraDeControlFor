archivo = open('paises.txt', 'r')
#Cuente e imprima cuantos paises que hay en el archivo
lista=[]
cont=0
for i in archivo:
  cont+=1
print(cont) 
archivo.close()