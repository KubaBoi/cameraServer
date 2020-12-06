import requests
from picamera import PiCamera
from time import sleep

camera = PiCamera()

print("Starting...")
while True:
    print("Taking picture...")
    camera.capture('image.png')

    print("Posting picture...")
    url = "http://kuba-test.borec.cz/cameraServer/upload.php"
    files = {'file': open('image.png', 'rb')}
    r = requests.post(url, files=files)

    print(r.text)

    sleep(5)