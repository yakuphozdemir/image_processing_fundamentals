import cv2

path = r'C:\Users\yakup\Desktop\image_proccess_exercises\test\example.jpg'
a = cv2.imread(path)

while True:
    try:
        kelime = input("Lutfen sihirli kelimeyi giriniz: ")
        if kelime == "Kemalcik" or kelime == "kemalcik":
            break
        else:
            print("Yanlis, Lutfen canim hocam, sevgili pasamin ismini girmeniz gerekli (ipucu:kemalcik)" )        
    except ValueError:
        print("Yanlis, Lutfen canim hocam, sevgili pasamin ismini girmeniz gerekli (ipucu:kemalcik)" )
        continue 

b = cv2.imshow(winname="porkatal", mat=a)
cv2.waitKey(10000)
cv2.destroyAllWindows()
print("\n")   
input("Lutfen sevgili pasamin programinin sonlanmasi icin bir tusa basiniz.")