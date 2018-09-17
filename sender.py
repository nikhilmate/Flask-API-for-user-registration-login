import requests
f = open('img1.jpg', 'rb')
files = {'file' : f}
payload = {'name':'nik', 'email' : 'coolnik@gmail.com', 'phone' : '323424242'}
url = 'http://127.0.0.1:5000/register'
r = requests.post(url, files=files, data=payload) 
if r:
    print(r.text)
