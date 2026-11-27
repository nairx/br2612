import requests 
url = "http://localhost:3000/api/products"
response = requests.get(url) 
print("Status Code",response.status_code)
print(response.text)