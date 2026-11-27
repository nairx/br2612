import requests 
url = "http://localhost:3000/api/products"

product = {
    "name":"Mouse",
    "price":10
}

response = requests.post(url,json=product)

print(response.json())
