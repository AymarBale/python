# -*-coding:Latin-1 -*
import os
print("remplissez les vides par les mots donnez dans la consigne")

print("Voici les mots a inserer dans le texte\n 1:boutique, 2:voiture, 3:salon, 4:mario, 5:explosion, 6:pain")
os.system("pause")
print("je vais a la ___ pour acheter du ___")
a = input("n1:")
b = input("n2:")
print("L'___ a detruit la ___")
c = input("n3:")
d = input("n4:")
print("Nathan joue a ___ dans le ___")
e = input("n5:")
f = input("n6:")

a = "boutique"
b = "pain"
c = "explosion"
d = "voiture" 
e = "mario"
f = "salon"
print("je vais  a la {0} pour acheter du {1} . L'{2} a detruit la {3} . Nathan joue a {4} dans le {5};.".format(a,b,c,d,e,f))
print("Bien jouer vous avez completer l'exercice")

os.system("pause")