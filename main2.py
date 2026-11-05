import cv2


# 3. Convert flower.jpg to grayscale
flower = cv2.imread("flower.jpg")

gray_flower = cv2.cvtColor(flower, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray flower", gray_flower)
cv2.waitKey(0)
cv2.destroyAllWindows()


