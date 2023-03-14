import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

path = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\train.jpg"

original = cv.imread(path)
original = cv.pyrDown(original)
original = cv.pyrDown(original)

mean_filter1 = cv.blur(original,(3,3))
mean_filter2 = cv.blur(original,(5,5))
mean_filter3 = cv.blur(original,(7,7))

median_filter1 = cv.medianBlur(original,3)
median_filter2 = cv.medianBlur(original,5)
median_filter3 = cv.medianBlur(original,7)

gauss_filter1 = cv.GaussianBlur(original,(3,3),0)
gauss_filter2 = cv.GaussianBlur(original,(5,5),0)
gauss_filter3 = cv.GaussianBlur(original,(7,7),0)

images = np.array([mean_filter1,mean_filter2,mean_filter3,
                    median_filter1,median_filter2,median_filter3,
                    gauss_filter1,gauss_filter2,gauss_filter3])

names = np.array(["mean_filter1","mean_filter2","mean_filter3",
                    "median_filter1","median_filter2","median_filter3",
                    "gauss_filter1","gauss_filter2","gauss_filter3"])

fig = plt.figure(figsize=(8, 8))
columns = 3
rows = 4
j=0
fig.add_subplot(rows,columns, 2)
plt.imshow(original)
plt.axis("off")
plt.title("original")
for i in range(4, columns*rows +1):
    fig.add_subplot(rows,columns, i)
    plt.imshow(images[j])
    plt.axis("off")
    plt.title(names[j])
    j+=1
plt.show()

"""
cv.imshow("original",original)

cv.imshow("mean_filter1",mean_filter1)
cv.imshow("mean_filter2",mean_filter2)
cv.imshow("mean_filter3",mean_filter3)

cv.imshow("median_filter1",median_filter1)
cv.imshow("median_filter2",median_filter2)
cv.imshow("median_filter3",median_filter3)

cv.imshow("gauss_filter1",gauss_filter1)
cv.imshow("gauss_filter2",gauss_filter2)
cv.imshow("gauss_filter3",gauss_filter3)

cv.waitKey(0)
cv.destroyAllWindows()
"""