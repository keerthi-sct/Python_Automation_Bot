import requests
from datetime import datetime

print("Automation Bot Started!")

# Fetch advice
url = "https://api.adviceslip.com/advice"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    advice = data["slip"]["advice"]

else:
    advice = "No advice available"


today = datetime.now().strftime("%d-%m-%Y")


summary = f"""
DAILY AUTOMATION SUMMARY

Date:
{today}

Today's Advice:
{advice}

Bot Status:
Completed Successfully
"""


with open("daily_summary.txt", "w") as file:
    file.write(summary)


print(summary)

print("Summary file created successfully!")