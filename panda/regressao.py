import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas

# Pré processamento

arquivo = pandas.read_csv('dados_dengue.csv')

anos = arquivo[['ano']]
casos = arquivo[['casos']]

#mineracao

regr = LinearRegression()
regr.fit(X=anos, y=casos)

ano_futuro = [[2023]]
casos_2018 = regr.predict(ano_futuro)


print('Casos previstos para 2018 -> ', int(casos_2018))


#Pós processamento

plt.scatter(anos, casos, color='black', )
plt.scatter(ano_futuro, casos_2018, color='red')
plt.plot(anos, regr.predict(anos), color='blue')


plt.xlabel('Anos')
plt.ylabel('Casos de dengue')
plt.xticks([2023])
plt.yticks([int(casos_2018)])

plt.show()
