import requests
from datetime import datetime


def get_quote():
    url = "https://api.adviceslip.com/advice"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data["slip"]["advice"]

        else:
            return "No advice available"

    except:
        return "No advice available"


def build_summary(advice):

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

    return summary


def save_summary(summary):

    with open("daily_summary.txt", "w") as file:
        file.write(summary)


def run():

    print("Automation Bot Started!")

    advice = get_quote()

    summary = build_summary(advice)

    save_summary(summary)

    print(summary)

    print("Summary file created successfully!")


if __name__ == "__main__":
    run()