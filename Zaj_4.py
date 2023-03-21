# Zad_1
# A = {1-x for x in range(1,11)}
# B = {i**2 for i in range(1, 7)}
# C = {x for x in B if x % 2 == 0}
#
# print("Zbiór A:", A)
# print("Zbiór B:", B)
# print("Zbiór C:", C)

#  Zad_2
# import random
#
# lista1 = [random.randint(1, 100) for i in range(10)]
# print("Lista 1:", lista1)
#
# lista_parzysta = [x for x in lista1 if x % 2 == 0]
# print("Lista parzysta:", lista_parzysta)

# Zad_3
# produkty = {
#   'jabłka': 'kg',
#   'banany': 'szt',
#   'pomarańcze': 'kg',
#   'kiwi': 'szt',
#   'gruszki': 'kg',
#   'mandarynki': 'szt',
#   'mleko': 'litry',
#   'woda': 'litry'
# }
#
# produkty_sztuki = [produkt for produkt, wartosc in produkty.items() if wartosc == 'szt']
#
# print("Słownik produktów:", produkty)
# print("Lista produktów w sztukach:", produkty_sztuki)

# Zad_4
# def czy_prostokatny(a, b, c):
#     najdluzszy_bok = max([a, b, c])
#
#     if najdluzszy_bok ** 2 == a ** 2 + b ** 2 + c ** 2 - najdluzszy_bok ** 2:
#         return True
#     else:
#         return False
#
# a = float(input("Podaj długość boku a: "))
# b = float(input("Podaj długość boku b: "))
# c = float(input("Podaj długość boku c: "))
#
# if czy_prostokatny(a, b, c):
#     print("Trójkąt jest prostokątny.")
# else:
#     print("Trójkąt nie jest prostokątny.")

# Zad_5
# def pole_trapezu(a=2, b=4, h=3):
#     pole = (a + b) / 2 * h
#     return pole
# print("Pole trapezu to:", pole_trapezu())

# Zad_6
# def iloczyn_ciagu(a1, b=4, ile=10):
#     wynik = a1
#     for i in range(1, ile):
#         wynik *= b
#     return wynik
# wynik = iloczyn_ciagu(2, 5, 3)
# print("Wynik=", wynik)

# Zad_7
