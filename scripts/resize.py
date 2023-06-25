import cv2
from os import listdir, scandir
path = "/home/carlos/UFPR/tcc/tcc-carloscichon/data_emotionet/"

x = 0

for file in scandir(path):
    x = x + 1
    if file.is_file():
        print("lendo " + path+file.name)
        img = cv2.imread(path+file.name)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        dim = (48,48)
        result = cv2.resize(gray_img, dim)
        newfile = path + "/gray/" + file.name
        print(newfile)
        cv2.imwrite(newfile, result)

print(x)



