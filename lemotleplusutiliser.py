# Cet exercice à pour but de trouver le mot le plus utiliser dans un 
# répertoire donnés(ie: Documents, Bureau, Telechargements)
# Par défaut utilise le répertoire courant

from pathlib import Path
# fichiers = Path.cwd().joinpath('fichiers')
# iterdir(self) # Renvoie vers un generateur contenant tout les liens(absolut) des fichiers du répertoire en question
stats = {} # Dictionnaire vide

def denombr(fichier):
    """ Cette fonction denombre tout les mots contenue dans un fichier avec répétition et renvoie tout dans une liste """
    f = open(fichier, 'r')
    allcontent = f.read()
    ponct = [',', '.', ';', "'", '?', '...', ':', '«', '»', '!', '—', '-', '#']
    for signe in ponct:
        allcontent = allcontent.replace(signe, '')
    mots = list(allcontent.lower().strip().split())
    return mots
  

for fichier in Path.cwd().joinpath('fichiers').iterdir(): # Cette boucle renvoie un a un vers chaque fichier du répertoire.
    mots = denombr(fichier)
    for mot in mots: # Cette boucle compte chaque fois qu'apparait un nouveau mot et, incremente de 1 si le mot exite déjà dans le dictionaire.
        if mot not in stats:
            stats[mot] = 1
        elif mot in stats:
            stats[mot] +=  1
            
# import pdb; pdb.set_trace()  # Debugger python - BreakPoint 

maximal,key = 0,None
for key, valeur in stats.items(): # Cette boucle parcours la paire key, valeur et retourne la pair key/valeur pour lequel  la valeur est maximal
    if maximal < valeur:
        maximal = valeur
        motp = key 

print('«',motp,"» est le mot le plus utilié avec un score de:", maximal)