import seaborn as sns
import sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import numpy as np

temperature = np.array(range(60, 100, 2))
temperature = temperature.reshape(-1, 1)
sales = [65, 58, 46, 45, 44, 42, 40, 40, 36, 38, 38, 28, 30, 22, 27, 25, 25, 20, 15, 5]

line_fitter = LinearRegression()
line_fitter.fit(temperature,sales)
sales_predict = line_fitter.predict(temperature)

print(line_fitter.coef_)
print(line_fitter.intercept_)
print(line_fitter.get_params())
print(line_fitter.score(temperature,sales))
print(line_fitter.score(temperature,sales_predict))

plt.plot(temperature, sales_predict)
plt.plot(temperature, sales, 'o')
plt.show()








