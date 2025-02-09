import math

#1 Variable en python.

#Type de variables en python.
#Variable en python sont des objets qui peuvent contenir des valeurs de différents types.
#Les types de variables les plus courants sont:
#- int: entier
#- float: nombre à virgule flottante
#- str: chaîne de caractères
#- bool: booléen (True ou False)
#Exemple:

#Déclaration de variables
a = 1
b = 2.5
c = "Hello"
d = True

#Affichage des variables
print(a) #1
print(b) #2.5
print(c) #Hello
print(d) #True

#Les variables peuvent être modifiées à tout moment.
#Exemple:
a = 5
print(a) #5

#Les variables peuvent être utilisées dans des opérations mathématiques.
#Exemple:
a = 5
b = 3
c = a + b
print(c) #8

#Les variables peuvent être utilisées dans des opérations de chaînes de caractères.
#Exemple:
a = "Hello"
b = "World"
c = a + " " + b
print(c) #Hello World

#Les variables peuvent être utilisées dans des opérations booléennes.
#Exemple:
a = True
b = False
c = a and b
print(c) #False

#Les variables peuvent être utilisées dans des opérations de comparaison.
#Exemple:
a = 5
b = 3
c = a > b
print(c) #True

#Les variables peuvent être utilisées dans des opérations de liste.
#Exemple:
a = [1, 2, 3]
b = a[0]
print(b) #1

#Les variables peuvent être utilisées dans des opérations de dictionnaire.
#Exemple:
a = {"name": "John", "age": 30}
b = a["name"]
print(b) #John

#Les variables peuvent être utilisées dans des opérations de tuple.
#Exemple:
a = (1, 2, 3)
b = a[0]
print(b) #1

#Les variables peuvent être utilisées dans des opérations de set.
#Exemple:
a = {1, 2, 3}
b = 1 in a
print(b) #True

#Les variables peuvent être utilisées dans des opérations de fonction.
#Exemple:
def add(a, b):
    return a + b

c = add(2, 3)
print(c) #5

#Les variables peuvent être utilisées dans des opérations de classe.
#Exemple:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)
print(p.name) #John
print(p.age) #30 1


#2 Les opérations mathématiques en python.

#Les opérations mathématiques de base en python sont les suivantes:
#- Addition: +
#- Soustraction: -
#- Multiplication: *
#- Division: /
#- Division entière: //
#- Modulo: %
#- Puissance: **
#Exemple:

#Addition
a = 5
b = 3
c = a + b
print(c) #8

#Soustraction
a = 5
b = 3
c = a - b
print(c) #2

#Multiplication
a = 5
b = 3
c = a * b
print(c) #15

#Division
a = 5
b = 3
c = a / b
print(c) #1.6666666666666667

#Division entière
a = 5
b = 3
c = a // b
print(c) #1

#Modulo
a = 5
b = 3
c = a % b
print(c) #2

#Puissance
a = 5
b = 3
c = a ** b
print(c) #125

#Les fonctions mathématiques en python sont disponibles dans le module math.
#Exemple:

#Racine carrée
a = 16
b = math.sqrt(a)
print(b) #4.0

#Exponentielle
a = 2
b = math.exp(a)
print(b) #7.3890560989306495

#Logarithme
a = 10
b = math.log(a)
print(b) #2.302585092994046

#Trigonométrie
a = math.pi / 2
b = math.sin(a)
print(b) #1.0

#Les fonctions mathématiques en python peuvent être utilisées dans des opérations mathématiques.
#Exemple:

a = 2
b = 3
c = math.sqrt(a ** 2 + b ** 2)
print(c) #3.605551275463989

#3 Les opérations de chaînes de caractères en python.

#Les opérations de chaînes de caractères en python sont les suivantes:
#- Concaténation: +
#- Répétition: *
#- Longueur: len()
#- Accès aux caractères: []
#- Découpage: [:]
#- Recherche: find()
#- Remplacement: replace()
#- Majuscules: upper()
#- Minuscules: lower()
#- Capitalisation: capitalize()
#- Suppression des espaces: strip()
#Exemple:

#Concaténation
a = "Hello"
b = "World"
c = a + " " + b
print(c) #Hello World

#Répétition
a = "Hello"
b = a * 3
print(b) #HelloHelloHello

#Longueur
a = "Hello"
b = len(a)
print(b) #5

#Accès aux caractères
a = "Hello"
b = a[0]
print(b) #H

#Découpage
a = "Hello"
b = a[1:4]
print(b) #ell

#Recherche
a = "Hello"
b = a.find("l")
print(b) #2

#Remplacement
a = "Hello"
b = a.replace("l", "x")
print(b) #Hexxo

#Majuscules
a = "Hello"
b = a.upper()
print(b) #HELLO

#Minuscules
a = "Hello"

b = a.lower()
print(b) #hello

#Capitalisation
a = "hello"
b = a.capitalize()
print(b) #Hello

#Suppression
a = " Hello "
b = a.strip()
print(b) #Hello

#Les opérations de chaînes de caractères en python peuvent être utilisées dans des opérations de liste.
#Exemple:

a = "Hello"
b = list(a)
print(b) #['H', 'e', 'l', 'l', 'o']

#Les opérations de chaînes de caractères en python peuvent être utilisées dans des opérations de dictionnaire.
#Exemple:

a = "Hello"
b = {i: a[i] for i in range(len(a))}
print(b) #{0: 'H', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}

#Les opérations de chaînes de caractères en python peuvent être utilisées dans des opérations de tuple.
#Exemple:

a = "Hello"
b = tuple(a)
print(b) #('H', 'e', 'l', 'l', 'o')

#Les opérations de chaînes de caractères en python peuvent être utilisées dans des opérations de set.
#Exemple:

a = "Hello"
b = set(a)
print(b) #{'H', 'e', 'l', 'o'}

#Les opérations de chaînes de caractères en python peuvent être utilisées dans des opérations de fonction.
#Exemple:

def reverse(a):
    return a[::-1]

b = reverse("Hello")
print(b) #olleH

#Les opérations de chaînes de caractères en python peuvent être utilisées dans des opérations de classe.
#Exemple:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
p.greet() #Hello, John!

#4 Les opérations booléennes en python.

#Les opérations booléennes en python sont les suivantes:
#- ET: and
#- OU: or
#- NON: not
#Exemple:

#ET
a = True
b = False
c = a and b
print(c) #False

#OU
a = True
b = False
c = a or b
print(c) #True

#NON
a = True
b = not a
print(b) #False

#Les opérations booléennes en python peuvent être utilisées dans des opérations de comparaison.
#Exemple:

a = 5
b = 3
c = a > b and a < 10
print(c) #True

#Les opérations booléennes en python peuvent être utilisées dans des opérations de liste.
#Exemple:

a = [1, 2, 3]
b = 2 in a and 4 not in a
print(b) #True

#Les opérations booléennes en python peuvent être utilisées dans des opérations de dictionnaire.
#Exemple:

a = {"name": "John", "age": 30}
b = "name" in a and "age" in a
print(b) #True

#Les opérations booléennes en python peuvent être utilisées dans des opérations de tuple.
#Exemple:

a = (1, 2, 3)
b = 2 in a and 4 not in a
print(b) #True

#Les opérations booléennes en python peuvent être utilisées dans des opérations de set.
#Exemple:

a = {1, 2, 3}
b = 2 in a and 4 not in a
print(b) #True

#Les opérations booléennes en python peuvent être utilisées dans des opérations de fonction.
#Exemple:

def is_even(a):
    return a % 2 == 0

b = is_even(4) and not is_even(3)
print(b) #True

#Les opérations booléennes en python peuvent être utilisées dans des opérations de classe.
#Exemple:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

p = Person("John", 30)
b = p.is_adult() and p.name == "John"
print(b) #True

#5 Les opérations de comparaison en python.

#Les opérations de comparaison en python sont les suivantes:
#- Égalité: ==
#- Différence: !=
#- Inférieur: <
#- Inférieur ou égal: <=
#- Supérieur: >
#- Supérieur ou égal: >=
#Exemple:

#Égalité
a = 5
b = 5
c = a == b
print(c) #True

#Différence
a = 5
b = 3
c = a != b
print(c) #True

#Inférieur
a = 5
b = 3
c = a < b
print(c) #False

#Inférieur ou égal
a = 5
b = 5
c = a <= b
print(c) #True

#Supérieur
a = 5
b = 3
c = a > b
print(c) #True

#Supérieur ou égal
a = 5
b = 5
c = a >= b
print(c) #True

#Les opérations de comparaison en python peuvent être utilisées dans des opérations de liste.
#Exemple:

a = [1, 2, 3]
b = len(a) == 3
print(b) #True


#Les opérations de comparaison en python peuvent être utilisées dans des opérations de dictionnaire.
#Exemple:

a = {"name": "John", "age": 30}
b = "name" in a and "age" in a
print(b) #True

#Les opérations de comparaison en python peuvent être utilisées dans des opérations de tuple.
#Exemple:

a = (1, 2, 3)
b = len(a) == 3
print(b) #True

#Les opérations de comparaison en python peuvent être utilisées dans des opérations de set.
#Exemple:

a = {1, 2, 3}
b = len(a) == 3
print(b) #True

#Les opérations de comparaison en python peuvent être utilisées dans des opérations de fonction.
#Exemple:

def is_even(a):
    return a % 2 == 0

b = is_even(4)
print(b) #True

#Les opérations de comparaison en python peuvent être utilisées dans des opérations de classe.
#Exemple:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

p = Person("John", 30)
b = p.is_adult()
print(b) #True

#6 Les opérations de liste en python.

#Les opérations de liste en python sont les suivantes:
#- Ajout: append()


#Exemple:

#Ajout
a = [1, 2, 3]
a.append(4)
print(a) #[1, 2, 3, 4]

#Les opérations de liste en python peuvent être utilisées dans des opérations de dictionnaire.
#Exemple:

a = [1, 2, 3]
b = {i: a[i] for i in range(len(a))}
print(b) #{0: 1, 1: 2, 2: 3}

#Les opérations de liste en python peuvent être utilisées dans des opérations de tuple.
#Exemple:

a = [1, 2, 3]
b = tuple(a)
print(b) #(1, 2, 3)


#Les opérations de liste en python peuvent être utilisées dans des opérations de set.
#Exemple:

a = [1, 2, 3]
b = set(a)
print(b) #{1, 2, 3}

#Les opérations de liste en python peuvent être utilisées dans des opérations de fonction.
#Exemple:

def reverse(a):
    return a[::-1]

b = reverse([1, 2, 3])
print(b) #[3, 2, 1]

#Les opérations de liste en python peuvent être utilisées dans des opérations de classe.
#Exemple:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
p.greet() #Hello, John!

#7 Les opérations de dictionnaire en python.

#Les opérations de dictionnaire en python sont les suivantes:
#- Ajout: []
#- Suppression: del
#- Longueur: len()
#- Accès aux éléments: []
#- Parcours: items()
#Exemple:

#Ajout
a = {"name": "John", "age": 30}
a["city"] = "New York"
print(a) #{'name': 'John', 'age': 30, 'city': 'New York'}

#Suppression
a = {"name": "John", "age": 30}
del a["age"]
print(a) #{'name': 'John'}

#Longueur
a = {"name": "John", "age": 30}

b = len(a)
print(b) #2

#Accès aux éléments
a = {"name": "John", "age": 30}
b = a["name"]
print(b) #John

#Parcours
a = {"name": "John", "age": 30}
for key, value in a.items():
    print(key, value)

#name John
#age 30

#Les opérations de dictionnaire en python peuvent être utilisées dans des opérations de tuple.
#Exemple:

a = {"name": "John", "age": 30}
b = tuple(a)
print(b) #('name', 'age')

#Les opérations de dictionnaire en python peuvent être utilisées dans des opérations de set.
#Exemple:

a = {"name": "John", "age": 30}
b = set(a)
print(b) #{'name', 'age'}

#Les opérations de dictionnaire en python peuvent être utilisées dans des opérations de fonction.
#Exemple:

def reverse(a):
    return {value: key for key, value in a.items()}

b = reverse({"name": "John", "age": 30})
print(b) #{'John': 'name', 30: 'age'}

#Les opérations de dictionnaire en python peuvent être utilisées dans des opérations de classe.
#Exemple:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John", 30)
b = {key: value for key, value in p.__dict__.items()}
print(b) #{'name': 'John', 'age': 30}

#8 Les opérations de tuple en python.

#Les opérations de tuple en python sont les suivantes:
#- Longueur: len()
#- Accès aux éléments: []
#- Parcours: enumerate()
#Exemple:

#Longueur
a = (1, 2, 3)
b = len(a)
print(b) #3

#Accès aux éléments
a = (1, 2, 3)
b = a[0]
print(b) #1

#Parcours
a = (1, 2, 3)
for i, value in enumerate(a):
    print(i, value)

#0 1
#1 2
#2 3

#Les opérations de tuple en python peuvent être utilisées dans des opérations de set.
#Exemple:

a = (1, 2, 3)
b = set(a)
print(b) #{1, 2, 3}

#Les opérations de tuple en python peuvent être utilisées dans des opérations de fonction.
#Exemple:

def reverse(a):
    return a[::-1]

b = reverse((1, 2, 3))
print(b) #(3, 2, 1)

#Les opérations de tuple en python peuvent être utilisées dans des opérations de classe.
#Exemple:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
p.greet() #Hello, John!

#9 Les opérations de set en python.

#Les opérations de set en python sont les suivantes:
#- Ajout: add()
#- Suppression: remove()
#- Longueur: len()
#- Parcours: for
#Exemple:

#Ajout
a = {1, 2, 3}
a.add(4)
print(a) #{1, 2, 3, 4}

#Suppression
a = {1, 2, 3}
a.remove(2)
print(a) #{1, 3}

#Longueur
a = {1, 2, 3}
b = len(a)
print(b) #3

#Parcours
a = {1, 2, 3}
for value in a:
    print(value)

#1
#2
#3

#Les opérations de set en python peuvent être utilisées dans des opérations de fonction.
#Exemple:

def reverse(a):
    return {value for value in a}

b = reverse({1, 2, 3})
print(b) #{1, 2, 3}

#Les opérations de set en python peuvent être utilisées dans des opérations de classe.
#Exemple:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
p.greet() #Hello, John!

#10 Les opérations de fonction en python.

#Les opérations de fonction en python sont les suivantes:
#- Définition: def
#- Appel: ()
#- Arguments: ()
#- Valeur de retour: return
#Exemple:

#Définition
def add(a, b):
    return a + b

#Appel
c = add(2, 3)
print(c) #5

#Arguments
def add(a, b):
    return a + b

c = add(2, 3)
print(c) #5

#Valeur de retour
def add(a, b):
    return a + b

c = add(2, 3)
print(c) #5

#Les opérations de fonction en python peuvent être utilisées dans des opérations de classe.
#Exemple:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
p.greet() #Hello, John!

#11 Les opérations de classe en python.

#Les opérations de classe en python sont les suivantes:
#- Définition: class
#- Constructeur: __init__()
#- Méthodes: def
#- Attributs: self.
#Exemple:

#Définition
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

#Constructeur
p = Person("John")
p.greet() #Hello, John!

#Méthodes
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
p.greet() #Hello, John!

#Attributs
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
p.greet() #Hello, John!

#Les opérations de classe en python peuvent être utilisées dans des opérations de fonction.
#Exemple:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
p.greet() #Hello, John!

#Les opérations de classe en python peuvent être utilisées dans des opérations
#de liste.
#Exemple:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
p.greet() #Hello, John!

#Les opérations de classe en python peuvent être utilisées dans des opérations de dictionnaire.
#Exemple:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
b = {key: value for key, value in p.__dict__.items()}
print(b) #{'name': 'John'}

#Les opérations de classe en python peuvent être utilisées dans des opérations de tuple.
#Exemple:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
b = tuple(p.__dict__.values())
print(b) #('John',)

#Les opérations de classe en python peuvent être utilisées dans des opérations de set.
#Exemple:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
b = set(p.__dict__.values())
print(b) #{'John'}

#Les opérations de classe en python peuvent être utilisées dans des opérations de fonction.
#Exemple:

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
p.greet() #Hello, John!

#12 Conclusion
#Les variables en python sont des objets qui peuvent contenir des valeurs de différents types.
#Les types de variables les plus courants sont: int, float, str, bool.
#Les opérations mathématiques de base en python sont les suivantes: +, -, *, /, //, %, **.
#Les fonctions mathématiques en python sont disponibles dans le module math.
#Les opérations de chaînes de caractères en python sont les suivantes: +, *, len(), [], [:], find(), replace(), upper(), lower(), capitalize(), strip().
#Les opérations booléennes en python sont les suivantes: and, or, not.
#Les opérations de comparaison en python sont les suivantes: ==, !=, <, <=, >, >=.
#Les opérations de liste en python sont les suivantes: append().
#Les opérations de dictionnaire en python sont les suivantes: [], del, len(), [].
#Les opérations de tuple en python sont les suivantes: len(), [], enumerate().
#Les opérations de set en python sont les suivantes: add(), remove(), len(), for.
#Les opérations de fonction en python sont les suivantes: def, (), (), return.
#Les opérations de classe en python sont les suivantes: class, __init__(), def, self.
#Les variables en python peuvent être utilisées dans des opérations mathématiques, de chaînes de caractères, booléennes, de
#comparaison, de liste, de dictionnaire, de tuple, de set, de fonction, de classe.
#Les fonctions mathématiques en python peuvent être utilisées dans des opérations mathématiques.
#Les opérations de chaînes de caractères en python peuvent être utilisées dans des opérations de liste, de dictionnaire, de tuple, de set, de fonction, de classe.
#Les opérations booléennes en python peuvent être utilisées dans des opérations de comparaison, de liste, de dictionnaire, de tuple, de set, de fonction, de classe.
#Les opérations de comparaison en python peuvent être utilisées dans des opérations de liste, de dictionnaire, de tuple, de set, de fonction, de classe.
#Les opérations de liste en python peuvent être utilisées dans des opérations de dictionnaire, de tuple, de set, de fonction, de classe.
#Les opérations de dictionnaire en python peuvent être utilisées dans des opérations de tuple, de set, de fonction, de classe.
#Les opérations de tuple en python peuvent être utilisées dans des opérations de set, de fonction, de classe.
#Les opérations de set en python peuvent être utilisées dans des opérations de fonction, de classe.
#Les opérations de fonction en python peuvent être utilisées dans des opérations de classe.
#Les opérations de classe en python peuvent être utilisées dans des opérations de fonction, de liste, de dictionnaire, de tuple, de set.

#Fin de la documentation.