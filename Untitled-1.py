print("Hello, World!")
a=5+10
print(a)
print(a+5)
b=20
print(b)
c=a+b
print(c)
d=10
print(d)
w=4+5
print(w)
##Definition des types des données
# Entier (int)
# Flottant (float)
# Chaîne de caractères (str)
# Booléen (bool)
a="Saad"
type(a)
print(type(a))

##Explication complete sur les differents types des chaine de caractères existant
# Les chaînes de caractères (str) en Python sont des séquences de caractères utilisées pour représenter du texte.
# Elles peuvent être définies en utilisant des guillemets simples (' ') ou des guillemets doubles (" ").
# Voici quelques exemples de chaînes de caractères :
# 1. Chaîne de caractères simple
nom="Abdillahi"
prenom="Saad"
# 2.chaine de caractere avec  des guillemets inclus
phrase1="c'est une belle journée"
print(phrase1)
phrase2='il dit "bonjour"!'
print(phrase2)
##chaine des caractére speciaux
##nouvelle ligne
phrase3="bonjour\nPython"
print(phrase3)
o="c'est super"
print(o)
age=45
T="j'ai"+" " + str(age) + " " + "ans"
print(T)
print(T[-1])
print(T[0:5])
print(T[0:5:2])  # Affiche les caractères de l'index 0 à 5 avec un pas de 2 
p="ABDILLAHI OMAR DJAMA"
print(p)
print(p[0:5:3])  # 
K="Python"
print(K[2:6:3])

O="ABDILLAHI"
print(O[3:8:3])

##Nombre entier
##un nombre entier est un nombre sans virgule,peut etre negatif ou positif ou zero.
l=5
print(l)    
##les differents operations possible
V=9
print(l+V)  # Addition
print(l-V)  # Soustraction
print(l*V)  # Multiplication
print(l/V)  # Division
print(l%V)  # Modulo (reste de la division) 
print(l**V) # Puissance (l élevé à la puissance V)
print(l//V) # Division entière (quotient de la division)
True+2
print(str(10))
print(type(str(10)))  # Affiche le type de la variable après conversion en chaîne de caractères

##les principales fonctions de conversion de type
##vers int
##si c'est un float il enleve la partie decimal et si c'est une chaine de caractere il convertit si c'est possible
##exemple
print(int(10.5))
print(int("20"))  # Convertit la chaîne "20" en entier
##vers float
print(float(10))  # Convertit l'entier 10 en flottant
##vers une chaine de caracteres
print(str(10))  # Convertit l'entier 10 en chaîne de caractères

##1.les listes 
##une liste est une collection ordonnéé modifiable.
##"exemple"
fruits=["pomme", "banane", "cerise"]
print(fruits[0:2:2])
fruits.append("orange")  # Ajoute "orange" à la fin de la liste 
fruits.remove("banane")  # Supprime "banane" de la liste
fruits.insert(1, "kiwi")  # Insère "kiwi" à l'index 1
print(fruits)  # Affiche la liste mise à jour
##Exos:crée une liste contenant les nombres 1;2;3;4;5n,=[1,2,3,4,5,6]
nombres = [1, 2, 3, 4, 5, 6]
print(nombres)
print(nombres[0])
nombres.append(7)
nombres.remove(2)
print(nombres)
##l'utilité des listes est de pouvoir stocker plusieurs valeurs dans une seule variable et les manipuler facilement.

##2.les tuples
##un tuple est une collection ordonnée mais non modifiables.
##son utilité est de regrouper des valeurs heterogene et ordonnées mais non modifiables.des valeurs fixes tels que les coordonnées (x, y) d'un point dans un plan.
coordonnees = (10, 10)  # Un tuple représentant les coordonnées (x, y)
print(coordonnees)
print(coordonnees[0])  # Affiche la première valeur du tuple
coordonnees = (30, 30)  # Redéfinition du tuple avec de nouvelles coordonnées
print(coordonnees)  # Affiche le nouveau tuple
print(coordonnees.count(30))  # Compte le nombre d'occurrences de 30 dans le tuple

##les ensembles (set)
##un ensemble est une collection non ordonnée d'éléments uniques.
##son utilité est de stocker des valeurs sans ordre particulier et sans doublons.
nb={1,2,3,4}
bn={5,6,7,8}
print(nb)
print(bn)
print(nb.union(bn))
nb.add(5)  # Ajoute l'élément 5 à l'ensemble nb

##les opérations sur les ensembles
print(nb.intersection(bn))  # Affiche les éléments communs aux deux ensembles
print(nb.difference(bn))  # Affiche les éléments présents dans nb mais pas dans bn
print(nb.issubset(bn))  # Vérifie si nb est un sous-ensemble de bn
print(nb.issuperset(bn))  # Vérifie si nb est un sur-ensemble de bn 