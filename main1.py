import cv2

# 1. Read and display flower.jpg
flower = cv2.imread("flower.jpg")

cv2.imshow("Original Image", flower)
cv2.waitKey(0)
cv2.destroyAllWindows()


