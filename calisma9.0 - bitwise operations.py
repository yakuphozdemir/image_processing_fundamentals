import cv2 as cv

path1 = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\bitwise_photos\bitwise_op1.png"
path2 = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\bitwise_photos\bitwise_op2.png"

image1 = cv.imread(path1)
image2 = cv.imread(path2)

bitwise_and = cv.bitwise_and(image1,image2)
bitwise_or = cv.bitwise_or(image1,image2)
bitwise_xor = cv.bitwise_xor(image1,image2)
bitwise_not1 = cv.bitwise_not(image1)
bitwise_not2 = cv.bitwise_not(image2)

cv.imshow("image1",image1)
cv.imshow("image2",image2)
cv.imshow("bitwise_and",bitwise_and)
cv.imshow("bitwise_or",bitwise_or)
cv.imshow("bitwise_xor",bitwise_xor)
cv.imshow("bitwise_not1",bitwise_not1)
cv.imshow("bitwise_not2",bitwise_not2)

cv.waitKey(0)
cv.destroyAllWindows()