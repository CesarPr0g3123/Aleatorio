import requests

url = "https://68cc0319716562cf507604f5.mockapi.io/nome"

response = requests.get(url)

print(response.status_code)
print(response.text)