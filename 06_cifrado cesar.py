mi=""#mensaje   ingresado
cc=0#clave de cifrado 
mc=""#mensaje cifrado
abc="abcdefghijklmnñopqrstuvwxyz"
pla=""#posicion de la letra en el alfabeto
md=""#mensaje decifrado
cd=0#clave de decifrado

mi=input("ingrese el mensaje a cifrar: ")
print()

cc=(int(input("ingrese el dezplazamiento del mensaje a cifrar: ")))
if (cc>27):
    print("error ingrese un desplazamiento entre 1 y 27")

for i in(mi.lower()):
    if(i in abc):
        pla=abc.find(i)
        pla=pla+cc

        if(pla>=27):
            pla=pla-27
        mc=mc+abc[pla]
        
print()
print("el mensaje cifrado es: ",mc)

print()

mc=input("ingrese el mensaje que quiere decifrar: ")
print()
cd=int(input("ingrese el desplazamiento del mensaje a decifrar: "))

if (cd>27):
    print("error ingrese un desplazamiento entre 1 y 27")

for j in (mc.lower()):
    if(j in abc):
        pla=abc.find(j)
        pla=pla-cd
        if(pla<0):
            pla=pla+27

        md=md+abc[pla]
print()
print("el menseje decifrado es: ",md)

        
    


        
            
            
    
