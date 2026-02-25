import os
import json
import requests
Events_file = "events.json"


username = input("Enter your username dawg")
url = f"https://api.github.com/users/{username}/events"
try:
  response = requests.get(url)
  if response.status_code == 200:
     data = response.json()
     #dumping this to the file
     with open(Events_file,"w") as f:
            json.dump(data,f,indent =2)
     print(data)
  elif  response.status_code == 404:
    print("Error : user not found")
  elif response.status_code == 401:
    print("Error: access denied")
  else: 
    print(f"Error:Unexpected error occured : {response.status_code}")
except requests.exceptions.RequestException as e:
   print("Network error occurred:",e)


