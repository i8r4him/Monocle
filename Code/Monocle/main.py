import asyncio
import io
import PIL.Image as Image
import time
from brilliant import *
import binascii
import cv2
import webbrowser
from urllib.parse import urlparse
from pyzbar.pyzbar import decode
import numpy as np
from pyzbar import pyzbar

remote_script = '''
import bluetooth, camera, time, led, touch, display
text = display.Text('Waiting...', 100, 0, display.WHITE, justify=display.TOP_LEFT)
display.show(text)
def trigger_capture(button):
    len = bluetooth.max_length()
    text = display.Text('Capturing...', 100, 0, display.WHITE, justify=display.TOP_LEFT)
    display.show(text)
    camera.capture()
    time.sleep_ms(100)
    while data := camera.read(bluetooth.max_length() - 4):
        led.on(led.GREEN)
        while True:
            try:
                bluetooth.send((b"img:" + data)[:len])
            except OSError:
                continue
            break
    led.off(led.GREEN)
    bluetooth.send(b'end:')
    done = display.Text('Done', 100, 0, display.WHITE, justify=display.TOP_LEFT)
    display.show(done)
touch.callback(touch.EITHER, trigger_capture)
'''



async def get_image():
    async with Monocle() as m:
        await m.send_command(remote_script)
        await ev.wait()
        data = await m.get_all_data()
        return data
        
async def detect():
    # Load the image
    image = cv2.imread('hidden9.jpg')
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply Otsu's thresholding to separate the QR code from the background
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Apply morphological transformations to enhance the QR code
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)
    
    # Detect edges using Canny edge detector
    edged = cv2.Canny(eroded, 50, 200)
    
    # Save the intermediate results for debugging
    cv2.imwrite('gray.jpg', gray)
    cv2.imwrite('blurred.jpg', blurred)
    cv2.imwrite('thresh.jpg', thresh)
    cv2.imwrite('dilated.jpg', dilated)
    cv2.imwrite('eroded.jpg', eroded)
    cv2.imwrite('edged.jpg', edged)
    
    # Decode the QR code from the image
    decoded_objects = pyzbar.decode(dilated)
    
    # If no QR code is found in the dilated image, try the eroded image
    if not decoded_objects:
        decoded_objects = pyzbar.decode(eroded)
    
    # If no QR code is found in the eroded image, try the original grayscale image
    # if not decoded_objects:
    #     decoded_objects = pyzbar.decode(gray)
    
    # # Draw rectangles around the QR code and print the decoded data
    # for obj in decoded_objects:
    #     (x, y, w, h) = obj.rect
    #     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #     cv2.putText(image, obj.data.decode("utf-8"), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    # # Display the image with rectangles
    # cv2.imshow('Image with QR code', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # If QR code is found, return the decoded data
    if decoded_objects:
        for obj in decoded_objects:
            print("QR-Code Data:", obj.data.decode("utf-8"))
        data = decoded_objects[0].data.decode("utf-8")
        return data
    
    # If no QR code is found with pyzbar, try using the OpenCV QRCodeDetector
    else:
        print("No QR Code found with pyzbar, trying OpenCV QRCodeDetector.")
        
        # Use the OpenCV QRCodeDetector to detect and decode the QR code
        detector = cv2.QRCodeDetector()
        data, vertices_array, _ = detector.detectAndDecode(dilated)
        
        # If a QR code is found, return the decoded data
        if data:
            print("QR Code Data (OpenCV):")
            print(data)
            return data
        
        # If no QR code is found, return a message indicating no data was found
        else:
            print("No QR Code found in the image.")
            return "no data found"
async def display(data):
    async with Monocle() as m:
        await m.send_command(f"import display \ntext = display.Text('{data}', 100, 0, display.WHITE, justify=display.TOP_LEFT) \ndisplay.show(text)")
        
async def check(data):
    try:
        result = urlparse(data)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

async def main():
   while True:
        data = await get_image()
        
        try:
            img = Image.open(io.BytesIO(data))
        #     #img.verify()  
        except (IOError, SyntaxError) as e:
        #     print('Invalid image data:', e)
            continue
        img =  Image.open(io.BytesIO(data))
        jpgImg = img.convert('RGB')
        jpgImg.save('output.jpg')
        qr_data = await detect()
        
        checkImg = await check(qr_data)
        if checkImg:
            webbrowser.open(qr_data)
            qr_data = urlparse(qr_data).netloc
            await display(qr_data)
        else:
            await display(qr_data)
        ev.clear()

asyncio.run(main())
