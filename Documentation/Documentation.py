import gc
import math
import threading
from functools import reduce

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

# Puissance (Exponentiation)
a = 5
b = 3
c = a ** b
print(c) # 125

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

#Suppression del
a = {"name": "John", "age": 30}
del a["age"]
print(a) #{'name': 'John'}

#Longueur len
a = {"name": "John", "age": 30}

b = len(a)
print(b) #2

#Accès aux éléments
a = {"name": "John", "age": 30}
b = a["name"]
print(b) #John

#Parcours items
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

#Longueur len
a = (1, 2, 3)
b = len(a)
print(b) #3

#Accès aux éléments
a = (1, 2, 3)
b = a[0]
print(b) #1

#Parcours enumerate
a = (1, 2, 3)
for i, value in enumerate(a):
    print(i, value)

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

#Ajout add
a = {1, 2, 3}
a.add(4)
print(a) #{1, 2, 3, 4}

#Suppression remove
a = {1, 2, 3}
a.remove(2)
print(a) #{1, 3}

#Longueur len
a = {1, 2, 3}
b = len(a)
print(b) #3

#Parcours for
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

#Définition def
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

#Valeur de retour return
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

#Définition class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

#Constructeur init
p = Person("John")
p.greet() #Hello, John!

#Méthodes def
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name + "!")

p = Person("John")
p.greet() #Hello, John!

#Attributs self
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


#13 Les opérations de module en python.

#Les opérations de module en python sont les suivantes:

#- Importation: import
#- Utilisation: .
#Exemple:

#Importation
#Utilisation
a = math.sqrt(16)
print(a) #4.0

#Les opérations de module en python peuvent être utilisées dans des opérations de fonction.

#Exemple:
def square_root(a):
    return math.sqrt(a)

b = square_root(16)
print(b) #4.0

#Les opérations de module en python peuvent être utilisées dans des opérations de classe.

#Exemple:
class Math:
    def square_root(self, a):
        return math.sqrt(a)

m = Math()
b = m.square_root(16)
print(b) #4.0

#14 Les opérations de fichier en python.

#Les opérations de fichier en python sont les suivantes:
#- Ouverture: open()
#- Lecture: read()
#- Écriture: write()
#- Fermeture: close()
#Exemple:

#Ouverture open
f = open("file.txt", "w")

#Écriture write
f.write("Hello, World!")

#Fermeture close
f.close()

#Les opérations de fichier en python peuvent être utilisées dans des opérations de fonction.
#Exemple:

def read_file(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return content

b = read_file("file.txt")
print(b) #Hello, World!

#15 Les opérations d'exception en python.

#Les opérations d'exception en python sont les suivantes:
#- Gestion: try, except
#- Lancement: raise
#Exemple:

#Gestion
try:
    a = 1 / 0
except ZeroDivisionError:
    print("Division par zéro!")

#Lancement
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division par zéro!")
    return a / b

try:
    c = divide(1, 0)
except ZeroDivisionError as e:
    print(e)

#16 Les opérations de thread en python.

#Les opérations de thread en python sont les suivantes:
#- Création: Thread
#- Démarrage: start()
#- Attente: join()
#Exemple:

#Création Tread
class MyThread(threading.Thread):
    def run(self):
        print("Hello, World!")

#Démarrage start
t = MyThread()
t.start()

#Attente join
t.join()

#17 Les opérations de décorateur en python.

#Les opérations de décorateur en python sont les suivantes:
#- Définition: def
#- Utilisation: @
#Exemple:

#Définition
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

#Utilisation
@uppercase
def greet(name):
    return "Hello, " + name + "!"

print(greet("John")) #HELLO, JOHN!

#18 Les opérations de générateur en python.

#Les opérations de générateur en python sont les suivantes:
#- Définition: def
#- Rendement: yield
#Exemple:

#Définition
def count(n):
    for i in range(n):
        yield

#Rendement
for i in count(3):
    print(i)

#0
#1
#2

#19 Les opérations d'itérateur en python.

#Les opérations d'itérateur en python sont les suivantes:
#- Définition: class
#- Méthodes: def
#Exemple:

#Définition class
class Count:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

#Méthodes def
for i in Count(3):
    print(i)


#20 Les opérations de contexte en python.

#Les opérations de contexte en python sont les suivantes:

#- Définition: class

#- Méthodes: def

#Exemple:

#Définition class

class File:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()

#Méthodes def

with File("file.txt") as f:
    f.write("Hello, World!")

#21 Les opérations de gestion de mémoire en python.

#Les opérations de gestion de mémoire en python sont les suivantes:
#- Référence: del
#- Ramasse-miettes: gc.collect()
#Exemple:

#Référence del

a = [1, 2, 3]
b = a
del a
print(b) #[1, 2, 3]

#Ramasse-miette gc.collect
a = [1, 2, 3]
b = a
del a
gc.collect()

#22 Les opérations de programmation orientée objet en python.

#Les opérations de programmation orientée objet en python sont les suivantes:
#- Classe: class
#- Constructeur: __init__()
#- Méthodes: def
#- Attributs: self.
#Exemple:

#Classe
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

#23 Les opérations de programmation fonctionnelle en python.

#Les opérations de programmation fonctionnelle en python sont les suivantes:
#- Fonctions: lambda
#- Fonctions: map()
#- Fonctions: filter()
#- Fonctions: reduce()
#Exemple:

#Fonctions lambda
add = lambda a, b: a + b
print(add(2, 3)) #5

#Fonctions map
a = [1, 2, 3]
b = list(map(lambda x: x * 2, a))
print(list(b)) #[2, 4, 6]

#Fonctions filter
a = [1, 2, 3]
b = filter(lambda x: x % 2 == 0, a)
print(list(b)) #[2]

#Fonctions reduce
a = [1, 2, 3]
b = reduce(lambda x, y: x + y, a)
print(b) #6

#24 Les opérations de programmation impérative en python.

#Les opérations de programmation impérative en python sont les suivantes:
#- Instructions: if, else, elif
#- Instructions: for, while
#- Instructions: break, continue
#Exemple:

#Instructions if, else, elif
a = 5
if a > 0:
    print("Positive")
else:
    print("Negative")

#Instructions for, while
a = [1, 2, 3]
for i in a:
    print(i)

#Instructions break, continue
a = 5

while a > 0:
    print(a)
    a -= 1

a = [1, 2, 3]

for i in a:

    if i == 2:
        break
    print(i)

#25 Les opérations de programmation déclarative en python.

#Les opérations de programmation déclarative en python sont les suivantes:
#- Expressions: list, set, dict
#- Expressions: comprehension
#- Expressions: generator
#Exemple:

#Expressions list, set, dict
a = [1, 2, 3]
b = [x * 2 for x in a]
print(b) #[2, 4, 6]

#Expressions comprehension
a = [1, 2, 3]
b = {x * 2 for x in a}
print(b) #{2, 4, 6}

#Expressions generator
a = [1, 2, 3]
b = {x: x * 2 for x in a}
print(b) #{1: 2, 2: 4, 3: 6}


#26 Les opérations de programmation procédurale en python.

#Les opérations de programmation procédurale en python sont les suivantes:
#- Procédures: def
#- Variables: global
#Exemple:

#Procédures def
def greet(name):
    print("Hello, " + name + "!")

greet("John") #Hello, John!

#Variables global
a = 5

def add(b):
    global a
    a += b
    return a

print(add(3)) #8

#27 Les opérations de programmation structurée en python.

#Les opérations de programmation structurée en python sont les suivantes:
#- Blocs: if, else, elif
#- Blocs: for, while
#- Blocs: def
#Exemple:

#Blocs if, else, elif
a = 5
if a > 0:
    print("Positive")
else:
    print("Negative")

#Blocs for, while
a = [1, 2, 3]
for i in a:
    print(i)

#Blocs def
def greet(name):
    print("Hello, " + name + "!")

greet("John") #Hello, John!

#28 Les opérations de programmation procédurale en python.

#Les opérations de programmation procédurale en python sont les suivantes:
#- Procédures: def
#- Variables: global
#Exemple:

#Procédures
def greet(name):
    print("Hello, " + name + "!")
greet("John") #Hello, John!

#Variables
a = 5
def add(b):
    global a
    a += b
    return a
print(add(3)) #8



#12 Conclusion documentation.

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
#Les variables en python peuvent être utilisées dans des opérations mathématiques, de chaînes de caractères, booléennes, de comparaison, de liste, de dictionnaire, de tuple, de set, de fonction, de classe.
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
#Les opérations de module en python peuvent être utilisées dans des opérations de fonction, de classe.
#Les opérations de fichier en python peuvent être utilisées dans des opérations de fonction.
#Les opérations d'exception en python peuvent être utilisées dans des opérations de fonction.
#Les opérations de décorateur en python peuvent être utilisées dans des opérations de fonction.
#Les opérations de générateur en python peuvent être utilisées dans des opérations de fonction.
#Les opérations d'itérateur en python peuvent être utilisées dans des opérations de fonction.
#Les opérations de contexte en python peuvent être utilisées dans des opérations de fonction.
#Les opérations de gestion de mémoire en python peuvent être utilisées dans des opérations de fonction.
#Les opérations de programmation orientée objet en python peuvent être utilisées dans des opérations de fonction, de liste, de dictionnaire, de tuple, de set.
#Les opérations de programmation fonctionnelle en python peuvent être utilisées dans des opérations de fonction.
#Les opérations de programmation impérative en python peuvent être utilisées dans des opérations de fonction.
#Les opérations de programmation structurée en python peuvent être utilisées dans des opérations de fonction.
#Les opérations de programmation procédurale en python peuvent être utilisées dans des opérations de fonction.
#Les opérations de programmation déclarative en python peuvent être utilisées dans des opérations de fonction.



