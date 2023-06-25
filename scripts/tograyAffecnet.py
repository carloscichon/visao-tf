import cv2
from os import scandir

path = "/home/carlos/UFPR/tcc/tcc-carloscichon/affectnet_data/"
newpath = "/home/carlos/UFPR/tcc/tcc-carloscichon/affectnet_data_gray/"

subdir = "surprise/"

for file in scandir(path+subdir):
    if file.is_file():
        #print(path+subdir+file.name)
        img = cv2.imread(path+subdir+file.name)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(newpath+subdir+file.name, gray_img)