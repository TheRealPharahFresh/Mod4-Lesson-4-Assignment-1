class WeatherDataFetcher:
    def __init__(self,city):
        self.city = city
        self.weather_data = None

    def fetch_weather_data(self):
        data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 65, "city": "Tokyo"}
        }
        if self.city in data:
            self.weather_data = data[self.city]
            print(f"Weather data for {self.city} fetched successfully!")
        else:
            print("Data Could Not Be Fetched")

class WeatherDataParser:
    def __init__(self, weather_data):
        self.weather_data = weather_data

    def get_temperature(self):
        if self.weather_data:
            return self.weather_data["temperature"]
        else: 
            print("Temperature Not Found")
            return None

    def get_condition(self):
        if self.weather_data:
            return self.weather_data["condition"]
        else:
            print("Condition not found")
            return None
    
    def get_humidity(self):
        if self.weather_data:
            return self.weather_data['humidity']
        else:
            print("Humidity not found")
            return None
        
    def weather_display(self):
        return print(f"City: {self.weather_data["city"]},\n Temperature: {self.weather_data["temperature"]}, Condition: {self.weather_data["condition"]}, Humidity: {self.weather_data["humidity"]}")




