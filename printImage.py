from PIL import Image
import cups

printerName = "thermal"
inputImage = ""
tempImagePath = "/tempImage.png"

try:
    with Image.open(inputImage) as img:
        img = img.convert('RGB')
        img.save(tempImagePath, "PNG")
except Exception as e:
    print("error loading image")
    exit(1)

conn = cups.Connection()
try:
    conn.print(printerName, tempImagePath, "Printing", {})
except cups.IPPError as e:
    print("error")
