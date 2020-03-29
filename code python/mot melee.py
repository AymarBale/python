# -*-coding:Latin-1 -*
import os
z = input("inserer votre nom:")

print("Bonjour bienvenue dans le jeu de mot-melee.Le jeu consiste a trouver des mots dans la grille ci-dessous")

grille = ("Z O A P A Y E R \nP U C J E T E R \nL B H E M O V D \nA L E A P M J O \nC I T I S B O N \nE E E M M E U N \nR R R E R R E E \nQ P A R L E R R") 

print(grille)
print("Consigne:\nremplisser les mots en les mettant les lettre manquantes que vous trouverer dans la grille: \n1°_c_e_er  ;  4°_e_er ;  7°pa_l_r ; 10°t__be_ \n2°a_m_r ; 5°_o_er ; 8°_ay_r \n3°d___er ; 6°_u_l_er ; 9°_la_er")

a = input("n1°:")
for lettre in a :
    if lettre in "a":
       print("Z O * P A Y E R \nP U * J E T E R \nL B * E M O V D \nA L * A P M J O \nC I * I S B O N \nE E * M M E U N \nR R * E R R E E \nQ P A R L E R R")

b = input("n2°:")
for lettre in b :
    if lettre in "i":
       print("Z O * P A Y E R \nP U * J E T E R \nL B * E M O V D \nA L * * P M J O \nC I * * S B O N \nE E * * M E U N \nR R * * R R E E \nQ P A R L E R R") 

c = input("n3°:")
for lettre in c :
    if lettre in "o":
       print("Z O * P A Y E R \nP U * J E T E R \nL B * E M O V * \nA L * * P M J * \nC I * * S B O * \nE E * * M E U * \nR R * * R R E * \nQ P A R L E R *") 

d = input("n4°:")
for lettre in c :
    if lettre in "t":
       print("Z O * P A Y E R \nP U * * * T * * \nL B * E M O V * \nA L * * P M J * \nC I * * S B O * \nE E * * M E U * \nR R * * R R E * \nQ P A R L E R *") 

e = input("n5°:")
for lettre in e :
    if lettre in "j":
       print("Z O * P A Y E R \nP U * * * T * * \nL B * E M O V * \nA L * * P M * * \nC I * * S B * * \nE E * * M E * * \nR R * * R R * * \nQ P A R L E R *") 


f = input("n6°:")
for lettre in f :
    if lettre in "b":
       print("Z * * P A Y E R \nP * * * * T * * \nL * * E M O V * \nA * * * P M * * \nC * * * S B * * \nE * * * M E * * \nR * * * R R * * \nQ P A R L E R *") 

g = input("n7°:")
for lettre in g :
    if lettre in "r":
       print("Z * * P A Y E R \nP * * * * T * * \nL * * E M O V * \nA * * * P M * * \nC * * * S B * * \nE * * * M E * * \nR * * * R R * * \nQ * * * * * * *") 

h = input("n8°:")
for lettre in h :
    if lettre in "y":
       print("Z * * * * * * * \nP * * * * T * * \nL * * E M O V * \nA * * * P M * * \nC * * * S B * * \nE * * * M E * * \nR * * * R R * * \nQ * * * * E * *") 

i = input("n9°:")
for lettre in i :
    if lettre in "l":
       print("Z * * * * * * * \n* * * * * T * * \n* * * E M O V * \n* * * * P M * * \n* * * * S B * * \n* * * * M E * * \n* * * * R R * * \nQ * * * * E * *") 

j = input("n10°:")
for lettre in j :
    if lettre in "r":
       print("Z * * * * * * * \n* * * * * * * * \n* * * E * O V * \n* * * * P * * * \n* * * * S * * * \n* * * * M * * * \n* * * * R * * * \nQ * * * * E * *") 

print("Bien jouer vous avez fini le jeu")

os.system("pause")









