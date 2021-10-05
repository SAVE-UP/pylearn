
# Auteur: KODZO A. Mawuena aka devNull
# Cet code est distribuer sous licence MIT
# Clause de  non-resoponsabilité assujeti

# Declarer les variables à utiliser
Bin = []
y = None
o = True
# Saisis du chiffre à convertir
while o is True:
    Bin = list(str(input("Veuiller saisir le binaire à convertir : ")))
    def verif(nonbin = ['2','3','4','5','6','7','8','9'], Bin = Bin):
        """Cette fonction verifie si l'utilisateur n'a pas sasie des valeurs eronnées"""
        j=0
        for n in nonbin:
            i = n in Bin
            j +=i
        if j == 0:
            k = True
        else: 
            k = False
        return k
    if verif() is True:
        o = False
    else:
        print("Un nombre binaire ne comprend que 1 ou 0")
som = 0
x = len(Bin) - 1
for p in Bin:
    b = int(p)
    som += (2**x)*b
    x += -1
print("La valeur en decimal est: ",som)