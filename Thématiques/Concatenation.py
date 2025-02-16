#La concaténation est une opération qui consiste à mettre bout à bout deux chaînes de caractères.

# Exemple de concaténation
# Concaténation de deux chaînes de caractères
chaine1 = "Bonjour"
chaine2 = "tout le monde"
chaine3 = chaine1 + " " + chaine2
print(chaine3)
# Résultat: Bonjour tout le monde

#Cast concatenation
#Concaténation de chaînes de caractères et d'entiers
chaine = "Le nombre est "
nombre = 5
chaine = chaine + str(nombre)
print(chaine)
# Résultat: Le nombre est 5

#.format concatenation
chaine = "Le nombre est {}".format(nombre)
print(chaine)
# Résultat: Le nombre est 5

#format autre manière {f} concatenation
chaine = f"Le nombre est {nombre}"
print(chaine)