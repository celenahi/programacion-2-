matriz=[]
mv=[]#matirz volteada
filas=6
columnas=6
n=0

for f in range(filas):
    fil=[]
    for c in range(columnas):
        n=n+1
        fil.append(n)
    matriz.append(fil)
print("MATRIZ ORIGINAL")    
print()
print(f"{matriz[0]}\n{matriz[1]}\n{matriz[2]}\n{matriz[3]}\n{matriz[4]}\n{matriz[5]}")

mv=[filas[::-1]for filas in matriz]

print()
print("MATRIZ VOLTEADA")
print()    
print(f"´{mv[0]}\n{mv[1]}\n{mv[2]}\n{mv[3]}\n{mv[4]}\n{mv[5]}")
            
        
