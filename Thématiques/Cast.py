'''
Le cast en python, ça consiste à changer le type d'une variable.

Les variables en python:

int: entier
float: nombre à virgule flottante
str: chaîne de caractères
bool: booléen (True ou False)
'''


#Exemple: ERROR /!\
#print(type(nombre + 5)) ERROR CAST STR NON CONVERTIT EN INT /!\

#Exemple: Cast int
#Cast int
nombre = input("Quel et le nombres ? ") #Input
nombre = int(nombre) #Cast le type de variable à la source
print(int(nombre) + 30) #Cast str -> int
print(type(nombre)) #Voir si ça a bien cast

#Exemple: cast float
#Cast float
nombreF = input("Quel et le nombre floattant ? ") #Input
nombreF = float(nombreF) #Cast le type de la variable à la source
print(float(nombreF) + 30.5) #Cast str -> float
print(type(nombreF)) #Voir si ça a bien cast


#Exemple: Cast Boolean
#Cast boolean
femmmeHomme = 0 #Valeur false = 0 -> True = 1
femmmeHomme = bool (femmmeHomme) #Cast le type boolean
print(femmmeHomme) #print false


