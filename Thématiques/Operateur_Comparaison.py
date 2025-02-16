#Operateur de comparaison
#Les opérateurs de comparaison permettent de comparer deux valeurs. Ils renvoient un booléen, c'est-à-dire une valeur qui est soit True (vrai) soit False (faux).

#Opérateur	Description

#==	Égal à
#!=	Différent de
#>	Supérieur à
#<	Inférieur à
#>=	Supérieur ou égal à
#<=	Inférieur ou égal à

#Exemple 1
a = 10
if a > 5:
    print("a est supérieur à 5")
else:
    print("a est inférieur à 5")

#Exemple 2
a = 10
if a > 5:
    print("a est supérieur à 5")

#Exemple 3
a = 10

if a > 5:
    print("a est supérieur à 5")
elif a < 5:
    print("a est inférieur à 5")
else:
    print("a est égal à 5")