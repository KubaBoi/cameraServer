import requests

url = "http://kuba-test.borec.cz/cameraServer/upload.php"
files = {'file': open('image.png', 'rb')}
r = requests.post(url, files=files)

print(r.text)