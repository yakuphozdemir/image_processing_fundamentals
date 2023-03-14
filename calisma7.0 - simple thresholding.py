import cv2 as cv

path = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\fingerprint.jpg"

image = cv.imread(path)

ret, thresh1 = cv.threshold(src=image,thresh=110,maxval=250,type=cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(src=image,thresh=110,maxval=250,type=cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(image,110,250,cv.THRESH_MASK)
ret, thresh4 = cv.threshold(image,110,250,cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(image,110,250,cv.THRESH_TOZERO_INV)
#ret, thresh6 = cv.threshold(image,110,250,cv.THRESH_TRIANGLE)
ret, thresh7 = cv.threshold(image,110,250,cv.THRESH_TRUNC)
#ret, thresh8 = cv.threshold(image,110,250,cv.THRESH_OTSU)

cv.imshow("original",image)
cv.imshow("binary",thresh1)
cv.imshow("binary_inv",thresh2)
cv.imshow("mask",thresh3)
cv.imshow("to zero",thresh4)
cv.imshow("to zero_inv",thresh5)
#cv.imshow("triangle",thresh6)
cv.imshow("trunc",thresh7)
#cv.imshow("otsu",thresh8)

cv.waitKey(0)
cv.destroyAllWindows()