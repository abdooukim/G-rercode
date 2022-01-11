import math
print('Bonjour ! Ce programme sert à générer des codes  d’employés ')
year = 1
L = []
while year !=0:
    year = int(input("entrer votre année de naissance : "))
    if year != 0:
        while 2040 < year or year < 1950 :
            year = int(input("entrer votre année de naissance : "))
        else :
            if year != 0 :
                month = int(input('entrer le mois de naissance : '))
                while month > 12 or month < 1:
                    month = int(input('entrer le mois de naissance : '))
                else:
                    day = int(input('entrer le jour de naissance : '))
                    while day < 1 or day > 31:
                        day = int(input('entrer le jour de naissance : '))
                    else:
                        if month in [4 , 6 , 9 , 11]:
                            while day > 30:
                                day = int(input('entrer le jour de naissance : '))
                        elif month == 2 :
                            while day > 29 :
                                day = int(input('entrer le jour de naissance : '))
                            else :
                                if year % 4 != 0:
                                    while day > 28:
                                        day = int(input('entrer le jour de naissance : '))
                    sexe = input("enter votre sexe :")
                    while sexe not in ["F" , "f" , "h" , "H"]:
                        sexe = input("enter votre sexe :")
                    else:
                        L.append(sexe)
                        if sexe in ["F" , "f"]:
                            month += 70
            year = str(year)
            month = str(month)
            day = str(day)
            C1 = year[2]
            C2 = year[3]
            if len(month) == 1 :
                C3 = 0
                C4 = month[0]
            else:
                C3 = month[0]
                C4 = month[1]
            if len(day) == 1 :
                C5 = 0
                C6 = day[0]
            else:
                C5 = day[0]
                C6 = day[1]
            C1 = int(C1)
            C2 = int(C2)
            C3 = int(C3)
            C4 = int(C4)
            C5 = int(C5)
            C6 = int(C6)
            C7 = (C1 + 7 * C3 + 5 * C5) % 10
            C8 = (9 * ( C2 + C4 + 2 * C6 )) % 10
            C9 = (C1+C2+C3+C4+C5+C6+C7+C8) % 10
            print("V O T R E  C O D E   E S T  :" ,C1 , C2 , C3 , C4 , C5 , C6 , C7 , C8 , C9)
    else:
        F = L.count("F") 
        H = L.count("H")
        f = L.count("f")
        h = L.count("h")
        T = F + H + f + h
        if T == 0:
            T = 1
        PF = ((F+f) *100) / T
        PH = ((H+h) *100) / T
        print("FIN DE PROGRAMME ")
        print("Le pourcentage des femmes est : " , math.floor(PF) ,"%" )
        print("Le pourcentage des Hommes est : " , math.ceil(PH) , "%")

