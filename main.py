"""""
Programme fait par Alexandre Toriz
Groupe 023
Description : TP2 - Jeu de devinette

"""""

boucle_jeu = True
import random

nombre_aleatoire = random.randint(0, 100)
print("J'ai choisi un nombre au hasard entre 0 et 100")
print("À vous de deviner !")

def jeu():
    essai = input(int("Entrez un nombre: "))
    if nombre_aleatoire == essai:
        print("Égalité! Vous avez gagné!")
        rejouer = input(str("Voulez-vous rejouer? Oui ou Non?"))
        if rejouer = "Oui":
            jeu()
        else:
            boucle_jeu = False
    elif essai < nombre_aleatoire:
        print("Raté, pensez plus grand")
        jeu()
    elif essai > nombre_aleatoire:
        print("Raté, pensez plus petit")
        jeu()

while boucle_jeu:

