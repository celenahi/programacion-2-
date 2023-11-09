import random		
IMAGENES_AHORCADO = ['''		
  +---+		
  |   |		
      |		
      |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
      |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
  |   |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|   |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
 /    |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
 / \  |		
      |		
  =========''']		
ListaPalabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo cebra'.split()
LetraCorrecta=0
LetraIncorrecta=0
VidasRestantes=0
VIDAS=6
r=""
LetrasIngresadas=" "
ABC='A B C D E F G H I J K L M N Ñ O P K R S T X Y Z W V Q a b c d e f g h j k l m n ñ o p q i r s t v  w  x  y z'.split()
def buscarPalabra(ListaPalabra):
    PalabraElegida=random.randint(0, len(ListaPalabra)-1)
    return ListaPalabra[PalabraElegida]
def MostrarTablero(IMAGENES_AHORCADO,LetraCorrecta,LetraIncorrecta,VidasRestantes,PalabraElegida):
    print("hola bienvenido al juego del ahorcado")
    print("")
    while  LetrasCorrectas != len((PalabraElegida)-1):
        print(IMAGENES_AHORCADO[0])
        for i in range(1,1,len(PalabraElegida)-1):
            LetrasIngresadas= int(input("ingrese una letra"))
            LetrasIngresadas.lower()
            if LetrasIngresadas in ABC:
                if LetrasIngresadas in PalabraElegida:
                    LetrasCorrectas= LetrasCorrectas+1
                    print("la letra ingresaa es correcta")#falta mostrar la imagen con las letras
                else:
                    print("la letra ingresada es incorrecta")
                    for j in range (1,1,VIDAS):
                        LetrasIncorrectas=LetrasIncorrectas+1
                        VidasRestantes=VIDAS-1
                        print("le quedan: ",VIDAS,"vidas")
                        if  VidasRestantes==5:
                            print(IMAGENES_AHORCADO[1])
                        if VidasRestantes==4:
                           print(IMAGENES_AHORCADO[2])
                        if VidasRestantes==3:
                           print(IMAGENES_AHORCADO[3])
                        if VidasRestantes==2:
                           print(IMAGENES_AHORCADO[4])
                        if VidasRestantes==1:
                           print(IMAGENES_AHORCADO[5])
                        if VidasRestantes==0:
                            print(IMAGENES_AHORCADO[6])
            else:
               print("lo que ingreso no es valido")
            break
        if (LetraCorrecta == len ((PalabraElegida)-1)):
            print("felicitaciones has ganado")

buscarPalabra(ListaPalabras)

MostrarTablero(IMAGENES_AHORCADO,LetraCorrecta,LetraIncorrecta,VidasRestantes,PalabraElegida )

#r=input("desea volver a jugar")
#print("si es si presione la tecla s, sino n")

