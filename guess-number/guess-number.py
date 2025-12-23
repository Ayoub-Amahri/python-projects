import random

print(" Jeu: Devine le nombre ")

nombre_secret = random.randint(1, 100)

essais = 0

while True:
    try:
        guess = int(input("Devinez le nombre (entre 1 et 100) : "))
        essais += 1

        if guess < nombre_secret:
            print("Trop petit !")
        elif guess > nombre_secret:
            print("Trop grand !")
        else:
            print(f"Bravo ! Vous avez trouvé le nombre {nombre_secret} en {essais} essais.")
            break

    except ValueError:
        print("Veuillez entrer un nombre valide !")