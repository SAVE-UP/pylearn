#Script permettant de changer un ou plusieurs mot d'un fichier  par un autre
from pathlib import Path
# fichier = open('fichiers\chanson.txt', 'r')
fichier, nfichier = 'chanson.txt',"nchanson.txt"
def remplacer_mots(fichier, nfichier,**kwords):
    """ Remplacer_mots remplace les mots d'un texte et le réécrit dans un autre

        Utilisation:
        remplacer_mots('chanson.txt', 'nchant.txt', plume="stylo", lune = "soleil", le = "la")    
    """
    path = Path.cwd().joinpath('fichiers', fichier)
    npath = Path.cwd().joinpath('fichiers', nfichier)
    try:
        with open(path, mode='r') as f:
            content = f.read()
            for old, new in kwords.items():
                content = content.replace(old,new)
    except EnvironmentError as e:
        print("Impossible d'ouvrir le fichier %s : %s" %(fichier, e))
    try:
        with open(npath, mode='x') as n:
            n.write(content)
    except EnvironmentError as ee:
        print("Impossible de creer le fichier %s: %s " %(nfichier, ee))
    return 0
    open