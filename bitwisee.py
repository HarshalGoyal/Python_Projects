import cv2 as cv
import numpy as np

image1 = cv.imread("Lena1.jpg")

image2 = np.ones(image1.shape,np.uint8)
image3 = np.ones(image1.shape,np.uint8)

cv.rectangle(image2,(50,50),(300,300),(255,255,255),-1)

cv.circle(image3,(285,285),50,(255,255,255),-1)

image4 = cv.bitwise_and(image1,image2)

# image4 = cv.bitwise_and(image2,image3)
# image5 = cv.bitwise_or(image2,image3)
# image6 = cv.bitwise_xor(image2,image3)
# image7 = cv.bitwise_not(image2)


cv.imshow("frame1",image1)
cv.imshow("frame2",image2)
cv.imshow("frame3",image3)
cv.imshow("frame4",image4)
# cv.imshow("frame5",image6)
# cv.imshow("frame6",image7)

cv.waitKey()
cv.destroyAllWindows()