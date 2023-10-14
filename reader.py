import cv2
import points
from cv2 import data
d=cv2.QRCodeDetector()
image=cv2.imread("C:\\Users\\DELL\\Desktop\\QR\\test1.jpg")
data,points,straight_qrcode=d.detectAndDecode(image)
print("Your url is "+data)