# Weather Forecast with Machine Learning Insights

This is a Streamlit-based weather forecasting application that integrates real-time weather data with basic machine learning predictions. The application allows users to view current weather conditions, analyze a seven-day temperature trend, predict the temperature for the next day, and receive a clothing recommendation based on that prediction.

## Features

This project includes the following functionality:

Real-time weather search and display by city name  
Current temperature, weather conditions, humidity, and wind speed  
Seven-day temperature forecast chart (based on API access)  
Simple moving average ML model for next-day temperature prediction  
Clothing recommendation system based on predicted temperature  
Secure API key management with environment variables  
Ready-to-deploy structure for Streamlit Cloud or local hosting  

## Project Structure

app.py                  Main Streamlit application  
utils.py                Functions for API calls to OpenWeatherMap  
ml_model.py             Basic ML logic and clothing recommendation  
.env.example            Template for user API key configuration  
requirements.txt        Python dependencies  
.gitignore              Ensures secrets and temporary files are excluded  
README.md               Full documentation for the project  

## Setup Instructions

Clone the repository

git clone https://github.com/your-username/weather-ml-app.git  
cd weather-ml-app

(Recommended) Create and activate a virtual environment

python -m venv venv  
source venv/bin/activate  
On Windows: venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Configure your API key

Rename the file .env.example to .env  
Visit https://home.openweathermap.org/api_keys and generate an API key  
Paste it into your .env file like this:

OPENWEATHER_API_KEY=your_api_key_here

Run the app

streamlit run app.py

## Deployment Instructions

Push this project to your GitHub account  
Visit https://streamlit.io/cloud and sign in  
Create a new app from your GitHub repo and choose app.py as the main file  
In Streamlit Cloud settings, add a secret called OPENWEATHER_API_KEY with your API key value  
Deploy the app to the web  

## Important Notice About Forecast Functionality

The current weather feature in this application works immediately with a free OpenWeatherMap API key. Users can retrieve accurate, real-time weather data including temperature, condition, humidity, and wind speed for any city.

However, the machine learning features, including the seven-day temperature forecast and the clothing recommendation system, require access to the OpenWeatherMap One Call API. As of 2025, this API is not fully available on all free-tier accounts.

If you encounter the message:

"ML Forecast: Unable to fetch forecast data."

This means your API key does not have access to the One Call API or the request is blocked due to rate limits or subscription tier.

To enable forecast support:

Log in at https://home.openweathermap.org/api_keys  
Check that your API key has One Call API access  
Upgrade to a paid subscription or apply for educational/student access if needed  
Once access is granted, the forecast features will begin working without any code changes  

## Technical Scope and Developer Notes

This project demonstrates the following developer capabilities:

Design and development of a full-stack web application using Streamlit  
Integration of third-party APIs with error handling and user feedback  
Implementation of a simple machine learning model using real-world data  
Creation of a rule-based recommendation system  
Preparation of secure, documented, and production-ready code for deployment  
Use of environment variables to manage API credentials safely  
Ability to explain and document edge-case limitations transparently  

This project is designed for public use and technical evaluation. It is structured to be understandable, extensible, and adaptable to future feature additions such as advanced ML models, geolocation, or export capabilities.

## License

This project is provided under the MIT License. See LICENSE file for details.

## Author

Developed by Osman  
GitHub: https://github.com/oabdi444  

