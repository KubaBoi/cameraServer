import requests
from picamera import PiCamera
from time import sleep

camera = PiCamera()

while True:
    camera.capture('image.png')

    url = "http://kuba-test.borec.cz/cameraServer/upload.php"
    files = {'file': open('image.png', 'rb')}
    r = requests.post(url, files=files)

    print(r.text)

    sleep(5)