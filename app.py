import streamlit as st
import pandas as pd
from utils import get_weather_data, get_forecast_data
from ml_model import predict_next_temp, recommend_clothing

st.set_page_config(page_title="Weather Forecast with ML", layout="centered")
st.title("🌤️ Weather Forecast + ML Insights")

city = st.text_input("Enter a city:", "Cairo")
units = st.radio("Select unit:", ("Celsius", "Fahrenheit"))
unit_type = "metric" if units == "Celsius" else "imperial"

if st.button("Get Weather"):
    current = get_weather_data(city, unit_type)

    if "error" in current:
        st.error(current["error"])
    else:
        st.subheader(f"Weather in {current['name']}, {current['sys']['country']}")
        st.write(f"**Temperature:** {current['main']['temp']}° {units}")
        st.write(f"**Condition:** {current['weather'][0]['description'].title()}")
        st.write(f"**Humidity:** {current['main']['humidity']}%")
        st.write(f"**Wind Speed:** {current['wind']['speed']} {'m/s' if unit_type == 'metric' else 'mph'}")

        st.markdown("---")
        st.subheader("ML Forecast")

        lat = current['coord']['lat']
        lon = current['coord']['lon']
        forecast = get_forecast_data(lat, lon, unit_type)

        if forecast:
            past_temps = [day["temp"]["day"] for day in forecast[:7]]
            days = [f"Day {i+1}" for i in range(len(past_temps))]
            df = pd.DataFrame({"Day": days, "Temperature": past_temps})
            st.line_chart(df.set_index("Day"))

            predicted = predict_next_temp(past_temps)
            clothing = recommend_clothing(predicted)

            st.write(f"**Predicted Temperature for Tomorrow:** {predicted}° {units}")
            st.write(f"**Clothing Recommendation:** {clothing}")
        else:
            st.warning("Unable to fetch forecast data.")

