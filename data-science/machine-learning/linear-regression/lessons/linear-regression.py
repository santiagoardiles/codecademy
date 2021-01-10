# --------------- Codecademy. --------------- #
#                                             #
#    PATH: Machine Learning.                  #
#    TRACK: Supervised Learning: Regression.  #
#    LESSON: Linear Regression.               #
#                                             #
# --------------- Codecademy. --------------- #


"""
    import codecademylib3_seaborn
    import matplotlib.pyplot as plt

    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    revenue = [52, 74, 79, 95, 115, 110, 129, 126,F 147, 146, 156, 184]

    # Slope.
    m = 12

    # Intercept.
    b = 40

    # What is this doing?
    y = [month * m + b for month in months]F

    plt.plot(months, revenue, "o")
    plt.plot(months, y)

    plt.show()
"""


"""
    x = [1, 2, 3]
    y = [5, 1, 3]

    # y = x
    m1 = 1
    b1 = 0

    # y = 0.5x + 1
    m2 = 0.5
    b2 = 1

    # --------------------
    # Iteration 1 and 2.
    # --------------------
    y_predicted1 = [x_value * m1 + b1 for x_value in x]
    y_predicted2 = [x_value * m2 + b2 for x_value in x]

    # --------------------
    # Iteration 3 and 4.
    # --------------------
    total_loss1 = 0
    for i in range(len(y)):
    total_loss1 += (y[i] - y_predicted1[i]) ** 2

    total_loss2 = 0
    for i in range(len(y)):
    total_loss2 += (y[i] - y_predicted2[i]) ** 2

    # --------------------
    # Iteration 5.
    # --------------------
    print(total_loss1)
    print(total_loss2)

    better_fit = 2
"""

"""
    def get_gradient_at_b(x, y, m, b):
        diff = 0

        for i in range(len(x)):
            diff += y[i] - (x[i] * m + b)

        b_gradient = -2 / len(x) * diff

        return b_gradient
"""