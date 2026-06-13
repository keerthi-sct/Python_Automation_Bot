import requests
import json

username = "keerthi-sct"

url = f"https://api.github.com/users/{username}/repos"

response = requests.get(url)

repos = response.json()

projects = []

for repo in repos:
    projects.append({
        "name": repo["name"],
        "url": repo["html_url"]
    })

with open("portfolio/projects.json", "w") as file:
    json.dump(projects, file, indent=4)

print("Projects updated successfully!")
print(projects)