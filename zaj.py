#Zad1
# try:
#     a = int(input("Liczba całkowita: "))
#     b = int(input("Liczba całkowita: "))
#     c = int(input("Liczba całkowita: "))
#
#     result = a ** 2 + a * b + b ** 2
#
#     with open("zadanie1.txt", "w") as f:
#         f.write(str(result))
#
# except ValueError:
#     print("Błąd: podane wartości nie są liczbami całkowitymi!")
# except Exception as e:
#     print("Nieznany błąd: ", e)


# Zad2
# def suma(lista1, lista2):
#     lista3 = []
#     for i in range(0, len(lista1)):
#         tmp = 0
#         tmp = lista1[i] + lista2[i]
#         lista3.append(tmp)
#     return lista3
#
# a = [5, 3, 6, 8]
# b = [1, 9, 3, 1]
# zad2 = suma(a, b)
# print(zad2)

# #Zad3
# tekst = open("tekst.txt", "r+", encoding="utf-8")
# odczyt = tekst.read()
# znaki = []
# duze = []
# for i in range(100, 135):
#     znaki.append(odczyt[i])
#     if odczyt[i].isupper():
#         duze.append(odczyt[i])
# try:
#     a = sum(1 for i in znaki if i.isupper())
#     print(duze)
#     print("Duże litery: ", a)
# except ValueError:
#     if a == 0:
#         print("Nie ma dużych liter")

# Zad4
# lista = [6, 4, 24, 4, 1, 34, 252]
# b = 10
# zad4 = [lista[i] for i in range(len(lista)) if lista[i] > b]
# print(zad4)

# Zad5
# import math
# ulamek = pow((2/7), 3)
# cos = pow(math.cos(39), 2)
# e = pow(math.e, 3)
# pierwiastek = pow((e+cos), (1/5))
# Odp = pierwiastek + ulamek + math.pi
# print(round(Odp, 2))

