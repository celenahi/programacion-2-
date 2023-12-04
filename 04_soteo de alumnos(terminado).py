import random
cn=0#cantidad de nombres
ni=0#nombres ingresados
x=0
ln=[]#lista de nombres ingresados
lnn=[]#lista nueva de nom bres
na=""#nombres aleatorios
cv=0#cantidad de vueltas
i=0


cn=(int(input("ingrese la cantidad de nombres que desea sortear")))

for x in range(cn):
    print("ingrese el nombre numero ",x+1)
    ni=(input())
    ln.append(ni)
print("lista de nombres:")
for i in range(cn):
    print(i,")",ln[i])

while (cv !=cn  ):
      na=random.choice(ln)
      if (na in lnn):
          print(" ")
      else:
          lnn.append(na)
          cv=cv+1

print("lista de nombres sorteados: ")
for t in range(cn):
    print(t,")",lnn[t])








