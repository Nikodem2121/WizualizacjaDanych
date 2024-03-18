import numpy as np
import matplotlib.pyplot as plt
# Generowanie danych
x = np.arange(3, 7.25, 0.25)
y = np.cos(x) / x**2
# Tworzenie wykresu
plt.plot(x, y, 'b-', label='f(x) = cos(x)/x^2')
# Dodawanie etykiet i tytułów
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x) = cos(x)/x^2')
plt.legend()
# Ustawianie zakresu osi x
plt.xlim(3, 7)
# Wyświetlanie wektorów danych
print("Wartości x:", x)
print("Wartości f(x):", y)
# Wyświetlanie wykresu
plt.show()
