import random
ns=0#numero secreto
cv=6#cantidad de vidas
ni=0#numero ingresado
ns=random.randint(1,20)
print(ns)
print("Bienvenido al juego adivina el numero secreto")
print("tiene 6 intentos")
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

