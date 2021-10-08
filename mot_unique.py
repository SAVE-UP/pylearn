# Cet script retourne les mots unique d'un fichier en retirant les doublons et
# les signes de ponctuations
"""
Les fichiers
Les Listes
L'utilisation de set()
Boucles For
"""

fichier = open('fichiers\chanson.txt', 'r')
allcontent = fichier.read()
# Remplacement de tout les signes de ponctuations
ponct = [',', '.', ';', "'", '?', '...', ':', '«', '»', '!', '—', '-']
for signe in ponct:
        allcontent = allcontent.replace(signe, '')
# Tout les mots sont passer en minisculle (lower()) puis on supprime les espaces en début et fin (strip()) enfin 
# On transforme tout en liste de mot individuel (split()) on enregistre tout dans un set()
db = set(allcontent.lower().strip().split()) #convertie la liste [] content en un élément set().
for x in db:
        print(x)
