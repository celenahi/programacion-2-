import random
ns=0#numero secreto
cv=0#cantidad de vidas
ni=0#numero ingresado
res=""#respuesta
print("Bienvenido al juego adivina el numero secreto")
res=input("ingrese en que nivel quiere jugar:(d=dificil,f=facil):")

if res=="f":
    ns=random.randint(1,20)
    print("este es el numero secreto: ",ns,"  (lo muestro para ver si el codigo funciona)")
    print("tiene 6 intentos en este nivel")
    cv=6
    while cv>0:
        ni=(int(input("adivina el numero")))
            
        if ni>ns:
            print("el numero ingresado es mayor al numero a adivinar")
            cv=cv-1
            print("le quedan ",cv,"vidas")
        
        elif ni<ns:
            print("el numero ingresado es menor al numero a adivinar")
            cv=cv-1
            print("le quedan ",cv,"vidas")

        elif ni==ns:
            print("felicitaciones adivinaste el numero")
            break
            
    if cv==0:
        print("perdiste")

elif res=="d":
    ns=random.randint(1,100)
    print("este es el numero secreto: ",ns,"  (lo muestro para ver si el codigo funciona)")
    print("tiene 7 intentos en este nivel")
    cv=7
    while cv>0:
        ni=(int(input("adivina el numero")))
            
        if ni>ns:
            print("el numero ingresado es mayor al numero a adivinar")
            cv=cv-1
            print("le quedan ",cv,"vidas")
        
        elif ni<ns:
            print("el numero ingresado es menor al numero a adivinar")
            cv=cv-1
            print("le quedan ",cv,"vidas")

        elif ni==ns:
            print("felicitaciones adivinaste el numero")
            break
            
    if cv==0:
        print("perdiste")
else:
    print("el nivel ingresado es invalido")
    
        
