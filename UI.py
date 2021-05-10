import sys
import cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from cartoonlization import Photo2Cartoon
import os


def clearImage():
    path = './images/cartoon_result.png'
    if os.path.exists(path):
            os.remove(path)
    path = './images/cartoon_result_background.png'
    if os.path.exists(path):
            os.remove(path)

class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()

        self.resize(300, 400)

        self.label = QLabel(self)
        self.label.setFixedSize(256, 256)
        self.label.move(22, 20)
        self.setWindowTitle("Cartoon portrait Generator") 
        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )

        btn = QPushButton(self)
        btn.setText("Male Mode")
        btn.move(40, 316)
        btn.clicked.connect(self.TransferOnMale)

        btn = QPushButton(self)
        btn.setText("Female Mode")
        btn.move(180, 316)
        btn.clicked.connect(self.TransferOnFemale)

        btn = QPushButton(self)
        btn.setText("Save Image")
        btn.move(180, 356)
        btn.clicked.connect(self.SaveImage)

        btn = QPushButton(self)
        btn.setText("Add background")
        btn.move(40, 356)
        btn.clicked.connect(self.BlendBackground)

    def TransferOnFemale(self):
        clearImage()

        imgName, imgType = QFileDialog.getOpenFileName(self, "Open an image", "", "*.jpg;;*.png;;All Files(*)")
        if imgName == '':
            return

        c2p = Photo2Cartoon('./models/photo2cartoon_weightsfemale.pt')
        img = cv2.cvtColor(cv2.imread(imgName), cv2.COLOR_BGR2RGB)
        cartoon = c2p.FaceExtraction(img)
        if cartoon is not None:
            cv2.imwrite('./images/cartoon_result.png', cartoon)
            print('Cartoon portrait has been saved successfully!')
        imgName = './images/cartoon_result.png'
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

    def TransferOnMale(self):
        clearImage()
        imgName, imgType = QFileDialog.getOpenFileName(self, "Open an image", "", "*.jpg;;*.png;;All Files(*)")
        if imgName == '':
            return
        c2p = Photo2Cartoon('./models/photo2cartoon_weightsmale.pt')
        img = cv2.cvtColor(cv2.imread(imgName), cv2.COLOR_BGR2RGB)
        cartoon = c2p.FaceExtraction(img)
        if cartoon is not None:
            cv2.imwrite('./images/cartoon_result.png', cartoon)
            print('Cartoon portrait has been saved successfully!')
        imgName = './images/cartoon_result.png'
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)

    def SaveImage(self):
        if os.path.exists('./images/cartoon_result_background.png'):
            filename=QFileDialog.getSaveFileName(self,"Open an image", "", "*.jpg;;*.png;;All Files(*)")
            print(filename)
            img = cv2.cvtColor(cv2.imread('./images/cartoon_result_background.png'), cv2.IMREAD_COLOR)
            cv2.imwrite(filename[0], img)
        elif os.path.exists('./images/cartoon_result.png'):
            filename=QFileDialog.getSaveFileName(self,"Open an image", "", "*.jpg;;*.png;;All Files(*)")
            print(filename)
            img = cv2.cvtColor(cv2.imread('./images/cartoon_result.png'), cv2.IMREAD_COLOR)
            cv2.imwrite(filename[0], img)
        else:
            print("no image generated yet!")
            return

    def BlendBackground(self):
        if os.path.exists('./images/cartoon_result.png'):
            imgName, imgType = QFileDialog.getOpenFileName(self, "Open an image", "", "*.jpg;;*.png;;All Files(*)")
            if imgName == '':
                return

            img1 = cv2.cvtColor(cv2.imread(imgName), cv2.COLOR_BGR2RGB)
            img2 = cv2.imread('./images/cartoon_result.png',cv2.IMREAD_COLOR)
            img1 = cv2.resize(img1, (256,256))
            rows, cols, channels = img2.shape
            roi = img1[0:rows, 0:cols]
            img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            ret, mask = cv2.threshold(img2gray, 254, 255, cv2.THRESH_BINARY)
            mask_inv = cv2.bitwise_not(mask)
            img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
            img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
            dst = cv2.add( img2_fg,img1_bg)
            img1[0:rows, 0:cols] = dst
            cv2.imwrite('./images/cartoon_result_background.png',img1)

            imgName = './images/cartoon_result_background.png'
            jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
            self.label.setPixmap(jpg)
        else:
            print("no image generated yet!")
            return



if __name__ == "__main__":
    clearImage()
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())
