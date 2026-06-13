import requests

api_key = "0d7e4b534d74c5e8dae03cae8b1b56c8"

city = "Thiruvananthapuram"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

temperature = data["main"]["temp"]

print("City:", city)
print("Temperature:", temperature, "°C")

if temperature > 35:
    print("ALERT: Temperature above 35°C")
else:
    print("Weather Normal")