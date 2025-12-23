print("-To-Do List")

taches = []

while True:
    print("\nChoisis une option:")
    print("1- Ajouter une tâche")
    print("2- Afficher les tâches")
    print("3- Supprimer une tâche")
    print("4- Quitter")

    choix = input("Écris le numéro de l'option: ")

    if choix == "1":
        tache = input("Écris la tâche: ")
        taches.append(tache)
        print("Tâche ajoutée!")

    elif choix == "2":
        if len(taches) == 0:
            print("Pas de tâches.")
        else:
            print("Tâches:")
            numero = 1
            for t in taches:
                print(numero, "-", t)
                numero = numero + 1  

    elif choix == "3":
        if len(taches) == 0:
            print("Pas de tâches à supprimer.")
        else:
            print("Tâches:")
            numero = 1
            for t in taches:
                print(numero, "-", t)
                numero = numero + 1

            suppr = int(input("Écris le numéro de la tâche à supprimer: "))

            if suppr >= 1 and suppr <= len(taches):
                supprime = taches.pop(suppr - 1)
                print("Tâche supprimée:", supprime)
            else:
                print("Numéro invalide.")

    elif choix == "4":
        print("Au revoir!")
        break

    else:
        print("Option invalide, réessaie!")