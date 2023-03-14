import cv2 as cv

kamera = cv.VideoCapture(0)

while True:
    ret, goruntu = kamera.read()
    
    cv.imshow("kamera", goruntu)
    
    if cv.waitKey(30) & 0xFF == ('q'):
        break
    
kamera.release()
cv.destroyAllWindows()