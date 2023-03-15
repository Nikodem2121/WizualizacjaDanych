# #Zad 1
# import math
# wynik=math.exp(10)
# print(wynik)
#
# y=math.pow(math.log(5+math.pow(math.sin(8),2)),1/6)
# print(y)
#
# z=math.floor(3.55)
# q=math.ceil(4.80)
# print(z)
# print(q)
#
# #Zad 2
# imie="NIKODEM"
# nazwisko="SZAPIEL"
# print(imie.capitalize(), nazwisko.capitalize())
#
# #Zad 3
# tekst="My life be likeOoh Aah (yeah), Ooh OohMy life be like (yeah)Ooh Aah, Ooh Aah (yeah), Ooh OohOoh Aah (yeah), Ooh OohMy life be like (yeah)Ooh Aah, Ooh Aah (yeah), Ooh OohMy life be like (yeah)[Chorus (over hook)]It's times like these"
# print(tekst.count("Ooh Aah"))
#
# #Zad 4
# print(imie[0], imie[len(imie)-1])
#
# #Zad 5
# print(tekst.split())
#
# #Zad 6
# zmienna_string = "przykładowy_tekst"
# zmienna_float = 3.14
# zmienna_hex = 0xABCD
#
# print(zmienna_string)
# print(zmienna_float)
# print("Hex: {:X}".format(zmienna_hex))
#
# #Zad 7
# ulubione_sporty = ["łyżwiarstwo", "kolarstwo", "pływanie", "siłownia"]
# odwrocona_lista = list(reversed(ulubione_sporty))
# inne_sporty = ["koszykówka", "tenis stołowy"]
#
# odwrocona_lista.extend(inne_sporty)
#
# print(odwrocona_lista)
#
# #Zad 8
# skroty = {
#     "np.": "na przykład",
#     "tj.": "to jest",
#     "itp.": "i tym podobne",
#     "itd.": "i tak dalej",
#     "cd.": "ciąg dalszy",
#     "red.": "redaktor",
#     "prof.": "profesor",
#     "mgr": "magister",
#     "dr": "doktor"
# }
# print(skroty)
#
# #Zad 9
# ulubione_gry = {
#     "Sons of the forest": "Gra surviwalowa",
#     "Minecraft": "Sandbox",
#     "Heartstone": "Karciana",
#     "The Forest": "Horror",
#     "Call of duty mobile": "Battle royale"
# }
#
# ilosc_gier = len(ulubione_gry)
#
# print("Liczba ulubionych gier:", ilosc_gier)
# print("Lista ulubionych gier:", ulubione_gry)
#
# #Zad 10
# zdanie = input("Podaj zdanie: ")
# liczba_a = 0
# for litera in zdanie:
#     if litera == 'a' or litera == 'A':
#         liczba_a += 1
# print("Liczba liter a w podanym zdaniu to:", liczba_a)

#Zad 11
# a=input("Podaj a:")
# b=input("Podaj b:")
# c=input("Podaj c:")
#
# if a>b and a>c:
#     print("a jest największe")
# elif b>a and b>c:
#     print("b jest największe")
# elif c>a and c>b:
#     print("c jest największe")
# elif a==b==c:
#     print("wszystkie liczby równe")

#Zad 12
# a=[2,2.5,3,3.5,5,6.2]
# for i in range(len(a)):
#     a[i]=a[i]**2
# print(a)

# #Zad 13
# b=[]
# i=0
# while i<10:
#     a=int (input())
#     if a % 2 == 0:
#         b.append(a)
#     i += 1
#
# print("Parzyte liczby: ", b)
