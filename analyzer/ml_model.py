import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Train the model
def train_model():

    data = {
        "radiation": [4, 5, 6, 7, 5.5, 6.2, 7.1],
        "temperature": [28, 30, 31, 32, 29, 30, 33],
        "wind": [3, 4, 5, 6, 4, 5, 6],
        "energy": [6, 8, 10, 12, 9, 11, 13]
    }

    df = pd.DataFrame(data)

    X = df[["radiation", "temperature", "wind"]]
    y = df["energy"]

    model = LinearRegression()
    model.fit(X, y)

    return model


# Predict energy production
def predict_energy(radiation, temperature, wind):

    model = train_model()

    prediction = model.predict([[radiation, temperature, wind]])

    return float(prediction[0])


# Example usage
radiation = 6
temperature = 30
wind = 5

energy_output = predict_energy(radiation, temperature, wind)

print("Predicted Energy Output:", energy_output)