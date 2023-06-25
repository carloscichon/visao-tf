import cv2
from os import listdir, scandir
path = "/home/carlos/UFPR/tcc/tcc-carloscichon/affectnet_data_gray_test/"
subdirs = ["fear/", "contempt/", "disgust/"]
for subdir in subdirs:
    cpath = path+subdir
    for file in scandir(cpath):
        if file.is_file():
            #print("lendo " + path+file.name)
            img = cv2.imread(cpath+file.name)
            lowcon_image = cv2.convertScaleAbs(img, alpha=0.5)
            con_image = cv2.convertScaleAbs(img, alpha=1.5)
            #flip_image = cv2.flip(img, 1)
            newlow = cpath + "low/lowcon_" + file.name
            newc = cpath + "con/con_" + file.name

            #print(newfile)
            cv2.imwrite(newlow, lowcon_image)
            cv2.imwrite(newc, con_image)

