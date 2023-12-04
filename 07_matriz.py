matriz=[]
filas=4
columnas=4
n=0
sd=0
md=1
scd=0
mcd=1

for f in range(filas):
    vf=[]
    for c in range(columnas):
        n=n+1
        vf.append(n)
    matriz.append(vf)
        
            
print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}\n{matriz[3]}")

for  f in range(filas):
    for c in range(columnas):
        if(f==c):
            sd=sd+matriz[f][c]
            md=md*matriz[f][c]

        if(f+c==filas-1):
            scd=scd+matriz[f][c]
            mcd=mcd*matriz[f][c]
            
print("la suma de la diagonal de la matriz es: ",sd)
print("la multiplicacion de la diagonal de la matriz es: ",md)
print()

print("la suma de la contra diagonal de la matriz es: ",scd)
print("la multiplicacion de la contra diagonal es: ",mcd)

