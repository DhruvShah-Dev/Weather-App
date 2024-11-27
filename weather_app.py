import requests

def get_weather(city):
    # Your OpenWeatherMap API key (replace with your actual key)
    api_key = "ENTER YOUR API KEY"
    
    # Base URL for OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Construct the final URL
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    # Send a GET request to the API
    response = requests.get(complete_url)
    
    # Convert the response to a JSON format
    data = response.json()
    
    # Check if the request was successful
    if data["cod"] == 200:
        # Extract the weather data
        main_data = data["main"]
        weather_data = data["weather"][0]
        
        # Display the weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Humidity: {main_data['humidity']}%")
        print(f"Weather: {weather_data['description']}")
    else:
        print("City not found!")

def main():
    city = input("Enter city name: ") 
    get_weather(city)

if __name__ == "__main__":
    main()
