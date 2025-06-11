import requests

url = "http://localhost:8085/movie"
data = {"id": 3, "name": 'Alien', 'length': 120, 'genre': 'Horror'}
flag = False

#get current movies list
response = requests.get(url)
print(response.json())

#add a new movie
response = requests.post(url, json = data)

#check if the movie was added successfully
response = requests.get(url)
print(response.json())
output = response.json()

for movie in output:
    if movie["name"] == data["name"]:
        print("API Test completed successfully")
        flag = True

if flag == False:
    print("API test failed")