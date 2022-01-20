import requests
import json
import sys

# POST REQUEST (getting authentication token from user login)
def getAPI_authToken():
  api_auth = "http://127.0.0.1:8000/api/users/token/"
  data = {
      "username": "froxity",
      "password": "albab1234"
  }
  # sending post request and saving response as response object
  response = requests.post(url = api_auth, data = data)
  jsonResponse = response.json()
  access_token = jsonResponse["access"]
  print(str(access_token) + "\n")
  return access_token

# GET REQUEST AUTHENTICATED
def getDomains(access_token):
  api_domain = "http://127.0.0.1:8000/api/domains/"
  token = "Bearer " + str(access_token)
  headers = {
    "Authorization": token
  }

  response2 = requests.get(url = api_domain, headers = headers)
  data = response2.json()
  print(data)

def newDomain(access_token):
  api_newdomain = "http://127.0.0.1:8000/api/domains/"
  token = "Bearer " + str(access_token)
  headers = {
    "Authorization": token
  }
  data = {
    "domain" : "www.hahacubaan.com",
    "freq" : 13,
    "cat_id" : "e971a05b-d4df-40d2-9d98-93968ad164b0"
  }
  response2 = requests.post(url = api_newdomain, headers = headers, data = data)

def getCategory(access_token):
  api_url = "http://127.0.0.1:8000/api/category/"
  token = "Bearer " + str(access_token)
  headers = {
    "Authorization": token
  }
  response2 = requests.get(url = api_url, headers = headers)
  data = response2.json()
  print(data)

def main():
  access_token = getAPI_authToken()
  # getDomains(access_token)
  # newDomain(access_token)
  getCategory(access_token)

if __name__ == "__main__":
    main()




