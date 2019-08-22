from gpiozero import MotionSensor
from picamera import PiCamera
import time
import datetime

# Create object for PIR Sensor
# PIR Sensor is on GPIO-4 (Pin 7)
pir = MotionSensor(4)

# Create Object for Camera
camera = PiCamera()

# Function to create new Filename from date and time
def getFileName():
	return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.jpg")


while True:
	# Get a Filename
    filename = getFileName()
    # Wait for a motion to be detected
    pir.wait_for_motion
    # Print text to Shell
    print("Sneaky Person Alert!!")
    # Preview camera on screen until picture is taken
    camera.start_preview()
    # Take a picture of intruder
    camera.capture(filename)
    camera.stop_preview()
    # Wait 10 seconds before repeating
    time.sleep(10)
