#Netacademy by CISCO Exercies

#Entrons les 03 valeurs à comparer
num1 = int(input("Enter le nombre premier numero ")) 
num2 = int(input("Enter le nombre second numero ")) 
num3 = int(input("Enter le nombre troisieme numero ")) 

if num1 > num2 and num1>num3:
    grand = num1
elif num2 > num1 and num2 >  num3:
    grand = num2
else:
    grand = num3
print("Le plus grand des trois nombres est: ",grand)