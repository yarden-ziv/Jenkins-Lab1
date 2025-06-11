import requests

url = "http://localhost:8085/movie"
data = {"id": 3, "name": 'Alien', 'length': 120, 'genre': 'Horror'}

#get current movies list
print(response = requests.get(url))

#add a new movie
response = requests.post(url, json = data)

#check if the movie was added sucssfully
print(response = requests.get(url))