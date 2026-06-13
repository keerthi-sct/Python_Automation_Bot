import requests

city = "Thiruvananthapuram"

api_key = "b1a751c9e830275de344401cedf5dd20"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()
print(data)

temperature = data["main"]["temp"]

print("City:", city)
print("Temperature:", temperature, "°C")

if temperature > 35:
    print("ALERT: Temperature is above 35°C")
else:
    print("Weather Normal")