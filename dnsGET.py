import urllib.request
import requests
from requests.exceptions import ConnectionError
import json

api_url_whitelist = "http://127.0.0.1:8000/api/whitelist"
api_url_blacklist = "http://127.0.0.1:8000/api/blacklist"
HTTPCodeStatus1 = urllib.request.urlopen(api_url_whitelist).getcode()
HTTPCodeStatus2 = urllib.request.urlopen(api_url_blacklist).getcode()


try:
  while HTTPCodeStatus1 == 201 and HTTPCodeStatus1 == 201:
    response1 = requests.get(url = api_url_whitelist)
    response2 = requests.get(url = api_url_blacklist)
    data1 = response1.json()
    data2 = response2.json()
    """Testing below to see data actually get from API or not"""
    print("----------")
    print(data1)
    print("----------")
    print(data2)
    # Extract data and put into rpz.db file
    # Restart system for dns
except ConnectionError as error:
  print("Connection Error!! Make sure you are connected to Internet. Technical Details given below:")
  print(str(error))
except requests.Timeout as error:
  print("Timeout Error!!")
  print(str(error))
except KeyboardInterrupt:
  print("Someone closed the program")
