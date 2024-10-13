from picamera2 import Picamera2, Preview
from PIL import Image
import cups
import time


picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()
picam2.capture_file("test.jpg")
printerName = "thermal"
tempImagePath = "test.jpg"

try:
    with Image.open(tempImagePath) as img:
        img = img.convert('RGB')
        img.save(tempImagePath, "PNG")
except Exception as e:
    print("error loading image", e)
    exit(1)

conn = cups.Connection()
try:
    conn.printFile(printerName, tempImagePath, "Printing", {})
except cups.IPPError as e:
    print("error")
