from requests import get
response = get('https://ipinfo.io/json')
data = response.json()
city = data['city']
print(city)