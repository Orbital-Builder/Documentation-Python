'''
Les fonctions en python
Les fonctions sont des blocs de code qui effectuent une tâche spécifique.
Une fois que vous avez défini une fonction, vous pouvez l'appeler autant de fois que vous le souhaitez.
Vous pouvez passer des données, appelées paramètres, à une fonction.
Une fonction peut renvoyer des données en sortie.
Les fonctions rendent votre code plus lisible et plus facile à gérer.
Les fonctions peuvent être appelées à partir d'autres fonctions.
Les fonctions sont utilisées pour organiser les programmes en groupes de code réutilisables.
Les fonctions sont définies en utilisant le mot-clé def suivi du nom de la fonction et des parenthèses.

#Fonction break : arrête la boucle avant qu'elle ne soit terminée
#Fonction continue : passe à l'itération suivante de la boucle
#Fonction pass : ne fait rien, mais évite une erreur

#Fonction def(define) : définit une fonction.
#Sert notament de pas répéter le code, et sert beeaucoup dans la factorisation du code.
#Si ont mes 2 même fonction écrasse la première fonction pour afficher la deuxième fonction.

#Fonction def(define) return : renvoie une valeur à partir d'une fonction.



Exemple:
'''

#Variables prenom et nom, dans lesquelles l'utilisateur entre son prénom et son nom, est la fonction input.
prenom = input("Entrez votre prénom: ")
nom = input("Entrez votre nom: ")
print("Bonjour", prenom, " " + nom, "Bienvenue sur le panel administrateur cette espace et réservé aux administrateurs.")

#Type de variable prenom,
#Type affiche le type de variable de la variable donnée.
print(type(prenom))

#Exemple break
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    print("i est maintenant égal à", i)
print("Fin de la boucle")

#Exemple continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    print("i est maintenant égal à", i)
print("Fin de la boucle")

#Exemple pass
i = 0
while i < 5:
    i += 1
    if i == 3:
        pass
    print(i)
    print("i est maintenant égal à", i)
print("Fin de la boucle")

#Exemple def(define)
def table10():
    for i in range(1, 11):
        print(f"{i} x 10 = {i * 10}")
        
table10()

#Exemple def(define) (argument)
def table5(n):
    for i in range(1, 6):
        print(f"{i} x {n} = {i * n}")
table5(5)

#Exemple def(define) prend valeur par défaut
def ditBonjour(nom="John", prenom="Doe", age=25):
    print("Bonjour mon nom et", nom, prenom, "j'ai", age, "ans.")
          
ditBonjour("Smith", "John", 30)

#Exemple def(define) * Liste de mots
def afficheMots(*mots):
    for mot in mots:
        print(mot)
afficheMots("Rouge", "Bleu", "Vert", "Jaune")

#Exemple def(define) return
def addition(nb1, nb2):
    return nb1 + nb2
resultat = addition(5, 3)
print(resultat)

#Exemple de plusieurs valeurs de retour
def calcul(nb1, nb2):
    return nb1 + nb2, nb1 - nb2
print(calcul(25, 12))

(add, sous) = calcul(25, 12)
print (f"Addition: {add}, Soustraction: {sous}")


#Exemple de fonction plusiurs return dans un if, else, elif
def pgq10(n):
    if n > 10:
        return "Plus grand que 10"
    elif n < 10:
        return "Plus petit que 10"  
    else:
        return "Egal à 10"
print(pgq10(11))