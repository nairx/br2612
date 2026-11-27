import requests 
url = "http://localhost:3000/api/products"
response = requests.get(url) 

products = response.json() 

for product in products:
    print(product["id"],product["name"],product["price"])