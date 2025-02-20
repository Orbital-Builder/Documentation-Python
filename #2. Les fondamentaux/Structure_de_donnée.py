"""

Stucture de donnée en python :

Les structures de données sont des types de données utilisés pour stocker des collections de données.
Il existe quatre types de structures de données en Python :
Liste : une collection ordonnée et modifiable d'éléments.

List : une collection d'éléments ordonnés et modifiables.
Tuple : une collection ordonnée et immuable d'éléments.
Ensemble : une collection non ordonnée et non indexée d'éléments uniques.
Dictionnaire : une collection non ordonnée, modifiable et indexée d'éléments clé-valeur.

Quel'que fonction intégré en python pour les structure de donnée :
len() : renvoie la longueur de la structure de données.
in : vérifie si un élément est présent dans la structure de données.
append() : ajoute un élément à une liste.
remove() : supprime un élément d'une liste.
add() : ajoute un élément à un ensemble.
del : supprime un élément d'un dictionnaire.
items() : renvoie une vue d'ensemble des paires clé-valeur d'un dictionnaire.
keys() : renvoie une vue d'ensemble des clés d'un dictionnaire.
values() : renvoie une vue d'ensemble des valeurs d'un dictionnaire.
sort() : trie les éléments d'une liste.
reverse() : inverse l'ordre des éléments d'une liste.
copy() : renvoie une copie de la structure de données.
clear() : supprime tous les éléments de la structure de données.
pop() : supprime l'élément à l'index spécifié de la liste.
popitem() : supprime la dernière paire clé-valeur d'un dictionnaire.
update() : met à jour un dictionnaire avec les paires clé-valeur spécifiées.
setdefault() : renvoie la valeur de la clé spécifiée d'un dictionnaire. Si la clé n'existe pas, elle l'ajoute avec la valeur spécifiée.
index() : renvoie l'index de la première occurrence de la valeur spécifiée.
count() : renvoie le nombre de fois que la valeur spécifiée apparaît dans la liste.
extend() : ajoute les éléments d'une liste (ou d'un autre itérable) à la fin d'une liste.
insert() : ajoute un élément à la position spécifiée de la liste.
---------------------------------------------------------------------------------------------------------------------------------------

"""


#Liste :
#Une liste est une collection ordonnée et modifiable d'éléments.
#Les éléments d'une liste peuvent être de différents types de données.
#Les éléments d'une liste sont indexés et peuvent être accédés en utilisant des indices.
#Les listes sont définies en utilisant des crochets []. Les éléments d'une liste sont séparés par des virgules.

#Créer une liste
liste = [1, 2, 3, 4, 5]
print(liste)

#Accéder aux éléments d'une liste
print(liste[0]) #Affiche 1
print(liste[1]) #Affiche 2
print(liste[2]) #Affiche 3

#Modifier les éléments d'une liste
liste[0] = 10
print(liste) #Affiche [10, 2, 3, 4, 5]

#Ajouter des éléments à une liste
liste.append(6)
print(liste) #Affiche [10, 2, 3, 4, 5, 6]

#Supprimer des éléments d'une liste
liste.remove(6)
print(liste) #Affiche [10, 2, 3, 4, 5]

#Longueur d'une liste
print(len(liste)) #Affiche 5

#Vérifier si un élément est présent dans une liste
if 3 in liste:
    print("3 est présent dans la liste")
else:
    print("3 n'est pas présent dans la liste")

#Parcourir une liste
for i in liste:
    print(i)

#Liste de listes
liste = [[1, 2], [3, 4], [5, 6]]
print(liste) #Affiche [[1, 2], [3, 4], [5, 6]]
print(liste[0]) #Affiche [1, 2]
print(liste[0][0]) #Affiche 1
print(liste[0][1]) #Affiche 2

#Tuple (sequence):
#Un tuple est une collection ordonnée et immuable d'éléments.
#Les éléments d'un tuple peuvent être de différents types de données.
#Les éléments d'un tuple sont indexés et peuvent être accédés en utilisant des indices.
#Les tuples sont définis en utilisant des parenthèses (). Les éléments d'un tuple sont séparés par des virgules.
#Les tuples sont immuables, ce qui signifie que les éléments d'un tuple ne peuvent pas être modifiés une fois qu'ils sont définis.
#On peux crée un tuples vide: tuple = ()

#Exemple de tuples vide + le type: 
tuple = ()
print(type(tuple))

#Exemple de tuple:
tuple = (1, 2, 3, 4, 5, "John", "Jane")
#Error: on ne peux pas assigné une nouvelle value à un tuple Exemple: tuple[2] = "Paul"
print(tuple)

#Quel'que exeption aux nouvelle value: 
(nombre1, nombre2, nombre3) = (10, 20, 30)
#Changer la value:
#Car se sont des variables et non des tuples
nombre1 = 10
nombre2 = 20
nombre3 = 30
print(nombre1) #Affiche 1
print(nombre2) #Affiche 2
print(nombre3) #Affiche 3

#Accéder aux éléments d'un tuple
print(tuple[0]) #Affiche 1
print(tuple[1]) #Affiche 2
print(tuple[2]) #Affiche 3
print (tuple[5]) #Affiche John

#Longueur d'un tuple
print(len(tuple)) #Affiche 5

#Vérifier si un élément est présent dans un tuple
if 3 in tuple:
    print("3 est présent dans le tuple")
else:
    print("3 n'est pas présent dans le tuple")

#Parcourir un tuple
for i in tuple:
    print(i)

#Ensemble :
#Un ensemble est une collection non ordonnée et non indexée d'éléments uniques.
#Les éléments d'un ensemble ne sont pas indexés et ne peuvent pas être accédés en utilisant des indices.
#Les ensembles sont définis en utilisant des accolades {}. Les éléments d'un ensemble sont séparés par des virgules.

#Créer un ensemble
ensemble = {1, 2, 3, 4, 5}
print(ensemble)

#Ajouter des éléments à un ensemble
ensemble.add(6)
print(ensemble) #Affiche {1, 2, 3, 4, 5, 6}

#Supprimer des éléments d'un ensemble
ensemble.remove(6)
print(ensemble) #Affiche {1, 2, 3, 4, 5}

#Longueur d'un ensemble
print(len(ensemble)) #Affiche 5

#Vérifier si un élément est présent dans un ensemble
if 3 in ensemble:
    print("3 est présent dans l'ensemble")
else:
    print("3 n'est pas présent dans l'ensemble")

#Parcourir un ensemble
for i in ensemble:
    print(i)

#Dictionnaire :
#Un dictionnaire est une collection non ordonnée, modifiable et indexée d'éléments clé-valeur.
#Les éléments d'un dictionnaire sont indexés par des clés et peuvent être accédés en utilisant des clés.
#Les clés d'un dictionnaire doivent être uniques.
#Les dictionnaires sont définis en utilisant des accolades {}. Les éléments d'un dictionnaire sont des paires clé-valeur séparées par des virgules.
#Pair, dictionnaire = {<key:value> , <key2:value>}
#Lire la valeur : dictionnaire[<key>]
#Ajouter une valeur : dictionnaire[<key>] = <value>
#Si valeur déjà présente la value et écrassée

#Exemple de fonction dictionnaire: 

#pop : supprime la clé spécifiée et renvoie la valeur.
#popitem : supprime la dernière paire clé-valeur et renvoie la paire supprimée.
#clear : supprime tous les éléments du dictionnaire.
#copy : renvoie une copie du dictionnaire.
#items : renvoie une vue d'ensemble des paires clé-valeur du dictionnaire.
#keys : renvoie une vue d'ensemble des clés du dictionnaire.
#values : renvoie une vue d'ensemble des valeurs du dictionnaire.
#update : met à jour le dictionnaire avec les paires clé-valeur spécifiées.
#setdefault : renvoie la valeur de la clé spécifiée. Si la clé n'existe pas, elle l'ajoute avec la valeur spécifiée.


#Créer un dictionnaire
dictionnaire = {"nom": "John", "age": 30, "ville": "New York"}
print(dictionnaire)

#Exemple dictionnaire: 
for val in dictionnaire.values():
    print(val)  

#Affiche les keys du dictionnaire:
for key in dictionnaire.keys():
    print(key)

#Testé les deux: 
for key, val in dictionnaire.items():
    print(key, val)

#Accéder aux éléments d'un dictionnaire
print(dictionnaire["nom"]) #Affiche John
print(dictionnaire["age"]) #Affiche 30
print(dictionnaire["ville"]) #Affiche New York

#Modifier les éléments d'un dictionnaire
dictionnaire["age"] = 35
print(dictionnaire) #Affiche {'nom': 'John', 'age': 35, 'ville': 'New York'}

#Ajouter des éléments à un dictionnaire
dictionnaire["pays"] = "USA"
print(dictionnaire) #Affiche {'nom': 'John', 'age': 35, 'ville': 'New York', 'pays': 'USA'}

#Supprimer des éléments d'un dictionnaire
del dictionnaire["ville"]
print(dictionnaire) #Affiche {'nom': 'John', 'age': 35, 'pays': 'USA'}

#Longueur d'un dictionnaire
print(len(dictionnaire)) #Affiche 3

#Vérifier si une clé est présente dans un dictionnaire
if "age" in dictionnaire:
    print("La clé 'age' est présente dans le dictionnaire")
else:
    print("La clé 'age' n'est pas présente dans le dictionnaire")

#Parcourir un dictionnaire
for cle, valeur in dictionnaire.items():
    print(cle, valeur)

#Liste de dictionnaires
liste = [{"nom": "John", "age": 30}, {"nom": "Jane", "age": 25}]
print(liste) #Affiche [{'nom': 'John', 'age': 30}, {'nom': 'Jane', 'age': 25}]
print(liste[0]) #Affiche {'nom': 'John', 'age': 30}
print(liste[0]["nom"]) #Affiche John

#Tuple de dictionnaires
tuple = ({"nom": "John", "age": 30}, {"nom": "Jane", "age": 25})
print(tuple) #Affiche ({'nom': 'John', 'age': 30}, {'nom': 'Jane', 'age': 25})
print(tuple[0]) #Affiche {'nom': 'John', 'age': 30}


#Dictionnaire de listes
dictionnaire = {"noms": ["John", "Jane"], "ages": [30, 25]}
print(dictionnaire) #Affiche {'noms': ['John', 'Jane'], 'ages': [30, 25]}
print(dictionnaire["noms"]) #Affiche ['John', 'Jane']
print(dictionnaire["noms"][0]) #Affiche John

#Dictionnaire de tuples
dictionnaire = {"personne": ("John", 30)}
print(dictionnaire) #Affiche {'personne': ('John', 30)}
print(dictionnaire["personne"]) #Affiche ('John', 30)
print(dictionnaire["personne"][0]) #Affiche John

#Dictionnaire de dictionnaires
dictionnaire = {"personne": {"nom": "John", "age": 30}}
print(dictionnaire) #Affiche {'personne': {'nom': 'John', 'age': 30}}
print(dictionnaire["personne"]) #Affiche {'nom': 'John', 'age': 30}

#Dictionnaire de listes de dictionnaires
dictionnaire = {"personnes": [{"nom": "John", "age": 30}, {"nom": "Jane", "age": 25}]}
print(dictionnaire) #Affiche {'personnes': [{'nom': 'John', 'age': 30}, {'nom': 'Jane', 'age': 25]}
print(dictionnaire["personnes"]) #Affiche [{'nom': 'John', 'age': 30}, {'nom': 'Jane', 'age': 25}]
print(dictionnaire["personnes"][0]) #Affiche {'nom': 'John', 'age': 30}
print(dictionnaire["personnes"][0]["nom"]) #Affiche John

#Dictionnaire de dictionnaires de listes
dictionnaire = {"personne": {"noms": ["John", "Jane"], "ages": [30, 25]}}
print(dictionnaire) #Affiche {'personne': {'noms': ['John', 'Jane'], 'ages': [30, 25]}}
print(dictionnaire["personne"]) #Affiche {'noms': ['John', 'Jane'], 'ages': [30, 25]}
print(dictionnaire["personne"]["noms"]) #Affiche ['John', 'Jane']
print(dictionnaire["personne"]["noms"][0]) #Affiche John

