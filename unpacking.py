# Explication de la notion de unpacking en python
# Author: Mawuena

# Notion Unpacking(Débalage en Fr) en Python
x, y, z  = (1, 2, 3) # Python assigne automatiquement 1 à x, 2 à y et 3 à z
# cela marche avec tout itterable: les tuples, les listes, les chaine de caratères et les set
x, y, z  = [1, 2, 3]
x, y, z  = set((1, 2, 3))
x, y, z  = 'abc'
# Il faut bien s'assurrer que le nombre de variable à gauche est égale au nombre d'élément dans l'itérable
x, y , *z = range(100) # stock le premier element dans x, le second dan y et le reste(*) dans z

# L'unpacking intervient aussi dans les fonctions`
    # 1 A niveau des arguments des fonctions
    def ajouter(a, b):
        return a+b
    # Façon classique d'appeler la fonction ajouter
    ajouter(2,3)
    # Avec l'unpacking
    note = [2, 3]
    ajouter(*note) # Ceci va automatiquement assigner la premiere valeur de la liste au premier paramètre de 
    # la fonction ainsi de suite.
    # Il faut bien s'assurrer que le nombre de paramètres équivaut au nombre d'élément de l'iterable
    note = {'s1': 2,'s2': 3}
    ajouter(**note) # Avec les dictonaires c'est deux ** => ajouter(s1= 2, s2 =3)

    # 2 A niveau des valeurs de retour des fonctions
    def carre(a=0,b=0):
        """Cette fonction retourne le carré de 2 nombres"""
        return a*a, b*b
    A, B = carre() # => A = a*a et B = b*b