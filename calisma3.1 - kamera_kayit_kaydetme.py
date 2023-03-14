import time
import cv2 as cv

cam1 = cv.VideoCapture(0)
t0 = time.time()

cam2 = cv.VideoWriter_fourcc(*"XVID")

path = r"C:\Users\yakup\Desktop\image_proccess_exercises\example photos\video.avi"

out = cv.VideoWriter(path, cam2, 30, (640,480))

while cam1.isOpened():
    ret, frame = cam1.read()
    
    if ret == 0:
        print("Camera is not working.")
        break
    
    t1 = time.time()
    t2 = t1 - t0
    t3 = 10
    
    if t2 <= t3:
        out.write(frame)
        cv.imshow("kamera", frame)
        cv.waitKey(1)
    else:
        print(f"{time} saniye vakit doldu caniim", t3)
        cam1.release()
        out.release()
        cv.destroyAllWindows()
        break