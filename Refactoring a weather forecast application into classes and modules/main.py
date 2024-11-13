from classes import WeatherDataFetcher,WeatherDataParser


def main():
    while True:
        try:
            city = input("Enter The City: (New York, London, Tokyo, or exit) ").title()
            if city.lower() == "exit":
                break
            fetcher = WeatherDataFetcher(city)
            fetcher.fetch_weather_data()
            full_weather_display = input("Do You Want A Full Weather Display? (yes/no): ")
            if full_weather_display == "yes".lower():
                display = WeatherDataParser(fetcher.weather_data)
                display.weather_display()
            else:
                print("No Weather To Displayed By Your Request")
                break
        except ValueError: 
            print("Please enter a non integer")
        except Exception as e:
            print(f"An error ocurred: {e}")

    print("Exiting System.....")

                
if __name__ == "__main__":
    main()

