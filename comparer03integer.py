#Netacademy by CISCO Exercies

#Entrer les valleurs à comparer
num1 = int(input("Entrer la premier valeur: "))
num2 = int(input("Entrer la premier valeur: "))
num3 = int(input("Entrer la premier valeur: "))

#Supposons que num1 est la plus grande valeur parmis les 3
grand = num1

if num2 > num1:
    grand = num2
if num3 > num1:
    grand = num3
    
print("Le plus grand des trois nombre est: ", grand)