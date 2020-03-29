import os
fight = input("mettez votre age:")
fight = int(fight)
if fight <= 20 and fight > 0:
    print("vous etes un enfant")
if fight <= 30 and fight > 20:
    print("vous etes un jeune")
if fight < 50 and fight > 30:
    print("vous etes un adulte")
if fight >= 50:
    print("vous etes vieux")
if fight > 100 and fight < 0 :
    print("error impossible")

os.system("pause")