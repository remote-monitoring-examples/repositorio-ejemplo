
import random

def jugar():
    print("=" * 40)
    print("       JUEGO: ADIVINA EL NÚMERO")
    print("=" * 40)

    print("\nSelecciona la dificultad:")
    print("1. Fácil (1 - 20)")
    print("2. Medio (1 - 50)")
    print("3. Difícil (1 - 100)")

    opcion = input("\nTu elección: ")

    if opcion == "1":
        maximo, intentos = 20, 7
    elif opcion == "2":
        maximo, intentos = 50, 6
    elif opcion == "3":
        maximo, intentos = 100, 5
    else:
        print("Opción no válida.")
        return

    secreto = random.randint(1, maximo)
    puntos = 100
    print(f"\nHe elegido un número entre 1 y {maximo}.")
    print(f"Tienes {intentos} intentos para descubrirlo.")

    while intentos > 0:
        try:
            numero = int(input("\nIngresa tu número: "))
        except ValueError:
            print("Debes ingresar un número entero.")
            continue

        if numero < 1 or numero > maximo:
            print(f"El número debe estar entre 1 y {maximo}.")
            continue

        intentos -= 1

        if numero == secreto:
            puntos += intentos * 20
            print("\n¡FELICIDADES! ¡Lo descubriste!")
            print(f"El número era {secreto}.")
            print(f"Puntuación final: {puntos} puntos.")
            return

        elif numero < secreto:
            print("El número secreto es MAYOR.")
        else:
            print("El número secreto es MENOR.")

        puntos -= 10
        print(f"Intentos restantes: {intentos}")

    print("\n¡Se acabó el juego!")
    print(f"El número secreto era {secreto}.")
    print(f"Puntuación: {max(0, puntos)} puntos.")


while True:
    jugar()
    otra = input("\n¿Quieres jugar otra vez? (s/n): ").lower()

    if otra != "s":
        print("\n¡Gracias por jugar!")
        break
