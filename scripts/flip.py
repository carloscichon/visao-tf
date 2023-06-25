import cv2
from os import listdir, scandir
path = "/home/carlos/UFPR/tcc/tcc-carloscichon/affectnet_data_gray_test/"
subdirs = ["anger/", "sad/", "contempt/", "fear/", "surprise/", "disgust/"]

for subdir in subdirs:
    cpath = path+subdir
    for file in scandir(cpath):
        if file.is_file():
            #print("lendo " + cpath+file.name)
            img = cv2.imread(cpath+file.name)
            flip_image = cv2.flip(img, 1)
            newfile = cpath + "flip/flipped_" + file.name
            #print(newfile)
            cv2.imwrite(newfile, flip_image)