import cv2 as cv

path = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\fingerprint.jpg"

image1 = cv.imread(path,0)          # -> the image have to be grey
image2 = cv.blur(image1,(5,5))

ret, simple_thresh = cv.threshold(src=image1,thresh=110,maxval=250,type=cv.THRESH_BINARY)
ret, simple_thresh = cv.threshold(src=image2,thresh=110,maxval=250,type=cv.THRESH_BINARY)

adaptive_mean1 = cv.adaptiveThreshold(image1,250,adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv.THRESH_BINARY,blockSize=11,C=2)
adaptive_mean2 = cv.adaptiveThreshold(image2,250,adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv.THRESH_BINARY,blockSize=11,C=2)

adaptive_gaussian1 = cv.adaptiveThreshold(image1,250,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
adaptive_gaussian2 = cv.adaptiveThreshold(image2,250,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)

cv.imshow("original_image1", image1)
cv.imshow("original_image2", image2)
cv.imshow("adaptive_mean1",adaptive_mean1)
cv.imshow("adaptive_mean2",adaptive_mean2)
cv.imshow("adaptive_gaussian1",adaptive_gaussian1)
cv.imshow("adaptive_gaussian2",adaptive_gaussian2)

cv.waitKey(0)
cv.destroyAllWindows()