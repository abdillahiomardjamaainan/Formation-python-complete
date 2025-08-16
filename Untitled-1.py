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

##les dictionnaires
##un dictionnaire est une collection non ordonnee de paires clé-valeur.
##son utilité est de stocker des données sous forme de paires clé-valeur, permettant un accès rapide aux valeurs via leurs clés.
personne={"nom":"Saad","age":29,"ville":"Paris"}
print(personne)
print(personne["ville"])
print(personne.values())    # Affiche toutes les valeurs du dictionnaire
ETUDIANT={"nom":"Ali","age":23,"note":10}
print(ETUDIANT)
print(ETUDIANT["age"])
ETUDIANT.update({"note":"20"})  # Ajoute une nouvelle clé "note" avec la valeur "20"    
print(ETUDIANT)
ETUDIANT["Ecole"]="Telecom Paris"
print(ETUDIANT)

##Leur utilité dans la vraie vie reel a chacun des cas
##les listes servent servent quand on a besoin de garder une collection d'éléments ordonnée et modifiable.
##exemple dans une entreprise,pour stocker les employés d'une équipe.

##les dictionnaires servent quand on a besoin de stocker des données sous forme de paires clé-valeur.
##exemple dans une application, pour stocker les informations d'un utilisateur (nom, âge, email).  

##Resumé:
##les listes sont des collections ordonnées et modifiables.
##les tuples sont des collections ordonnées et non modifiables.
##les ensembles sont des collections non ordonnées d'éléments uniques.
##les dictionnaires sont des collections non ordonnées de paires clé-valeur.

### les variables
##une variable est un conteneur pour stocker des données.
##elle a un nom et une valeur, et peut être modifiée au cours de l'exécution du programme.
nom = "Alice"
age = 30
print(nom)
print(age)
## les affectation simple,multiple ,parallele
## affectation simple
x = 5
## affectation multiple
a, b, c = 1, 2, 3
## affectation parallèle
d = e = f = 4
##singleton
g = (1,) # Un tuple avec un seul élément
print(g)

id(g)  # Affiche l'identifiant de l'objet g
print(type(g))  # Affiche le type de l'objet g
id(x)  # Affiche l'identifiant de l'objet x

###Les operateurs 
##1.les operateurs arithmétiques
##+,-,*,/,%,**
##ils servent a faire des calculs numériques.
##les operateurs de comparaison
##==,!=,>,<,>=,<=
##ils servent a comparer des valeurs.
age=25
print(age)


##manipuler les chaines des caracteres
##changer la casse
chaine="Bonjour"
print(chaine.lower())  # Convertit la chaîne en minuscules
print(chaine.capitalize())  # Convertit la première lettre en majuscule

###la fonction input
##input sert a lire des entrées utilisateur depuis le clavier
  # Affiche un message de bienvenue avec le nom saisi

age=18
print(f"mon age est {age} ans")
taille=1.75
print(f"ma taille est:{taille} m ")
prenom="saad"
nom="omar"
nom_complet=prenom + " " + nom
print(f"mon nom complet est {nom_complet}")
age=18
if age >= 18:
    print("je suis majeur")
else:
    print("je suis mineur")

print("fin") 

Temperature=30

if Temperature > 25:
    print("il fait chaud")
else:
    print("il fait frais")
print("Bienvenue dans le programme de bienvenue !")

if False:
    print("Bienvenue dans le programme de bienvenue !")
else:
    print("Accès refusé.")

nombre=int(input("Entrez un nombre : "))
if nombre>=0:
    print("Le nombre est positif ou nul.")
else:
    print("Le nombre est négatif.")

mot_de_passe=input("Entrez votre mot de passe : ")
if mot_de_passe=="python123":
    print("Accès autorisé.")
else:
    print("Accès refusé.")

# Demande de l'âge
age = int(input("Quel est votre âge ? "))

if age < 18:
    print("Trop jeune pour participer")
else:
    # Demande si l'utilisateur a une licence
    licence = input("Avez-vous une licence (oui/non) ? ").strip().lower()

    if licence != "oui":
        print("Licence requise")
    else:
        # Demande du niveau
        niveau = input("Quel est votre niveau (débutant/intermédiaire/avancé) ? ").strip().lower()

        if niveau == "avancé":
            print("Résultat : Accès complet")
        elif niveau == "intermédiaire":
            print("Résultat : Accès modéré")
        elif niveau == "débutant":
            print("Résultat : Accès restreint")
        else:
            print("Niveau inconnu")


age = int(input("Quel est votre âge ? "))


if age < 18:
    print("Accès refusé.")
else :
    compte_actif=input("Votre compte est-il actif (oui/non) ? ").strip().lower()
    if compte_actif != "oui":
        print("Accès refusé.")
    else:
        niveau_d_abonnement = input("Quel est votre niveau d'abonnement (bronze/argent/or) ? ").strip().lower()
        if niveau_d_abonnement == "bronze":
            print("Accès limité.")
        elif niveau_d_abonnement == "argent":
            print("Accès standard.")
        elif niveau_d_abonnement == "or":
            print("Accès premium.")
        else:
            print("Niveau inconnu.")



username=input("Entrez votre nom d'utilisateur : ")
users=["admin", "user1", "user2"]
if username in users:
    print("Bienvenue, administrateur !")
else:
    print("error")


###Sytéme de controle d'accès
badge=input("tu as un badge (oui/non) ? ").strip().lower()
if badge != "oui":
    print("Accès refusé.")
else:
    statut=input("Quel est votre statut (employé/visiteur/administrateur) ? ").strip().lower()
    if statut == "employé":
        print("Accés limité")
    elif statut == "administrateur":
        print("Accés total !")
    elif statut == "visiteur":
        print("Accés restreint")

nombre = int(input("Entrez un nombre : "))
if nombre % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")

x=range(5)
print(x)
##les boucles en python sont des structures qui permet d'exécuter plusieurs fois un bloc d'instructions,tant qu'une condition est vrai
#type des boucles
##boucle for
#sert a parcourir une sequence(liste,chaine de caracteres,range)
X=range(5)
for i in X:
    print(i+1)


notes=[10, 15, 12, 18, 14]
compteur_notes = 0
for i in notes:
    if i >= 10:
        print("Note supérieure ou égale à 10 :", i)
    if i >= 15:
        compteur_notes += 1
    print("Note supérieure ou égale à 15 :", compteur_notes)

Clients = ["Alice", "Bob", "Charlie"]
factures = [100, 200, 150]

for i in range(len(Clients)):
    print(f"Client : {Clients[i]}, Facture : {factures[i]}")

#Exercice : Demander à l'utilisateur son nom et son âge, puis afficher un message de bienvenue