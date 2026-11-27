import requests 
url = "http://localhost:3000/api/products/3"

response = requests.delete(url)

print("Product Deleted")

