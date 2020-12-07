import requests
from picamera import PiCamera
from time import sleep
import time

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.rotation = 180

print("Starting...")
tm = time.time()
while True:
    try:
        print("Taking picture...")
        camera.capture('image.png')
    except Exception as e:
        print(e)
        
    try:
        print("Posting picture...")
        print(time.time() - tm - 3600)
        if (time.time() - tm - 3600 <= -3650):
            url = "http://kuba-test.borec.cz/cameraServer/upload.php?save=1"
            tm = time.time()
            print("Image will be saved.")
        else: 
            url = "http://kuba-test.borec.cz/cameraServer/upload.php?save=0"

        files = {'file': open('image.png', 'rb')}
        r = requests.post(url, files=files)

        print(r.text)
    except Exception as e:
        print(e)

    sleep(5)