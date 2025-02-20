"""

Les Fonction lambda sont des fonctions anonymes, c'est-à-dire des fonctions sans nom.

Syntaxe:
lambda arguments: <arg1> + <arg2> <instruction>


def carrer(x): #Pas néccesaire 
    return x * x 
-------------------------------------------------------------------------------------

"""

carrer = lambda x: x * x

print(carrer(5))

#Autre exemple:
addition = lambda nb1, nb2: nb1 + nb2
print(addition(5, 3))