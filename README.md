# Weather App

A small Python command-line app that looks up a city's current temperature, humidity, and weather conditions with the OpenWeatherMap Current Weather API. Temperatures are shown in °C.

## Requirements

- Python 3
- An [OpenWeatherMap API key](https://openweathermap.org/api)
- The `requests` package

## Run locally

```bash
git clone https://github.com/DhruvShah-Dev/Weather-App.git
cd Weather-App
python -m pip install requests
```

Open `weather_app.py` and replace `ENTER YOUR API KEY` with your own API key. Keep that key out of commits. Then run:

```bash
python weather_app.py
```

Enter a city name when prompted. The script prints the current temperature, humidity, and condition description.

## Current limitations

This is a learning project with a single-city, interactive workflow. It does not store forecasts or weather history. The script currently reports all API failures as “City not found,” so check your API key and network connection if a valid city fails.