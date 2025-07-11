from operator import truediv

from typing import List
from colorama import init, Fore
emojis = [
    "\U0001F600", "\U0001F601", "\U0001F602", "\U0001F603", "\U0001F604", "\U0001F605", "\U0001F606", "\U0001F607",
    "\U0001F608", "\U0001F609", "\U0001F60A", "\U0001F60B", "\U0001F60C", "\U0001F60D", "\U0001F60E", "\U0001F60F",
    "\U0001F610", "\U0001F611", "\U0001F612", "\U0001F613", "\U0001F614", "\U0001F615", "\U0001F616", "\U0001F617",
    "\U0001F618", "\U0001F619", "\U0001F61A", "\U0001F61B", "\U0001F61C", "\U0001F61D", "\U0001F61E", "\U0001F61F",
    "\U0001F620", "\U0001F621", "\U0001F622", "\U0001F623", "\U0001F624", "\U0001F625", "\U0001F626", "\U0001F627",
    "\U0001F628", "\U0001F629", "\U0001F62A", "\U0001F62B", "\U0001F62C", "\U0001F62D", "\U0001F62E", "\U0001F62F",
    "\U0001F630", "\U0001F631", "\U0001F632", "\U0001F633", "\U0001F634", "\U0001F635", "\U0001F636", "\U0001F637",
    "\U0001F638", "\U0001F639", "\U0001F63A", "\U0001F63B", "\U0001F63C", "\U0001F63D", "\U0001F63E", "\U0001F63F",
    "\U0001F640", "\U0001F641", "\U0001F642", "\U0001F643", "\U0001F644", "\U0001F645", "\U0001F646", "\U0001F647",
    "\U0001F648", "\U0001F649", "\U0001F64A", "\U0001F64B", "\U0001F64C", "\U0001F64D", "\U0001F64E", "\U0001F64F",
    "\U0001F680", "\U0001F681", "\U0001F682", "\U0001F683", "\U0001F684", "\U0001F685", "\U0001F686", "\U0001F687",
    "\U0001F688", "\U0001F689", "\U0001F68A", "\U0001F68B", "\U0001F68C", "\U0001F68D", "\U0001F68E", "\U0001F68F",
    "\U0001F690", "\U0001F691", "\U0001F692", "\U0001F693", "\U0001F694", "\U0001F695", "\U0001F696", "\U0001F697",
    "\U0001F698", "\U0001F699", "\U0001F69A", "\U0001F69B", "\U0001F69C", "\U0001F69D", "\U0001F69E", "\U0001F69F",
    "\U0001F6A0", "\U0001F6A1", "\U0001F6A2", "\U0001F6A3", "\U0001F6A4", "\U0001F6A5", "\U0001F6A6", "\U0001F6A7",
    "\U0001F6A8", "\U0001F6A9", "\U0001F6AA", "\U0001F6AB", "\U0001F6AC", "\U0001F6AD", "\U0001F6AE", "\U0001F6AF",
    "\U0001F6B0", "\U0001F6B1", "\U0001F6B2", "\U0001F6B3", "\U0001F6B4", "\U0001F6B5", "\U0001F6B6", "\U0001F6B7",
    "\U0001F6B8", "\U0001F6B9", "\U0001F6BA", "\U0001F6BB", "\U0001F6BC", "\U0001F6BD", "\U0001F6BE", "\U0001F6BF",
    "\U0001F6C0", "\U0001F6C1", "\U0001F6C2", "\U0001F6C3", "\U0001F6C4", "\U0001F6C5", "\U0001F6CB", "\U0001F6CC",
    "\U0001F90C", "\U0001F90D", "\U0001F90E", "\U0001F90F", "\U0001F910", "\U0001F911", "\U0001F912", "\U0001F913",
    "\U0001F914", "\U0001F915", "\U0001F916", "\U0001F917", "\U0001F918", "\U0001F919", "\U0001F91A", "\U0001F91B",
    "\U0001F91C", "\U0001F91D", "\U0001F91E", "\U0001F91F", "\U0001F920", "\U0001F921", "\U0001F922", "\U0001F923",
    "\U0001F924", "\U0001F925", "\U0001F926", "\U0001F927", "\U0001F928", "\U0001F929", "\U0001F92A", "\U0001F92B",
    "\U0001F92C", "\U0001F92D", "\U0001F92E", "\U0001F92F", "\U0001F930", "\U0001F931", "\U0001F4A7"]

init()
#sacamos de chatgpt lo de colorama
#from colorama import init, Fore, Back, Style


#tablero
Tablero:List[List[bool]] = []
f=5
c=5
row=f-1
column=c-1
t=[]
for i in range (f):
    hilera = []
    for r in range(c):
        hilera.append(False)
    t.append(hilera)

#barcos
cantidadBarcos = 3
#for i in range (cantidadBarcos):
    
#filab1j1= input("Jugador 1, ingrese la fila del barco 1:")
#columnab1j1= input("Jugador 1, ingrese la columna del barco 1:")
#t[filab1j1][columnab1j1] = True

#filab1j2= input("Jugador 2, ingrese la fila del barco 1:")
#columnab1j2= input("Jugador 2, ingrese la columna del barco 1:")
#t[filab1j2][columnab1j2] = True

#filab2j1= input("Jugador 1, ingrese la fila del barco 2:")
#columnab2j1= input("Jugador 1, ingrese la columna del barco 2:")
#t[filab2j1][columnab2j1] = True

#filab2j2= input("Jugador 2, ingrese la fila del barco 2:")
#columnab2j2= input("Jugador 2, ingrese la columna del barco 2:")
#t[filab2j2][columnab2j2] = True

#filab3j1= input("Jugador 1, ingrese la fila del barco 3:")
#columnab3j1= input("Jugador 1, ingrese la columna del barco 3:")
#t[filab3j1][columnab3j1] = True

#filab3j2= input("Jugador 2, ingrese la fila del barco 3:")
#columnab3j2= input("Jugador 2, ingrese la columna del barco 3:")
#t[filab3j2][columnab3j2] = True

#juego
tirosAcertados = 0
tirosErrados = 0
tirosDisponibles = 3

#la funcion while la sacamos de chat gpt, sin contenido
for j in range (tirosDisponibles):
    if tirosDisponibles > 0:
        while True:
            filaIngresada = input("Ingresa la fila: ")
            if filaIngresada.isdigit():  # Verifica si la entrada es un número entero
                filaIngresada = int(filaIngresada)
                if 0 <= filaIngresada <= row:  # Verifica si el número está en el rango de 0 a la Fila
                    break
                else:
                    print("La fila debe estar en el rango de 0 a " + str(row))
            else:
                print("Por favor, introduce un número entero válido.")

    # Pedir al usuario el segundo número
        while True:
            columnaIngresada = input("Ingresa la columna: ")
            if columnaIngresada.isdigit():  # Verifica si la entrada es un número entero
                columnaIngresada = int(columnaIngresada)
                if 0 <= columnaIngresada <= column:  # Verifica si el número está en el rango de 0 a la Columna
                    break
                else:
                    print("El número debe estar en el rango de 0 a " + str(column))
            else:
                print("Por favor, introduce un número entero válido.")
        if t[filaIngresada][columnaIngresada] == True:
            tirosAcertados+=1
            posicionBien = filaIngresada
            columnaBien = columnaIngresada
        else:
            tirosErrados+=1
    else:
        print("Te quedaste sin tiros, el juego finalizó")
    
    



        


print(Fore.GREEN + "Cantidad de tiros acertados: " + str(tirosAcertados))
print(Fore.RED + "Cantidad de tiros errados: " + str(tirosErrados))
print(Fore.WHITE + "")

# Los saltos de linea cada 5 lo hicimos con chat.openai.com
for fila in t:
    contador = 0
    for elemento in fila:
        if elemento == False:
            print("\U0001F4A7", end="")
        else:
            print("\U0001F6E5", end="")
        contador += 1
        if contador == 5:
            print()
            contador = 0
print(Fore.WHITE + "")