#Les opérateur logique :
#Sont des opérateurs qui permettent de combiner des expressions booléennes.

#Opérateur logique
#not n'es pas (inverse la valeur de l'expression booléenne)
#and et logique (si les deux sont vrai alors c'est vrai)
#or ou logique (si une des deux est vrai alors c'est vrai)

username = "admin"
password = "admin123"

print("__________PANEL LOGIN__________")
usernameInput = input("Enter your username: ")
passwordInput = input("Enter your password: ")

if usernameInput == username and passwordInput == password:
    print("Login successful")
else:
    print("Login failed")


