# Zad 1
print("Zad1")
import numpy as np

macierz1 = np.array([[8, 2, 4]])
macierz2 = np.array([[4], [3], [6]])

result = np.dot(macierz1, macierz2)

print(result)


# Zad 2
print("Zad 2")
macierz3x3 = np.array([[8, 3, 5], [1, 5, 9], [4, 8, 5]])
print("Macierz 3x3:")
print(macierz3x3)

print("\nNajniższe wartości dla każdej kolumny:")
print(np.min(macierz3x3, axis=0))
print("\nNajniższe wartości dla każdego rzędu:")
print(np.min(macierz3x3, axis=1))

macierz4x4 = np.array([[5, 8, 1, 6], [5, 9, 3, 6], [1, 7, 3, 6], [2, 6, 4, 3]])
print("\nMacierz 4x4:")
print(macierz4x4)

print("\nNajniższe wartości dla każdej kolumny:")
print(np.min(macierz4x4, axis=0))
print("\nNajniższe wartości dla każdego rzędu:")
print(np.min(macierz4x4, axis=1))

#Zad3
print("Zad3")
iloczyn = np.dot(macierz1, macierz2)

print("Iloczyn:")
print(iloczyn)

#Zad4
print("Zad4")
macierz_calkowita = np.array([8, 4, 5], dtype=int)
macierz_rzeczywista = np.array([0.5, 1.5, 2.5])
wynik = macierz_calkowita * macierz_rzeczywista

print("Wynik:")
print(wynik)

#Zad5
print("Zad5")
macierz_sin = np.array([[7, 5, 3], [4, 9, 6]])

a = np.sin(macierz_sin)

print("Wynik:")
print(a)

#Zad6
print("Zad6")
macierz = np.array([[9, 2, 6], [4, 3, 7]])

b = np.cos(macierz)

print("Wynik:")
print(b)

#Zad7
print("Zad7")
c = a + b

print("Wynik:")
print(c)

#Zad8
print("Zad8")

for rzad in macierz3x3:
    print(rzad)

#Zad9
print("Zad9")
for element in macierz3x3.flat:
    print(element)

#Zad10
print("Zad10")


#Zad11
print("Zad11")
vector = np.array([7, 2, 4, 6, 1, 6, 8, 5, 9, 14, 11, 8])

macierz_przekszt1 = vector.reshape((3, 4))
print("Macierz 3x4:\n", macierz_przekszt1)
print("Spłaszczona macierz 3x4:\n", macierz_przekszt1.flatten())

macierz_przekszt2 = vector.reshape((4, 3))
print("Macierz 4x3:\n",macierz_przekszt2)
print("Spłaszczona macierz 4x3:\n", macierz_przekszt2.ravel())

# przekształcenie na macierz 2x6
macierz_przekszt3 = vector.reshape((2, 6))
print("Macierz 2x6:\n", macierz_przekszt3)
print("Spłaszczona macierz 2x6:\n", macierz_przekszt3.flatten())
print("Wyniki są identyczne")