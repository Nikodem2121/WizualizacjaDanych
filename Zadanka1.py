import math

# a = pow(pow(math.e, 4) - math.log2(34), 1 / 3)
# a = round(a, 2)
#
# b = pow(math.log(20) + math.cos(45) + math.e, 1/3)
# b = round(b, 2)
#
# c = pow(math.log(20, 3) + math.sin(45) * (5/8), 1/4)
# c = round(c, 2)
# print(a)
# print(b)
# print(c)

# def wierza(n):
#     if n > 10 | n < 1:
#         print("Zła wartość n")
#     else:
#         for i in range(1, n+1):
#             for j in range(0, i):
#                 print("A", end=" ")
#             print()
# wierza(10)

def piramida(n):
    if n < 10 | n < 1:
        print('zla wartosc n')
    else:
        a = 2*n
        for i in range(n):
            for j in range(a):
                if j == a/2:
                    print("A", end="")
                elif (j >= a/2 - i) & (j < a/2):
                    print("A", end='')
                elif (j > a/2) & (j <= a/2 + i):
                    print("A", end="")
                else:
                    print(" ", end="")
            print('')

piramida(10)