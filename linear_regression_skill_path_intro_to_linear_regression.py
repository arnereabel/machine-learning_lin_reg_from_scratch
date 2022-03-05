import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt


y = [1,2,3,4,3,4,5,4,5,5,4,5,4,5,4,5,6,5,4,5,4,3,4]

x = [
     [4,2,3,4,5,4,5,6,7,4,8,9,8,8,6,6,5,5,5,5,5,5,5],
     [4,1,2,3,4,5,6,7,5,8,7,8,7,8,7,8,7,7,7,7,7,6,5],
     [4,1,2,5,6,7,8,9,7,8,7,8,7,7,7,7,7,7,6,6,4,4,4]
     ]

def reg_m(y, x):
    ones = np.ones(len(x[0]))
    X = sm.add_constant(np.column_stack((x[0], ones)))
    for ele in x[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results


print (reg_m(y, x).summary())




months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

plt.plot(months, revenue, 'o')
plt.title("Sandra's Lemonade Stand")
plt.xlabel('Months')
plt.ylabel("Revenue ($)")

plt.show()


#slope
m = 8
m = 11 #"better fit manualy observed"

#intercept
b = 40
b = 42 #"better fit manualy observed"

y = [(x * m) +b for x in months]

plt.plot(months, revenue, 'o')
plt.plot(months, y)
plt.show()


x = [1, 2, 3]
y = [5, 1, 3]

#y = x
m1 = 1
b1 = 0

#y = 0.5x + 1
m2 = 0.5
b2 = 1

total_loss1 = 0
total_loss2 = 0
better_fit = 0
y_predicted1 = [(m1 * ele) + b1 for ele in x]
y_predicted2 = [(m2 * ele) + b2 for ele in x]

for i in range(len(y)):
    total_loss1 += (y[i] - y_predicted1[i]) **2

for i in range(len(y)):
    total_loss2 += (y[i] - y_predicted2[i]) **2



def print_loss(t1,t2):
    print(f'total_loss1 = {total_loss1} or total_loss2 = {total_loss2}')
    if t1 < t2:
        bfit = 1
    else:
        bfit = 2

    return bfit


better_fit = print_loss(total_loss1, total_loss2)
print(better_fit)



