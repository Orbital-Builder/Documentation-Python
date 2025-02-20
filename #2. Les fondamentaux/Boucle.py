"""

Les boucle en python sont :

 while condition:
     instruction
 for variable en sequence:
     instruction
 
 range : génère une séquence de nombres

while : tant que la condition est vraie, on exécute les instructions (tant que)
for : pour chaque élément de la séquence, on exécute les instructions (pour)
-------------------------------------------------------------------------------

"""

#while
i = 0
while i < 5:
    print(i)
    i += 1
    print("i est maintenant égal à", i)

#for
for i in range(5):
    print(i)
else: #else est optionnel, else est exécuté une fois que la boucle est terminée
    print("Fin de la boucle") #Affiche "Fin de la boucle"
