import random

"""

la modularité en python & Utilisation des modules.

Doc python : https://docs.python.org/fr/3.13/py-modindex.html

Importé un module : 
from random import random -> #Supprime le prefixe random. pour appeler la fonction , random, randerange, etc
from random import * -> #Importe toutes les fonctions du module random

Importé un module alias : 
import random as r 
------------------------------------------------------------------------------------------------------------

"""

for i in range(10):  
    print(random.randrange(1, 10)) #renvoie un nombre aléatoire entre 1 et 10
