""" 
# ----------- Linear Regression. ----------- #
    # Import and create the model.
        from sklearn.linear_model import LinearRegression
        your_model = LinearRegression()

    # Fit.
        your_model.fit(x_training_data, y_training_data)

    # Predict.
        predictions = your_model.predict(your_x_data)
"""

"""
# ----------- Naive Bayes. ----------- #
    # Import and create the model.
        from sklearn.naive_bayes import MultinomialNB
        your_model = MultinomialNB()

    # Fit.
        your_model.fit(x_training_data, y_training_data)

    # Predict.
        # Returns a list of predicted classes; one prediction for every data point.
            predictions = your_moel.predict(your_x_data)

        # For every data point, returns a list of probabilities of each class.
            probabilities = your_model.predict_proba(your_x_data)
"""

"""
# ----------- K-Nearest Neighbors. ----------- #
    # Import and create the model.
        from sklearn.neighbors import KNeighborsClassifier
        your_model = KNeighborsClassifier()

    # Fit.
        your_model.fit(x_training_data, y_training_data)

    # Predict.
        # Returns a list of predicted classes; one prediction for every data point.
            predictions = your.model.predict(your_x_data)
        
        # For Every data point, returns a list of probabilities of each class.
            probabilities = your_model.predict_proba(your_x_data)
"""
