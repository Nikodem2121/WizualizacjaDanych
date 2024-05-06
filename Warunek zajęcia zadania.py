import numpy as np
# Zakres do drugiego kolokwium
# Zajęcia 20.03.2024--------------------------------------------------------------------------

# Kod z zajęć
# a = np.array([0, 1])
# print(a)

# a = np.arange(2)
# print(a)
# print(a)
# print(type(a))

# print(a.dtype)
# a = np.array(['a' ,'b' ,'c' ,1, 2, 3])
# print(a)
# print(a.dtype)


# a = np.arange(2, dtype = 'int32')
# print(a.dtype)
# b = a.astype('float')
# print(b)
# print(b.dtype)
# print(b.shape)

# print(a.ndim)

# m = np.array((np.arange(2), np.arange(2)))
# print(m)
# print(m.shape)

# m = np.array([[2, 3, 4],
#               [5, 6, 7]], dtype = 'float')
# print(m)

# zera = np.zeros((5, 5))
# jedynki = np.ones((4, 4))
# print(zera)
# print(jedynki)
# print(zera.dtype)
# print(jedynki.dtype)

# pusta = np.empty((2, 2))
# print(pusta)
# poz_1 = pusta[1, 1]
# poz_2 = pusta[0, 1]
# print(poz_1)
# print(poz_2)

# macierz = np.array([[1, 2], [3, 4]])
# print(macierz)
# liczby = np.arange(1, 2, 0.1)
# print(liczby)

# liczby_lin = np.linspace(1, 2, 5, endpoint=False)
# print(liczby_lin)

# z = np.indices((5, 3))
# print(z)
# print(z.shape)
# print(z[0, 2, 1])


# x, y = np.mgrid[0:5, 0:5]
# print(x)
# print(y)

# mat_diag_k = np.diag([a for a in range(5)], -1)
# print(mat_diag_k)

# z = np.fromiter(range(5), dtype='int32')
# print(z)

# znaki = b'abcdef'
# zn1 = np.frombuffer(znaki, dtype='S1')
# print(zn1)

# zn2 = np.frombuffer(znaki, dtype='S2')
# print(zn2)

# zn3 = np.frombuffer(znaki, dtype='S3')
# print(zn3)

# zn4 = np.frombuffer(znaki, dtype='S4')
# print(zn4)

# znaki = 'abcdef'
# zn3 = np.array(list(znaki))
# zn4 = np.array(list(znaki), dtype='S1')
# zn5 = np.array(list(b'abcdef'))
# zn6 = np.fromiter(list(znaki, dtype='S1'))
# zn7 = np.fromiter(list(znaki, dtype='U1'))
# print(zn3)
# print(zn4)
# print(zn5)
# print(zn6)
# print(zn7)

# mat = np.ones((2, 2))
# mat_1 = np.ones((2, 2))
# mat = mat + mat_1
# print(mat)
# print(mat - mat_1)
# print(mat*mat_1)
# print(mat/mat_1)
#
# mat_1=np.array([[4, 5], [6, 7]])
# print(mat)
# print(mat - mat_1)
# print(mat*mat_1)
# print(mat/mat_1)
#
# a = np.dot(mat, mat_1)
# print(a)
# b = mat.dot(mat_1)
# mat  =+ mat_1
# print(mat)

# a = np.arange(10)
# print(a)
# s = slice(2, 7, 2)
# print(a[s])
# s = range(2, 7, 2)
# print(a[s])
# print(a[2:7:2])
# print(a[1:])
# print(a[2:5])

# mat = np.arange(25)
#
# mat = mat.reshape((5, 5))
#
# print(mat[1:])
# print(mat[:,1])
# print(mat[:, -1:])
# print(mat[2:5, 1:3])
# print(mat[:, range(2, 6, 2)])
# print(' ')

# x = np.array([[0, 1, 2],
#               [3, 4, 5],
#               [6, 7, 8],
#               [9, 10, 11]])
# print(x)
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
# y = x[rows, cols]
# print(y)

# Zadania zajęcia 06.05.2024------------------------------------------------------------------
# Zad 1
# import pandas as pd
#
# # Specify the path to your Excel file
# file_path = "D:/Dokumenty/Wizualizacja_danych/datasets/imiona.xlsx"
#
# # Load the Excel file into a DataFrame
# df = pd.read_excel(file_path)
#
# # Print the DataFrame to see the data
# print(df)

# Zad 2___________________________________________________________________________________________
# ------------------------------
# df_filtered_1000 = df[df['Liczba'] > 1000]
# print(df_filtered_1000)
# # ------------------------------
# df_your_name = df[df['Imie'] == 'NIKODEM']
# print(df_your_name)
# # ------------------------------
# suma_calkowita = df['Liczba'].sum()
# print("Całkowita suma dzieci=", suma_calkowita)
# # ------------------------------
# okres_00_05 = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]
# suma_okresowa = okres_00_05['Liczba'].sum()
# print("Suma w okresie od 2000 do 2005=", suma_okresowa)
# # ------------------------------
# chlopcy = df[df['Plec'] == 'M']['Liczba'].sum()
# # suma_chlopcow = chlopcy['Liczba'].sum()
# print("Suma chłopców=", chlopcy)
#
# dziewczynki = df[df['Plec'] == 'K']['Liczba'].sum()
# print("Suma dziewczynek=", dziewczynki)
# # ------------------------------
# most_popular_each_year = df.groupby(['Rok', 'Plec'])['Liczba'].idxmax()
# most_popular_names = df.loc[most_popular_each_year]
# print(most_popular_names[['Rok', 'Imie', 'Liczba']])
# # ------------------------------
# most_popular = df.groupby(['Plec'])['Liczba'].idxmax()
# most_popular_names = df.loc[most_popular]
# print(most_popular_names[['Rok', 'Imie', 'Liczba']])

# Zad_3_____________________________________________________________________________________________________________________
import pandas as pd

# Load the CSV file
df = pd.read_csv("D:/Dokumenty/Wizualizacja_danych/datasets/zamowienia.csv")
# ----------------------------------------------------------------------
# _______________________________________________________________________________________/Sprawdzić co nie tak/______________________________
# unique_sellers = df["Sprzedawca"].unique()
# print(unique_sellers)
# ----------------------------------------------------------------------
# top_five_values = df['Utarg'].nlargest(5)
# print(top_five_values)


