import requests

city = input("Enter city name: ")

api_key = "5137427ee855c604bad15506fe94659f"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    data = requests.get(url).json()

    if data["cod"] == 200:
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Wind Speed:", data["wind"]["speed"], "m/s")
        print("Condition:", data["weather"][0]["description"])
    else:
        print("City not found")

except:
    print("Internet problem or API issue")