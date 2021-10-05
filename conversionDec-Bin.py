# Auteur: KODZO A. Mawuena aka devNull
# Cet code est distribuer sous licence MIT
# Clause de  non-resoponsabilité assujeti

#Declarer les variables à utiliser
import math
Z = []
idx = 0
Y = []
r = None
n = int(input("Veuillez saisir un nombre entier positif: "))

while (n >= 1) :
    r = n%2
    n = (n-r)/2
    r = math.floor(r)
    Z.append(r)
    idx += 1

#while idx >= 0:        
#    Y.append((Z[idx])) # Fonction d'Inversion de la liste plus fastidieux 
#    idx += -1
Y = Z[::-1]  #Inversion de la liste
print (Y)

    