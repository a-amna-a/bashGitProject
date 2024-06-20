import requests

# Define the URL
url = 'https://jsonplaceholder.typicode.com/posts'

# Define the data to be sent in the POST request
data = {
    'title': 'Special Agent',
    'body': 'Leroy Jethro Gibbs',
    'userId': '1'
}

response = requests.post(url, data=data)

print(response.status_code)

print(response.json())
