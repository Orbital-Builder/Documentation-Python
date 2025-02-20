import Module_Custom
"""

Crée c'est propre module :

import <module> si il est a la racine du fichier ici monModule.py
import <dossier>.<module> si il est dans un sous dossier
Dossier __pycache__ -> fichier de cache pour l'optimisation 
-----------------------------------------------------------------

"""

nb = input("Entrez un nombre : ")

print("Le carré est de ", Module_Custom.carre(2))

Module_Custom.somme(2, 3)


#Testé sont module
print(__name__)