import requests
from datetime import datetime


def get_quote():
    try:
        url = "https://api.adviceslip.com/advice"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return data["slip"]["advice"]

        else:
            return "No advice available"

    except Exception:
        return "Unable to fetch advice today"


def get_weather():

    try:
        url = "https://wttr.in/?format=3"

        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.text

        else:
            return "Weather unavailable"

    except Exception:
        return "Unable to fetch weather"
        

    


def build_summary(quote, weather):

    today = datetime.now().strftime("%d-%m-%Y")

    summary = f"""
DAILY AUTOMATION SUMMARY

Date:
{today}

Weather:
{weather}

Today's Advice:
{quote}

Bot Status:
Completed Successfully
"""

    return summary


def run():

    print("Automation Bot Started!")

    quote = get_quote()

    weather = get_weather()

    summary = build_summary(quote, weather)


    with open("daily_summary.txt", "w", encoding="utf-8") as file:
        file.write(summary)  

    print(summary)

    print("Summary file created successfully!")


run()