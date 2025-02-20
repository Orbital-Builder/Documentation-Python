"""

Les erreurs et les exceptions en python sont des évenemts qui peuvent interrompre l'exécution d'un programme

Syntax try except:
try: testé un bloc de code
except: le bloc et exécuté en cas d'erreur


Erreur et exepctions en python 
 1. Erreur de syntaxe
 2. Erreur d'exécution
 3. Erreur de logique
 4. Exceptions
 5. Gestion des exceptions
 6. Créer ses propres exceptions


Les différente exeptions en python:

ZeroDivisionError: division par zéro
ValueError: Mauvaise valeur
TypeError: Mauvais type de variable
NameError: Variable non définie
IndexError: Index hors de la plage
KeyError: Clé non trouvée dans un dictionnaire
FileNotFoundError: Fichier non trouvé
ImportError: Module non trouvé
KeyboardInterrupt: Interruption du programme par l'utilisateur
MemoryError: Mémoire insuffisante
OverflowError: Dépassement de capacité
SyntaxError: Erreur de syntaxe
IndentationError: Erreur d'indentation
TabError: Erreur de tabulation
AttributeError: Attribut non trouvé
NotImplementedError: Fonctionnalité non implémentée
OSError: Erreur système
ArithmeticError: Erreur arithmétique
AssertionError: Assertion fausse
EOFError: Fin de fichier
FloatingPointError: Erreur de point flottant
IOError: Erreur d'entrée/sortie
ImportError: Erreur d'importation
LookupError: Erreur de recherche
Finally: Bloc d'instructions exécuté en fin de programme




 1. Erreur de syntaxe
'''for i in range(10)
    print(i)'''



2. Erreur d'exécution (exepction)
try: testé un bloc de code
except: le bloc et exécuté en cas d'erreur


nb1 = input("nb1? ")
nb2 = input("nb2? ")
try:
    nb1 = int(nb1)
    nb2 = int(nb2)
except:
    print("CODE BUGGÉ ! ")
    print("Fin du programme !")

------------------------------------------------------------------------------------------------------------

"""


#Résultat: ont essaie de convertir les variables en entier, si on rentre des lettres, erreur !
#On contourne l'erreur en utilisant try except

#Lever une exception et traité plusieurs exceptions
nb1 = input("nb1? ")
nb2 = input("nb2? ")
try:
    nb1 = int(nb1)
    nb2 = int(nb2)
except (ValueError, ZeroDivisionError):
    print("Il y'a une erreur dans le code, mais l'execption à était leveé !")
    print("Fin du programme, Exepction levée !")

#Récuperer l'exepction dans une variable:
nb1 = input("nb1? ")
nb2 = input("nb2? ")
try:
    nb1 = int(nb1)
    nb2 = int(nb2)
except Exception as err:
    print(err)


#Exepction dans un else: 
nb1 = input("nb1? ")
nb2 = input("nb2? ")
try:
    nb1 = int(nb1)
    nb2 = int(nb2)
except Exception as err:
    print(err)
else:
    print("Code Ok !")

#Finally: Bloc d'instructions exécuté en fin de programme
nb1 = input("nb1? ")
nb2 = input("nb2? ")
try:
    nb1 = int(nb1)
    nb2 = int(nb2)
except Exception as err:
    print(err)
else:
    print("Code Ok !")
finally:
    print("Fin du programme !")


#Fonction pass sur exeption:
nb1 = input("nb1? ")
nb2 = input("nb2? ")
try:
    nb1 = int(nb1)
    nb2 = int(nb2)
except:
    pass #pass permet de ne rien faire (null value)




