import sys
import cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from test import Photo2Cartoon

class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()

        self.resize(600, 800)

        self.label = QLabel(self)
        self.label.setFixedSize(400, 400)
        self.label.move(0, 0)

        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )

        btn = QPushButton(self)
        btn.setText("Open an image")
        btn.move(10, 30)
        btn.clicked.connect(self.openimage)

    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "Open an image", "", "*.jpg;;*.png;;All Files(*)")
        c2p = Photo2Cartoon()
        img = cv2.cvtColor(cv2.imread(imgName), cv2.COLOR_BGR2RGB)
        cartoon = c2p.inference(img)
        if cartoon is not None:
            cv2.imwrite('./images/cartoon_result.png', cartoon)
            print('Cartoon portrait has been saved successfully!')
        imgName = './images/cartoon_result.png'
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())
