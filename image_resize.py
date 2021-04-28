# coding: utf-8
import cv2 as cv
import os


def ResizeImage(file_path,new_path):
    i = 0
    for filename in os.listdir(file_path):
        img = cv.imread(file_path+'/'+filename)
        filename_new = new_path+"/new" + str(i) + '.png'
        img2 = cv.resize(img,(512,512))
        cv.imwrite(filename_new,img2)
        print(filename_new)
        i += 1

def FileRename(file_path):
    fileList = os.listdir(file_path)
    n = 0
    for filename in fileList:
        oldName = file_path + os.sep + fileList[n]
        newName = file_path + os.sep + str(n) + '.png'
        os.rename(oldName,newName)
        print(oldName,'======>',newName)
        n += 1

if __name__ == '__main__':
    file_path = 'D:/final project/dataset'
    new_path = 'D:/final project/datasetResized'
    #FileRename(file_path)
    ResizeImage(file_path,new_path)