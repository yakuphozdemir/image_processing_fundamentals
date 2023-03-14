import cv2 as cv
import numpy as np

path1 = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\bitwise_photos\bitwise1.png"
path2 = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\bitwise_photos\bitwise2.png"
path3 = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\bitwise_photos\bitwise3.png"

image1 = cv.imread(path1)
image2 = cv.imread(path2)
image3 = cv.imread(path3)


bitwise_and1 = cv.bitwise_and(image1,image2)
bitwise_and2 = cv.bitwise_and(image2,image3)       # maviler aynı ton, sarılar farklı ton

cv.imshow("image1",image1)
cv.imshow("image2",image2)
cv.imshow("image3",image3)
cv.imshow("bitwise1",bitwise_and1)
cv.imshow("bitwise2",bitwise_and2)

cv.waitKey(0)
cv.destroyAllWindows()
