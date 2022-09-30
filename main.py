"""""
Programme fait par Alexandre Toriz
Groupe 023
Description : TP2 - Jeu de devinette

"""""

import random


start_jeu = True
boucle_jeu = True
nb_maximum = 100
nb_minimum = 0


def bornes():
    global nb_minimum, nb_maximum
    nb_maximum = int(input("Décidez le nombre maximal que je peux atteindre : "))
    nb_minimum = int(input("Décidez le nombre minimal que je peux atteindre : "))

while start_jeu:
    print("Bienvenue! Je vais choisir un nombre aléatoirement, vous avez pour but de le trouver. ")
    bornes()
    nombre_aleatoire = random.randint(nb_minimum, nb_maximum)
    print(f"J'ai choisi mon nombre au hasard entre {nb_minimum} et {nb_maximum}")
    print("À vous de deviner !")
    while boucle_jeu == True:
        essai = int(input(str("Entrez un nombre: ")))
        if essai < nombre_aleatoire:
            print("Oups! Le nombre est plus grand.")
        elif essai > nombre_aleatoire:
            print("Ouille. Le nombre est plus petit.")
        elif essai == nombre_aleatoire:
            print("Bravo! Vous avez trouvé le nombre!")
            rejouer = input("Voulez-vous rejouer? (Oui ou Non): ")
            if rejouer == "Oui":
                boucle_jeu = False
            else:
                print("Merci de votre participation.")
                boucle_jeu = False
                start_jeu = False