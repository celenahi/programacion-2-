import random
cn=0#cantidad de nombres
ni=0#nombres ingresados
x=0
ln=[]#lista de nombres ingresados
sn=""
lnn=[]
cv=0



cn=(int(input("ingrese la cantidad de nombres que desea sortear")))

for x in range(cn):
    print("ingrese el nombre numero ",x+1)
    ni=(input())
    ln.append(ni)
print(ln)

        
    