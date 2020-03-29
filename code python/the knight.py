# -*-coding:Latin-1 -*

import os

love = input("fait votre choix entre la droite et la gauche:")

love = str(love)

for lettre in love:
   if lettre in "dg":
       print("vous etes tombé sur une foret enchanter")
   if lettre in "d":
       print("vu que vous avez choisi la droite vous devenez un chevalier")
   if lettre in "g":
       print("eyant choisi la gauche vous devenez un mage")   
   
os.system("pause")

adventure = input("choose a quest between a dragon and a giant snake:")

for lettre in adventure:
   if lettre in "d":
       print("you went to fight a dragon")
   if lettre in "g":
       print("you arrived at the snake lair")

os.system("pause")