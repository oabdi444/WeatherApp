def predict_next_temp(temps: list) -> float:
    """
    Dummy ML model: Predicts tomorrow's temperature based on the average of the past week.
    """
    if not temps:
        return 0.0
    return round(sum(temps) / len(temps), 2)

def recommend_clothing(temp: float) -> str:
    """
    Gives a basic clothing recommendation based on temperature.
    """
    if temp < 5:
        return "Heavy winter clothing recommended."
    elif temp < 15:
        return "Wear a jacket or sweater."
    elif temp < 25:
        return "Light and comfortable clothing."
    else:
        return "Very hot — wear breathable summer clothes."
