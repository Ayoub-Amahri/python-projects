def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur: Division par zéro !"

print("=== Calculatrice Python ===")
print("1 - Addition")
print("2 - Soustraction")
print("3 - Multiplication")
print("4 - Division")

choix = input("Choisissez une opération (1/2/3/4) : ")

a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

if choix == "1":
    print("Résultat :", addition(a, b))
elif choix == "2":
    print("Résultat :", soustraction(a, b))
elif choix == "3":
    print("Résultat :", multiplication(a, b))
elif choix == "4":
    print("Résultat :", division(a, b))
else:
    print("Choix invalide !")