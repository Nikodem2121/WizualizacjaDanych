a = 'napis\ndrugi napis'
print(a)
b = 4
c=4.5
print(b, c)
d = 3+4j
print(d)
e = b+c
print(e)
lista = ['a0', 2, 3, 5, [7, 6, 5], 5.5]
print(lista[4])
lista.append(6.5)
print(lista)

# dodanie elementu na pozycje
lista_a=[3, 6, 8, 3, 2]
lista_a.insert(3, 10)
print(lista_a)

# dodanie kilu elementów na koniec listy
lista_b=[5, 4, 3, 2, 6, 4, 0, 4]
lista_b.extend([10, 12, 13, 14])
print(lista_b)

# usuwanie elementu po indeksie
del lista_b[2]
print(lista_b)

# usuwanie elementu po wartości elementu
lista_b.remove(4)
print(lista_b)

# odwrócenie listy
lista_a.reverse()
print(lista_a)

# sortowanie
lista_a.sort()
print(lista_a)

slownik={'a': 1, 3: 1, 5: 'b', 'a': 5}
print(slownik)
print(slownik['a'])
slownik['klucz']='wartość'
print(slownik)

slownik.pop('a')
print(slownik)

print(slownik.keys())
print(slownik.values)

# print('a = %(zm)d' % {'zm': 12})
# print('a={}, b={}'.format(12, 14))

# a = input('podaj a:')
# b = input('podaj b:')
# print(a)
# print(b)
# print(type(a))
# print(type(b))

# a = int(a)
# b = int(b)

# if a > b:
#     print('a = ' + str(a))
# elif a < b:
#     print('b = ' + str(b))
# else:
#     print('a równe b')

# if a > b:
#     print('a jest większe')
# elif a < b:
#     print('b jest większe')
# else:
#     print('a równe b')


# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
#
# if (a > b) & (c > d):
#     print(a, c)
# else:
#     print('a nie jest większe od b lub c niejest większe od d')


#for element in sekwencja:
#    instrukcja 1
#    instrukcja 2
# else:
#    istrukca 1

for x in range(1, 6, 1):
    print(x)
    print("")


# range(start, stop, step) for(int i = 0, i < lista.count(), i++)

#while warunek:
    #instrukcja 1
    #instrukcja 2
#else:
    #instrukcaj1

# licznik = 0
# while licznik !=len(lista):
#     print(lista[licznik])
#     licznik += 1

# liczby = [3, 45, 1, 7, 8, 5]
# licznik = 0
# a = int(input('podaj a:'))
# while licznik != len(liczby):
#     if a - liczby[licznik] == 0:
#         print('{} - {} = 0'.format(a, liczby[licznik]))
#         break
#     licznik += 1


# liczby = [1, 2, 2, 2, 2, 3]
# licznik = 0
# while licznik != len(liczby):
#     if liczby[licznik] == 2:
#         liczby.remove(liczby[licznik])
#     else:
#         licznik += 1
#
# print(liczby)
