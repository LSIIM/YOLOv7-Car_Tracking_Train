import cv2

img = cv2.imread("000006.jpg")
print(img.shape)
cv2.imshow("img", img)

# wait for key to exit
cv2.waitKey(0)