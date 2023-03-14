import os
main_path = "C:/Users/yakup/Desktop/image_proccess_exercises/exp"


def check(x=0):
    while True:
        if os.path.isfile(main_path+"/"+"video"+str(x)+".avi"):
            x += 1
            check(x)
            break
        else:
            open(os.path.join(main_path+"/"+"video"+str(x)+".avi"),"w")
            break
            #with open(main_path+"/"+"video"+str(x)+".avi") as fp:
            #   pass
            
check(25663)