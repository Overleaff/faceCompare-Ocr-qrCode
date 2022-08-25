import cv2
from display import *
import matplotlib.pyplot as plt

path = "/home/kiet/Documents/faceReg+ocr/samples/qrC.png"

im = cv2.imread(path)
grayy = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

detector = cv2.QRCodeDetector()
data, bbox, _ = detector.detectAndDecode(grayy)

print(data)
print(bbox)

box = displayBbox(grayy, bbox)

plt.imshow(box, cmap='gray')
plt.show()


