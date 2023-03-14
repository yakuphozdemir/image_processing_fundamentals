from calisma6_0_kernel import kernel
import cv2 as cv
import numpy as np

kernel1 = kernel(1)

path1 = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\noisy_photos\morp_exp1.png"
#path2 = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\morp_exp2.png"
#path3 = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\morp_exp3.png"

org1 = cv.imread(path1)
#org1 = cv.pyrDown(org1)
#cv.imwrite(path1,org1)
eroseded1 = cv.erode(org1,kernel1,iterations=1)                         # -> asindirma, beyaz noktalarin, gurultulerin giderilmesini saglar
dilated1 = cv.dilate(org1,kernel1,iterations=1)                         # -> genisletme,
dilated2 = cv.dilate(eroseded1,kernel1)
opened1 = cv.morphologyEx(org1,cv.MORPH_OPEN,kernel1)                   # erosion + dilation
closed1 = cv.morphologyEx(org1,cv.MORPH_CLOSE,kernel1)                  # dilation + erosion
gradyan1 = cv.morphologyEx(org1,cv.MORPH_GRADIENT,kernel1)              # dilation - erosion
tophat1 = cv.morphologyEx(org1,cv.MORPH_TOPHAT,kernel1)                 # original - opened
blackhat1 = cv.morphologyEx(org1,cv.MORPH_BLACKHAT,kernel1)             # original - closed

cv.imshow("original1",org1)
cv.imshow("eroseded1",eroseded1)    
cv.imshow("dilated1",dilated1)       
cv.imshow("dilated2",dilated2)  
cv.imshow("opened1",opened1)        
cv.imshow("closed1",closed1)   
cv.imshow("gradyan1",gradyan1) 
cv.imshow("tophat1",tophat1)
cv.imshow("blackhat1",blackhat1)

cv.waitKey(0)
cv.destroyAllWindows()

