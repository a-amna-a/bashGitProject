import requests

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)

print(response.status_code)

expected_names = [
    "Sergey Prokopyev",
    "Dmitry Petelin",
    "Frank Rubio",
    "Stephen Bowen",
    "Warren Hoburg"
]

for name in expected_names:
    print(name)