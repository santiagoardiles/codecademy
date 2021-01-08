# --------------- Codecademy. --------------- #
#                                             #
#    PATH: Machine Learning.                  #
#    TRACK: Supervised Learning: Regression.  #
#    LESSON: Linear Regression.               #
#                                             #
# --------------- Codecademy. --------------- #

# import codecademylib3_seaborn
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

# Slope.
m = 12

# Intercept.
b = 40

# What is this doing?
y = [month * m + b for month in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()
