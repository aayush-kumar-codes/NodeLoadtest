import requests

url = "https://api.jigrr.com/api/v2/topics/list?language=en"

payload={}
files={}
headers = {
  '_id': '5ff5c25505ee39449b24e39f',
  'platform': 'android',
  'version': '1.0.0'
}

response = requests.request("GET", url, headers=headers, data=payload, files=files)

print(response.text)
