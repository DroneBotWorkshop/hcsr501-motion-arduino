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
	return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")


while True:
	# Get a Filename
    filename = getFileName()
    # Wait for a motion to be detected
    pir.wait_for_motion
    # Print text to Shell
    print("Jellybean thief detected!")
    # Preview camera on screen during video
    camera.start_preview()
    # Start recording video
    camera.start_recording(filename)
    # Record for 10 seconds
    camera.wait_recording(10)
    # Stop preview and recording
    camera.stop_preview()
    camera.stop_recording()
    # Wait 25 seconds and repeat
    time.sleep(25)
