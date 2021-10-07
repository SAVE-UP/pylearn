#Juste quelques petits rappels non-exhasive sur les dictionaires en python

score = {"louis": 14, "franc":20, "mawuen":94, "glen":30 } # Couples Clé/Valeurs
print(score["louis"]) # On accède à une valeur en pointant sur sa clé
score["louis"] = 13 # Permet de changer la valeur de la clé "louis"

for pers,buts in score.items(): # function unpacking et function 'items()'
    print(pers, buts)

scores = {"louis": [14, 12, 20, 55], "franc":[20, 30, 29, 62], "mawuen": 94, "glen": 30 }
print(scores["louis"].append(18))
print(scores)