import cv2 as cv

cam = cv.VideoCapture(0)

width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cam.get(cv.CAP_PROP_FPS)
frame_count = cam.get(cv.CAP_PROP_FRAME_COUNT)
saturation = cam.get(cv.CAP_PROP_SATURATION)
speed = cam.get(cv.CAP_PROP_SPEED)

print("\n\twidth: {}\n\
        height: {}\n\
        fps: {}\n\
        frame count: {}\n\
        saturation: {}\n\
        speed: {}".format(width,height,fps,frame_count,saturation,speed))

#four character codes
fourcc = cv.VideoWriter_fourcc(*".MP4")

path = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\kayit.mp4"
                        #filename,fourcc,fps,(width,height)
writer = cv.VideoWriter(path, fourcc, 25, (width,height))  # -> if you do not enter integer, program will be error

while True:
    ret, frame = cam.read()
    frame = cv.flip(frame,1)
    
    writer.write(frame)
    cv.imshow("pencere",frame)
    
    if cv.waitKey(30) & 0xFF == ord("q"):
        break
    
    
cam.release()
writer.release()
cv.destroyAllWindows()
    
    

