from typing import List
from colorama import init, Fore

init()
#sacamos de chatgpt lo de colorama
#from colorama import init, Fore, Back, Style


#tablero
Tablero:List[List[bool]] = []
f=5
c=5
t=[]
for i in range (f):
    hilera = []
    for r in range(c):
        hilera.append(False)
    t.append(hilera)

#barcos
t[0][1]=True
t[1][0]=True
t[2][2]=True

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
                if 0 <= filaIngresada <= 4:  # Verifica si el número está en el rango de 0 a 4
                    break
                else:
                    print("La fila debe estar en el rango de 0 a 4.")
            else:
                print("Por favor, introduce un número entero válido.")

    # Pedir al usuario el segundo número
        while True:
            columnaIngresada = input("Ingresa la columna: ")
            if columnaIngresada.isdigit():  # Verifica si la entrada es un número entero
                columnaIngresada = int(columnaIngresada)
                if 0 <= columnaIngresada <= 4:  # Verifica si el número está en el rango de 0 a 4
                    break
                else:
                    print("El número debe estar en el rango de 0 a 4.")
            else:
                print("Por favor, introduce un número entero válido.")
        if t[filaIngresada][columnaIngresada] == True:
            tirosAcertados+=1
        else:
            tirosErrados+=1
    else:
        print("Te quedaste sin tiros, el juego finalizó")
    
    


print(Fore.GREEN + "Cantidad de tiros acertados: " + str(tirosAcertados))
print(Fore.RED + "Cantidad de tiros errados: " + str(tirosErrados))
print(Fore.WHITE + "")
print(t)
print(Fore.WHITE + "")