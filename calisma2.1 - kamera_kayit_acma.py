import cv2 as cv
import time

kamera = cv.VideoCapture(0)     # -> 0 is default camera , 1 -> usb,    2 -> recorded video
t0 = time.time()                # -> current time

print(kamera.get(3),kamera.get(4), " -> resolution")        # -> Camera Resolution Values
print(kamera.get(5), " -> fps")                                # -> Camera Fps Value

while True:
    ret, frame = kamera.read()  # -> ret = kamera is working or not
                                # -> frame = picture frame(çerçeve)
    if not ret:
        print("Camera is not working.")
        break
    t1 = time.time()             # -> current time
    t2 = t1 - t0
    t3 = 10  #(record time)
    
    if t2 <= t3:
        cv.imshow("kamera",frame)
        cv.waitKey(1)
    else:
        print(f"{int(t2)} saniye doldu caniim")
        #print(int(t2),"saniye doldu caniim")
        #print("{} saniye doldu caniim".format(int(t2)))
        #print(str(int(t2)) + " saniye doldu caniim")
        kamera.release()                # -> close to camera
        cv.destroyAllWindows()
        break