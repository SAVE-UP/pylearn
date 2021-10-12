#Mini-Sondage
#usage des Dictionnaires et des boucles en python
stock = {} # Initailisation du dictionnaire!
i = 0
couleur = None
while couleur != "":
    couleur = str(input("Veillez saisir votre couleur préférer: "))
    # if couleur != "": # Même code en bas 
    if couleur: # Python verifie que couleur est True(contient quelque chose) ou False(vide)
        if couleur in stock:
            stock[couleur] = stock[couleur] +1
        else:
            stock[couleur] = 1
print("Sondage réaliser sur les couleurs")
for couleurs, valeurs in stock.items():
    print( "-", couleurs, ":", valeurs )