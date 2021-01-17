# --------------- Codecademy. --------------- #
#                                             #
#    PATH: Machine Learning.                  #
#    TRACK: Supervised Learning: Regression.  #
#    LESSON: Linear Regression.               #
#                                             #
# --------------- Codecademy. --------------- #


"""
    # Points and Lines.

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
    # --------------------
    # Loss
    # --------------------

    x = [1, 2, 3]
    y = [5, 1, 3]

    # y = x
    m1 = 1
    b1 = 0

    # y = 0.5x + 1
    m2 = 0.5
    b2 = 1
    
    y_predicted1 = [x_value * m1 + b1 for x_value in x]
    y_predicted2 = [x_value * m2 + b2 for x_value in x]

    total_loss1 = 0
    for i in range(len(y)):
    total_loss1 += (y[i] - y_predicted1[i]) ** 2

    total_loss2 = 0
    for i in range(len(y)):
    total_loss2 += (y[i] - y_predicted2[i]) ** 2

    print(total_loss1)
    print(total_loss2)

    better_fit = 2
"""


"""
    # --------------------
    # Gradient Descent for Intercept.
    # --------------------
    
    
    def get_gradient_at_b(x, y, m, b):
        diff = 0

        for i in range(len(x)):
            diff += y[i] - (x[i] * m + b)

        b_gradient = -2 / len(x) * diff

        return b_gradient
"""


"""
    # --------------------
    # Gradient Descent for Slope.
    # --------------------


    def get_gradient_at_m(x, y, m, b):
        diff = 0
        N = len(x)

        for i in range(N):
            y_val = y[i]
            x_val = x[i]

            diff += (x_val * (y_val - (m * x_val + b)))

        m_gradient = -2/N * diff

        return m_gradient
"""


""" 
    # --------------------
    # Step Gradient function.
    # --------------------

    def step_gradient(x, y, b_current, m_current):
        b_gradient = get_gradient_at_b(x, y, b_current, m_current)
        m_gradient = get_gradient_at_m(x, y, b_current, m_current)

        b = b_current - (0.01 * b_gradient)
        m = m_current - (0.01 * m_gradient)

        return [b, m]


    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

    # Current intercept guess.
    b = 0

    # Current slope guess.
    m = 0

    # Updates `b` and `m`.
    b, m = step_gradient(months, revenue, b, m)

    print(b, m)
"""


"""
    # --------------------
    # Gradient Descent function.
    # --------------------
    
    def gradient_descent(x, y, learning_rate, num_iterations):
        b = 0
        m = 0

        for i in range(num_iterations):
            b, m = step_gradient(b, m, x, y, learning_rate)

        return [b, m]
"""


"""
    # from gradient_descent_funcs import gradient_descent
    import seaborn
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv("heights.csv")

    X = df["height"]
    y = df["weight"]

    b, m = gradient_descent(X, y, num_iterations=1000, learning_rate=0.0001)

    y_predictions = [m * x + b for x in X]

    # ----- Plotting. ----- #
    plt.plot(X, y, "o")
    plt.plot(X, y_predictions, "o")

    plt.show()
"""
