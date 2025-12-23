print("- Calculatrice de moyenne ")

notes = []
nombre_notes = int(input("Combien de notes voulez-vous entrer ? "))

for i in range(nombre_notes):
    while True:
        try:
            note = float(input(f"Entrez la note {i+1} : "))
            if 0 <= note <= 20:
                notes.append(note)
                break
            else:
                print("Veuillez entrer une note entre 0 et 20 !")
        except ValueError:
            print("Entrée invalide, veuillez entrer un nombre.")

moyenne = sum(notes) / len(notes)
print(f"Votre moyenne est : {moyenne:.2f}")


if moyenne >= 16:
    print("Mention: Très Bien")
elif moyenne >= 14:
    print("Mention: Bien")
elif moyenne >= 12:
    print("Mention: Assez Bien")
elif moyenne >= 10:
    print("Mention: Passable")
else:
    print("Mention: Insuffisant")