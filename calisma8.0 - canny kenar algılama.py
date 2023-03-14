import cv2 as cv
import numpy as np

path = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\photo.jpg"

image1 = cv.imread(path)
image2 = cv.cvtColor(image1,cv.COLOR_BGR2GRAY)

#image3 = cv.cvtColor(image2,cv.COLOR_GRAY2BGR)
#print(image3.shape)
blured = cv.GaussianBlur(image2,(5,5),0)

sample = cv.Canny(blured,threshold1=0,threshold2=110)

def auto_canny(image, sigma = 0.30):
    median = np.median(image)
    print("\nmedian:  ",median)
    lower = int(max( 0, ((1.0-sigma)*median)) )
    print("lower:   ",lower)
    upper = int(min( 255, ((1.0+sigma)*median)) )
    print("upper:   ",upper)
    canny = cv.Canny(image,threshold1=lower,threshold2=upper)
    return canny

wide = cv.Canny(blured,10,220)
tight = cv.Canny(blured,200,230)
cannied = auto_canny(blured,0.5)

canny_images = np.hstack([wide,tight,cannied])
cv.imshow("original", blured)
cv.imshow("canny images", canny_images)

cv.waitKey(0)
cv.destroyAllWindows()