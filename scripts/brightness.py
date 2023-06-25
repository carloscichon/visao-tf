import cv2
from os import listdir, scandir
path = "/home/carlos/UFPR/tcc/tcc-carloscichon/affectnet_data_gray_test/"
subdirs = ["fear/", "disgust/", "contempt/"]
for subdir in subdirs:
    cpath = path+subdir
    for file in scandir(cpath):
        if file.is_file():
            #print("lendo " + path+file.name)
            img = cv2.imread(cpath+file.name)
            lowbright_image = cv2.convertScaleAbs(img, beta=-50)
            bright_image = cv2.convertScaleAbs(img, beta=50)
            #flip_image = cv2.flip(img, 1)
            newlow = cpath + "low/lowbright_" + file.name
            newb = cpath + "bright/bright_" + file.name

            #print(newfile)
            cv2.imwrite(newlow, lowbright_image)
            cv2.imwrite(newb, bright_image)

