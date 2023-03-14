import cv2 as cv

path = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\fingerprint.jpg"

image = cv.imread(path,0)            # -> the image have to be grey

ret, simple_thresh = cv.threshold(image,150,250,cv.THRESH_BINARY)

ret, otsu_thresh = cv.threshold(image,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

cv.imshow("original",image)
cv.imshow("simple", simple_thresh)
cv.imshow("otsu", otsu_thresh)

cv.waitKey(0)
cv.destroyAllWindows()