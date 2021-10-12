import sys, pathlib
from pathlib import Path
import sqlite3
import collections

# Obtenir le dossier du Profil par un Parsing d'argument au programme. 
# Leve une Erreur quand il n'y a pas d'argument.
try:
    pathProfil = pathlib.Path(sys.argv[1])
except IndexError:
    sys.exit("/!\ Vous devez passer un dossier de profil en paramètre")

# Obtenir le chemin complet vers la BD(places.sqlite) contenant l'historique du navigateur
histo = pathProfil.joinpath('places.sqlite')

# Leve et Affiche une Erreur quand le fichier est introuvable.
if not Path.is_file(histo):
    sys.exit("/!\ Impssible de trouver le fichier " + str(histo))

# Connexion à la BD sqlite.
dbConnect = sqlite3.connect(str(histo))
cuseur = dbConnect.cursor()

# Requête SQL qui renvoi la liste de chaque visite sur
# les sites visités 
requete = """
SELECT moz_places.rev_host 
    FROM moz_historyvisits, moz_places 
    WHERE moz_places.id == moz_historyvisits.place_id
"""
resultat = cuseur.execute(requete)

# on remet le nom du site dans le bon ordre, et
# on retire les "." et "www" superflux
g = [ligne[0][-2::-1].replace('www.','') for ligne in resultat]

# le compteur compteur chaque visite pour nous
compteur = collections.Counter(g)

#Affichage
for site, point in compteur.most_common(12):
    if site == 'localhost' or site == '0.0.0.0':
        continue
    print("- ", site, ":", point)