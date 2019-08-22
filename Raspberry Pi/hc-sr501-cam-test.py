from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()

while True:
    pir.wait_for_motion()
    if pir.motion_detected:
        print("Good Looking Person Detected")
        camera.start_preview()
