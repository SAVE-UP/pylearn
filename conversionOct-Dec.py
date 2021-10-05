
# Auteur: KODZO A. Mawuena aka devNull
# Cet code est distribuer sous licence MIT
# Clause de  non-resoponsabilité assujeti

# Declarer les variables à utiliser
Oct = []
y = None
o = True
# Saisis du chiffre à convertir
while o is True:
    Oct = list(str(input("Veuiller saisir le Octal à convertir : ")))
    def verif(nonbin = ['8','9'], Oct = Oct):
        """Cette fonction verifie si l'utilisateur n'a pas sasie des valeurs eronnées"""
        j=0
        for n in nonbin:
            i = n in Oct
            j +=i
        if j == 0:
            k = True
        else: 
            k = False
        return k
    if verif() is True:
        o = False
    else:
        print("Un nombre Octal ne comprend que 0 à 7")
som = 0
x = len(Oct) - 1
for p in Oct:
    b = int(p)
    som += (8**x)*b
    x += -1
print("La valeur en decimal est: ",som)