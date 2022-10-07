"""
Programme fait par Alexandre Toriz
Groupe 023
Description : TP2 - Jeu de devinette
"""

import random

start_jeu = True
boucle_jeu = True
nb_maximum = 100
nb_minimum = 0


def bornes():
    global nb_minimum, nb_maximum
    nb_minimum = int(input("Décidez le nombre minimal que je peux atteindre : "))
    nb_maximum = int(input("Décidez le nombre maximal que je peux atteindre : "))

    """""
    
    Cette fonction est invoquée lorsqu'il faut que le jeu recommence une nouvelle fois.
    Elle sert a définir les bornes du nombre aléatoire que l'ordinateur sélectionne, en tenant compte des limites du joueur.
    
    """""

while start_jeu:
    print("Bienvenue! Je vais choisir un nombre aléatoirement, vous avez pour but de le trouver. ")
    bornes()
    nombre_aleatoire = random.randint(nb_minimum, nb_maximum)
    print(f"J'ai choisi mon nombre au hasard entre {nb_minimum} et {nb_maximum}")
    print("À vous de deviner !")
    boucle_jeu = True
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