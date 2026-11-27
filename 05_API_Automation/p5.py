import requests 
url = "http://localhost:3000/api/products"
token = "Your_access_token"
headers = {
    "Authorization":f"Bearer {token}",
    "Accept":"application/json"
}

response = requests.get(url,headers=headers)
print(response.json())