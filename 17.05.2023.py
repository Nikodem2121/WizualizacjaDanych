import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns




# ts=pd.Series(np.random.randn(1000))
# ts=ts.cumsum()
#
# df=pd.DataFrame(ts, columns=['wartości'])
# print(df)
# df['Średnia krocząca']= df.rolling(window=50).mean()
# df.plot()
# plt.legend
# plt.show()



# x = np.random.randn(10000)
# plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
# plt.xlabel('Wartości')
# plt.ylabel('Prawdopodobieństwo')
# plt.title('Histogram')
# plt.grid()
# plt.show()




df=pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
print(df)
seria=df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
wedges,texts,autotext=plt.pie(x=seria, labels=seria.index,
                              autopct=lambda pct:"{:.1f}%".format(pct),
                              textprops=dict(color='black'),
                              colors=['red','green'])
plt.title('Suma zamówień dla sprzedawców')
plt.legend(loc='lower right')
plt.ylabel('Procentowy wynik wartości zamówień')
plt.show()



# sns.set(rc={'figure.figsize': (8, 6)})
# sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 9, 16], label='linia nr',
# color='red', marker='o', linestyle=':')
# sns.lineplot(x=[1, 2, 3, 4], y=[2, 5, 10, 17], label='linia nr',
# color='green', marker='o', linestyle=':')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Wykres linowy')
# plt.show()

                                  ####### siatka na wykresach
                                  # sns.set()

# s= pd.Series(np.random.randn(1000))
# s= s.cumsum()
# wykres = sns.relplot(kind='line', data=s, label='dane z serii')
# wykres.fig.set_size_inches(8, 6)
# wykres.fig.suptitle('wykres liniowy')
# wykres.set_xlabels('ideksy')
# wykres.set_ylabels('wartości')
# wykres.add_legend()
# wykres.figure.supplots_adjust(left=0.1, right=0.9,
#                               bottom=0.1, top=0.9)
# plt.show()


# df =pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df)
# sns.lineplot(data=df, x=df.index, y='sepal length',
#              hue='class', palette=['yellow', 'green', 'red'])
# plt.xlabel('indeksy')
# plt.ylabel('Wykres liniowy danych z Iris dataset')
# plt.show()



# data={'a': np.arange(50),
#       'c': np.random.randint(0, 50, 50),
#       'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# df = pd.DataFrame(data)
#
# plot = sns.relplot(data=df, x='a', y='b', hue='c',
#                    palette='bright', size='d', legend=True)
# plot.set(xticks=data['a'])
# plt.show()



# data ={'kraj': ['Belgia', 'Indie', 'Brazylia','Polska'],
#         'stolica': ['Bruksela', 'New delhi', 'brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [11109846,1303171035,207847528,386756762]}
# df = pd.DataFrame(data)
# plot=sns.barplot(data=df, x='Kontynent', y='Populacja',
#                  hue='Kontynent', estimator=np.sum, errorbar=None,
#                  dodge=False, palette=['red', 'green', 'blue'])
# plot.legend(title='Populacja na kontynentach')
# plot.set(title='Wykres słupkowy')
# plt.show()
