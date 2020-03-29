# -*-coding:Latin-1 -*
import os
z = input("inserer votre nom:");
print("Bonjour "+z+"! Bienvenue dans le jeu de mots-meles. \n Le jeu consiste a trouver des mots dans la grille ci-dessous");

grille = ["Z O A P A Y E R", "P U C J E T E R", "L B H E M O V D", "A L E A P M J O", "C I T I S B O N", "E E E M M E U N", "R R R E R R E E", "Q P A R L E R R"];
grille_modifiee = grille;

for ligne in grille:
    print(ligne);

mots_meles = ['payer', 'placer', 'parler', 'aimer', 'donner', 'jouer', 'jeter','tomber', 'oublier']
statut_mots = {}
for word in mots_meles:
    statut_mots[word] = "false"

print('identifiez les mots meles dans la grille.')

counter = 0;

while counter < 9:
    mot = input('Suggerez un mot! ')
    word_matched=0
    for mot_valide in mots_meles:
        if mot == mot_valide:
            word_matched = 1
            break
        else:
            word_matched = 0
    if word_matched == 1:
        if statut_mots[mot] == "true":
                print("vous avez deja identifier ce mot. Reessayer!")
        else:
                print('Correct!')
                statut_mots[mot] == "true"
                counter += 1
    else:
        print("Mot incorrect ! Reessayer!")
    word_matched = 0

print("Bien joue! Vous avez fini le jeu.")










