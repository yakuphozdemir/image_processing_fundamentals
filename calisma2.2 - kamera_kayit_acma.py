import cv2 as cv
import os

path = r"C:/Users/yakup/Desktop/image_proccess_exercises/example photos/sevgi.png"
pic = cv.imread(path)
print(pic.shape)
pic = cv.pyrDown(pic)
pic = cv.pyrDown(pic)
print(pic.shape)
height ,width, channels = pic.shape

cam = cv.VideoCapture(0)

while True:
    ret, frame = cam.read()
    
    cv.rectangle(frame,(200,100),(500,400),(0,255,0),3)
    cv.line(frame,(350,200),(350,300),(255,0,0),3)
    cv.circle(frame,(350,250),70,(240,240,0),3)
    cv.putText(frame,"Bu Yakup.",org=(250,75),fontFace=cv.FONT_HERSHEY_TRIPLEX,fontScale=1 ,color=(0,0,0),thickness=2)
    frame[0:height, 0:width] = pic
    cv.imshow("frame",frame)
    
    if cv.waitKey(25) & 0xFF == ord('q'):
        break
    
cam.release()
cv.destroyAllWindows()