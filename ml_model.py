from sklearn.linear_model import LinearRegression
import numpy as np

def predict_next_temp(temps: list) -> float:
    if len(temps) < 2:
        return None

    X = np.array(range(len(temps))).reshape(-1, 1)
    y = np.array(temps)

    model = LinearRegression()
    model.fit(X, y)

    next_day = np.array([[len(temps)]])
    predicted_temp = model.predict(next_day)[0]
    return round(predicted_temp, 2)

def recommend_clothing(temp: float) -> str:
    if temp >= 30:
        return "Wear light clothes like shorts and a t-shirt."
    elif 20 <= temp < 30:
        return "A light jacket or long sleeves would be good."
    elif 10 <= temp < 20:
        return "Wear a warm sweater or hoodie."
    else:
        return "It's cold—wear a heavy jacket or coat."
