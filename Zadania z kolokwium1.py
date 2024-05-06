# Kolokwium_1
# Zadanie 1 grB
# import math
#
# total_sum = 0
#
# for n in range(45, 71):
#     term = math.pow(math.sin(n) + math.pow(n, (1 / 2)), (1 / 3))
#     total_sum += term
#
# rounded_sum = round(total_sum, 2)
#
# print(rounded_sum)

# Wyniki
# Grupa a = 45.61
# Grupa b = 51.04

# Zadanie 1 GrA
# import math
#
# suma = 0
# for a in range (4, 11):
#     wynik = math.pow(math.pow(math.e, a) + math.log(24, 2), (1 / 4))
#     suma += wynik
#
# zaokrąglony = round(suma, 2)
# print(zaokrąglony)

# Zadanie 2 GrB
# from random import randint
#
# def losowe_liczby(ile, n):
#   """
#   Funkcja generuje listę `ile` losowych liczb z zakresu <1, 20>
#   z możliwością powtórzenia `n` razy.
#
#   Argumenty:
#     ile: liczba elementów do wygenerowania
#     n: maksymalna liczba powtórzeń
#
#   Zwracane wartości:
#     lista `ile` losowych liczb
#   """
#   if n < 1:
#     raise ValueError("Wartość n musi być dodatnia")
#   wynik = []
#   for _ in range(ile):
#     liczba = randint(1, 20)
#     for _ in range(randint(1, n)):
#       wynik.append(liczba)
#   return wynik
#
# # Przykład użycia
# liczby = losowe_liczby(10, 3)
# print(liczby)
#
# # Zadanie 2 GrA
# import random
#
# def tablica(ile, n):
#     if n < 1:
#         raise ValueError("n musi być dodatnie")
#     wynik = []

