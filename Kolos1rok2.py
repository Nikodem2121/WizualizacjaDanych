import math
import sys
import random
#lab2
#zad1
# Napisz skrypt, który pobiera od użytkownika zdanie i liczy ilość słów. Użyj funkcji input

# zdanie = input()
# slowa = zdanie.split(' ')
# print('liczba slow ' + str(len(slowa)))


# zad2
# Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: a^b + c.
# Użyj funkcji readline() i write()).

# a = sys.stdin.readline()
# b = sys.stdin.readline()
# c = sys.stdin.readline()
# wynik = pow(int(a), int(b)) + int(c)
# sys.stdout.write(str(wynik))


#zad3
# Napisz skrypt, który sprawdzi czy wczytany napis jest palindromem.

# napis = input()
# napis_list = list(napis)
# napis_list2 = list(napis)
# napis_list2.reverse()
#
# if napis_list == napis_list2:
#     print('napis jest palindromem')
# else:
#     print('napis nie jest palindromem')


#zad4
# Napisz skrypt, który sprawdzi czy wczytana liczba jest pierwsza.

# a = int(input())
# if a % 2 == 0 | a <= 1:
#     print('liczba nie jest pierwsza')
# else:
#     for i in range(2, math.floor(math.sqrt(a)), 2):
#         if a % i == 0:
#             print('liczba nie jest pierwsza')
#             break
#     else:
#         print('liczba jest pierwsza')


#zad5
# Napisz skrypt, który sprawdzi ile jest liczb doskonałych do liczby 1000.

# liczby_doskonale = []
# for a in range(2, 1001):
#     suma_dzielnikow = 0
#     for i in range(1, a):
#         if a % i == 0:
#             suma_dzielnikow += i
#     if suma_dzielnikow == a:
#         liczby_doskonale.append(a)
# print('Liczby doskonałe to liczby: {}, ilość tych liczb jest równa {}'.format(liczby_doskonale, len(liczby_doskonale)))


#zad6
# Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.

# lista = [2, 3, 4, 5.6, 6.7]
# for i in lista:
#     print(math.pow(i, 2))


#zad7
# Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko parzyste liczby.

# licznik = 0
# lista = []
# while licznik != 10:
#     liczba = int(input())
#     if liczba % 2 == 0:
#         lista.append(liczba)
#     licznik += 1
# print(lista)


#zad8
# Napisz skrypt, w którym utworzysz listę z elementami dowolnego typu. Utwórz słownik, gdzie klucze będą poszczególnymi elementami z listy, a wartość to ilość wystąpień klucza w liście. Następnie usuń wszystkie elementy ze słownika, które nie będą liczbami.

# lista = ['a', 'b0', 1, 2, 3, 4]
# slow = {}
# for item in lista:
#     slow[item] = lista.count(item)
# print(slow)
# for k in list(slow.keys()):
#     if type(k) == str:
#         slow.pop(k)
# print(slow)

#lab3
# zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:

# a = [1-x for x in range(1, 11)]
# b = [4**x for x in range(0, 8)]
# c = [x for x in b if x % 2 == 0]
# print(a)
# print(b)
# print(c)


#zad2
# Wygeneruj losowo 10 elementów, zapisz je do listy1, następnie wykorzystując Python Comprehension zdefiniuj nową listę, która będzie zawierała tylko parzyste elementy

# lista1 = []
# licznik = 0
# while licznik != 10:
#     a = random.randint(0, 100)
#     lista1.append(a)
#     licznik += 1
# print(lista1)
# nowa_lista = [x for x in lista1 if x % 2 == 0]
# print(nowa_lista)


#zad3
# Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.). Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.

# slownik = {'mleko': 'sztuki', 'ziemiaki': 'kg', 'jogurt': 'sztuki'}
# lista = [key for key in slownik.keys() if slownik[key] == 'sztuki']
# print(lista)


#zad4
# Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.

# def trojkat_prostokatny(a, b, c):
#     if a**2 + b**2 == c**2:
#         return 'trójtkąt prostokątny'
#     else:
#         return 'trójkąt nie jest prostokątny'
# print(trojkat_prostokatny(3, 4, 5))


#zad5
# Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.

# def pole_trapezu(a=6,b=3,h=5):
#     return (a+b)*h/2
# print(pole_trapezu())


#zad6
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy), ile (ile  elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10

# def iloczyn(a=1, b=4, ile=10):
#     licznik = 0
#     while licznik != ile:
#         a *= b
#         licznik += 1
#     return a
# print(iloczyn())
#zad7
# Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd.

# try:
#     a = int(input())
#     result = math.sqrt(a)
# except ValueError:
#     print('zla wartosc')
# else:
#     print(result)

#zadania lab4
# zad1
# Napisz skrypt, który policzy i wyświetli następujące wyrażenie:

# a = math.pow(math.exp(4) - math.log2(34), 1/3)
# a = round(a, 2)
# b = math.pow(math.log(20) + math.cos(45) + math.e, 1/3)
# b = round(b, 2)
# c = math.pow(math.log(20, 3) + math.sin(45) * (5/8), 1/4)
# c = round(c, 2)
# d = math.log(23, 3) + math.pow(math.sin(34) + 5, 1/3)
# d = round(d, 2)
# e = math.pow(math.log2(32) + math.pi + math.sin(56), 1/4)
# e = round(e, 2)
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)


# zad2
# Napisz funkcje, który rysuje wieżę z literek. Użytkownik podaje wysokość wieży ale nie więcej
# jak 10.

# def wierza(n):
#     if n < 10 | n < 1:
#         print('zla wartosc n')
#     else:
#         for i in range(1, n+1):
#             for j in range(0, i):
#                 print('A', end='')
#             print()
# wierza(2)


# zad3
# Zmodyfikuj kod z zadania 2 tak aby otrzymać piramidę. Użytkownik podaje wysokość
# piramidy ale nie więcej jak 10

# def piramida(n):
#     if n < 10 | n < 1:
#         print('zla wartosc n')
#     else:
#         a = 2*n
#         for i in range(n):
#             for j in range(a):
#                 if j == a/2:
#                     print("A", end="")
#                 elif (j >= a/2 - i) & (j < a/2):
#                     print("A", end='')
#                 elif (j > a/2) & (j <= a/2 + i):
#                     print("A", end="")
#                 else:
#                     print(" ", end="")
#             print('')
#
# piramida(10)


#zad5
# Napisz funkcje, która utworzy wektor nxn (n wierszy, n kolumn) składający się z wartości
# losowych, a następnie funkcja ma zwrócić sumę wszystkich elementów z każdego wiersza

def wektor_nxn(n):
    wektor = []
    for i in range(0, n):
        lista = [random.randint(0, 20) for _ in range(n)]
        wektor.append(lista)
    print(wektor)
    for j in wektor:
        print(j, sum(j))

wektor_nxn(5)