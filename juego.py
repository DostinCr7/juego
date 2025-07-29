import random

opciones = ["piedra", "papel", "tijera"]

eleccion = input("Que opcion eliges? (piedra, papel, tijera): ").lower()

computador = random.choice(opciones)

def juegoPiedraPapelTijera ():

    if eleccion not in opciones:
        print("Opcion no valida. Por favor, elige entre piedra, papel o tijera.")
        return
    
    if eleccion == computador:
        print("Ambos eligieron", eleccion + ". Es un empate.")

print(juegoPiedraPapelTijera())



    
