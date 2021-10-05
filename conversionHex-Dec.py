
# Auteur: KODZO A. Mawuena aka devNull
# Cet code est distribuer sous licence MIT
# Clause de  non-resoponsabilité assujeti

# Declarer les variables à utiliser
Hex = []
y = None
o = True
# Saisis du chiffre à convertir
while o is True:
    Hex = list(str(input("Veuiller saisir l' hexadecimal à convertir : ")))
    def verif(nonhex = ['g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z'], Hex = Hex):
        """Cette fonction verifie si l'utilisateur n'a pas sasie des valeurs eronnées"""
        j=0
        for n in nonhex:
            i = n in Hex
            j +=i
        if j == 0:
            k = True
        else: 
            k = False
        return k
    if verif() is True:
        o = False
    else:
        print("Un nombre hexadecimal ne comprend que 0 à f")
    
    # tab = {'a' : 10, 'b' :11, 'c': 12, 'd': 13, 'e':14, 'f': 15}
    tab = [['a','b','c','d','e','f'],['10','11','12','13','14','15']]
    def tabl( tab = tab, Hex = Hex ):
        """Cette fonction utilise le tableau de corespondance Hexadecimal - Decimal """
        i,j = len(Hex),0
        while j != i:
            if Hex[j] == tab[0][0]:
                Hex[j] = tab[1][0]
            elif Hex[j] == tab[0][1]:
                Hex[j] = tab[1][1] 
            elif Hex[j] == tab[0][2]:
                Hex[j] = tab[1][2]
            elif Hex[j] == tab[0][3]:
                Hex[j] = tab[1][3]   
            elif Hex[j] == tab[0][4]:
                Hex[j] = tab[1][4]     
            elif Hex[j] == tab[0][5]:
                Hex[j] = tab[1][5]                  
            j+=1
        return Hex
 
tabl()
som = 0
x = len(Hex) - 1
for p in Hex:
    b = int(p)
    som += (16**x)*b
    x += -1
print("La valeur en decimal est: ",som)