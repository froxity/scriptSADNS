import requests

global name
def getAPI_authToken():
  api_auth = "https://sadns.herokuapp.com/api/users/token/"
  data = {
      "username": "user2022",
      "password": "abubaba1234"
  }
  # sending post request and saving response as response object
  response = requests.post(url = api_auth, data = data)
  jsonResponse = response.json()
  access_token = jsonResponse["access"]
  name = 'Ahmad Afiq'
  return access_token

def getProfileConfig(access_token):
  url = "https://sadns.herokuapp.com/api/profileConfig/"
  token = "Bearer " + str(access_token)
  headers = {
    "Authorization": token
  }
  response = requests.request("GET", url, headers=headers)
  jsonResponse = response.json()
  for x in jsonResponse:
    print(x)

def main():
  access_token = getAPI_authToken()
  print(name)
  # getProfileConfig(access_token)

if __name__ == "__main__":
    main()