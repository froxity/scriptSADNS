from browser_history.utils import default_browser
import json
import datetime
from urllib.parse import urlparse

BrowserClass = default_browser()

if BrowserClass is None:
    # default browser could not be identified
    print("could not get default browser!")
else:
    b = BrowserClass()
    # his is a list of (datetime.datetime, url) tuples
    his = b.fetch_history().histories
    print(his[100])
    urlList = [item[1] for item in his]
    print(urlList[100])
    domain = urlparse(urlList[100]).netloc
    print(domain)
    # jsonString = json.dumps(his)
    # print(jsonString)