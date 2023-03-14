import cv2 as cv

video = cv.VideoCapture("samplevideo.mp4")

while video.isOpened():
    
    ret, frame = video.read()
    
    cv.imshow("video",frame)
    
    cv.waitKey(57000)
    
video.release()
cv.destroyAllWindows()