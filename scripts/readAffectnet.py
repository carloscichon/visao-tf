import numpy as np
import pandas as pd
import cv2
import os

anopath = "/home/carlos/UFPR/tcc/tcc-carloscichon/train_set/annotations/"
imgpath = "/home/carlos/UFPR/tcc/tcc-carloscichon/train_set/images/"
newimgpath = "/home/carlos/UFPR/tcc/tcc-carloscichon/affectnet_data/"

#x = 0

for file in os.scandir(anopath):
    split = file.name.split("_")
    name = split[0]
    file_type = split[1].split(".")[0]
    #print(file_type)
    if file_type == "exp":
        exp = np.load(anopath+file.name)
        #print(exp)
        if int(exp)==0:
            os.rename(imgpath+name+".jpg", newimgpath+"neutral/"+name+".jpg")
        if int(exp)==1:
            os.rename(imgpath+name+".jpg", newimgpath+"happy/"+name+".jpg")
        if int(exp)==2:
            os.rename(imgpath+name+".jpg", newimgpath+"sad/"+name+".jpg")
        if int(exp)==3:
            os.rename(imgpath+name+".jpg", newimgpath+"surprise/"+name+".jpg")
        if int(exp)==4:
            os.rename(imgpath+name+".jpg", newimgpath+"fear/"+name+".jpg")
        if int(exp)==5:
            os.rename(imgpath+name+".jpg", newimgpath+"disgust/"+name+".jpg")
        if int(exp)==6:
            os.rename(imgpath+name+".jpg", newimgpath+"anger/"+name+".jpg")
        if int(exp)==7:
            os.rename(imgpath+name+".jpg", newimgpath+"contempt/"+name+".jpg")
    