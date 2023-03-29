try:
    a = int(input("Liczba całkowita: "))
    b = int(input("Liczba całkowita: "))
    c = int(input("Liczba całkowita: "))

    result = a ** 2 + a * b + b ** 2

    with open("zadanie1.txt", "w") as f:
        f.write(str(result))

except ValueError:
    print("Błąd: podane wartości nie są liczbami całkowitymi!")
except Exception as e:
    print("Wystąpił nieznany błąd: ", e)
