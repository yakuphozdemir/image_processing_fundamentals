import cv2 as cv
import time

video = cv.VideoCapture("samplevideo.mp4")
fps = video.get(cv.CAP_PROP_FPS)
frame_count = video.get(cv.CAP_PROP_FRAME_COUNT)
resolution = video.get(cv.CAP_PROP_FRAME_HEIGHT), video.get(cv.CAP_PROP_FRAME_WIDTH)
duration = frame_count/fps

print(f"resolution = {str(resolution)}")
print(f"fps = {str(fps)}")
print(f"number of frames = {str(frame_count)}")
print(f"duration (second) = {str(duration)}")
minutes = int(duration/60)
seconds = duration % 60
print(f"duration (Minute and second) = {minutes}:{seconds}")

t0 = time.time()
while True:
    ret, frame = video.read()
    
    if not ret:
        print("Camera is not working.")
        break
    
    t1 = time.time()
    t2 = t1 - t0
    if t2 <= duration:
        cv.imshow("video", frame)
        cv.waitKey(int(fps))

t3 = time.time()
check_time = t3-t0
print("Video bitti.")
print("time checking:   ", check_time)
video.release()
cv.destroyAllWindows()