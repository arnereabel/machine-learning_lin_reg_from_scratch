import seaborn as sns
from gradient_descent_funcs import gradient_descent
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")

X = df["height"]
y = df["weight"]

plt.plot(X, y, 'o')
#plot your line here:
b, m = (gradient_descent(X,y,num_iterations=1000,learning_rate=0.0001))

y_predictions = [((x*m)+b) for x in X ]

plt.plot(X, y_predictions)

plt.show()