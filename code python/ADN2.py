import os
def X(): 
  l = [("AGT","UCA"),("CGA","GCU"),("ACG","UGC"),("TCG","AGC"),("CAA","GUU"),("TAC","AUG"),("TCC","AGG"),("ATA","UAU"),("ACT","UGA"),("CAG","GUC"),("GCT","CGA"),("CGT","GCU"),("GAC","CUG"),("GTC","CAG"),("CGA","GCU")]
  import random
  random.shuffle(l)
  del l[0:9]
  d ={}
  for k,v in l:
      d[k]=v
  print("Bonjours le but de se programme est de creer une chaine au d'ADN hasard et de la transformer en ARN")
  os.system("pause")
  for cle in d.keys():
      print(cle)
  print("voici la chaine que nous avons\n nous allons maintenant la transformer en ARN")
  os.system("pause")
  for cle, valeur in d.items():
        print("Le codons {} se transforme en l'ARN {} .".format(cle,valeur))
  os.system("pause")
