import requests

data=requests.get("http://fakestoreapi.in/api/products")
print(data.json())