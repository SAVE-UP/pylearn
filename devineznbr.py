# Il s'agit d'un simple jeu constant à choisir devinez un nombre
# La machine vous guide par des indications "...plus petit  que ça!..."
# "...plus grand  que ça!..." jusqu'à devinez le nombre exact
import random

ordinbr = random.randint(0, 10)
usernbr = None
usertab = []
while ordinbr != usernbr:
    usernbr = int(input("Veuillez saisir un nombre compris entre 0 et 10: "))

    usertab.append(usernbr)
    l = len(usertab)
    
    if usernbr > ordinbr:
        print("La valeur est plus petit  que ça! Veuillez ressayer: ")
    elif usernbr < ordinbr:
        print("La valeur est plus grand  que ça! Veuillez ressayer: ")
    else:
        print("Félicitation, la valeur rentrer est correct!!")
        print("Vous avez saisie", l, "Valeurs avant de trouvez la bonne, les voici:")
for i in usertab:
    print(i)