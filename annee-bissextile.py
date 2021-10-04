#Netacademy by CISCO Exercies

year = int(input("Enter a year: "))

#Leap Year = 366Days | Common Year = 365 Days

if year < 1582: #1582 The years where Gregorian Calendar is etablished
    print("Not within the Gregorian calendar period")
elif (year % 4) != 0:
    print("Common year")
elif (year % 100) != 0:
    print("Leap year")
elif (year % 400) != 0:
    print("Common year")
else:
    print("Leap year")