import requests

PORT=8082
localhost = "localhost"

res = requests.get('http://'+localhost+':'+str(PORT)+'/test')
print(res.text)