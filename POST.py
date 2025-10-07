import requests

url = "https://68cc0319716562cf507604f5.mockapi.io/nome"

data = {
    "nome":"Cesar"
}

response = requests.post(url,json=data)

print(response.status_code)
print(response.text)