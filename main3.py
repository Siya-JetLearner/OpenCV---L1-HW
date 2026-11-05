import cv2


# 4. Convert flower.jpg to HSV
flower = cv2.imread("flower.jpg")

hsv_flower = cv2.cvtColor(flower, cv2.COLOR_BGR2HSV)

cv2.imshow("HSV flower", hsv_flower)
cv2.waitKey(0)
cv2.destroyAllWindows()


