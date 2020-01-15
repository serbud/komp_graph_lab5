import sys
import os
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import QCoreApplication, pyqtSlot
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw

imageroute = sys.argv[1]
imageroute2 = "buffer1.bmp"



class Example(QWidget):



    def __init__(self):
        super().__init__()
        self.initUI()
        # self.applyChanges()




    def initUI(self):
        global imageroute
        global imageroute2
        os.system(f"python encode.py {imageroute}")
        jsonroute = imageroute.split(".")[0] + ".json"
        os.system(f"python decode.py {imageroute2} {jsonroute}")
        self.imageLabel = QLabel(self)
        self.pixmap = QPixmap(imageroute)
        # print("ccc",self.pixmap.)
        self.imageLabel.setPixmap(self.pixmap)
        self.imageLabel.move(50, 50)
        self.imageLabel2 = QLabel(self)
        self.pixmap2 = QPixmap(imageroute2)
        self.imageLabel2.setPixmap(self.pixmap2)
        self.imageLabel2.move(50 + self.pixmap.width() + 50, 50)
        self.resize(50 + self.pixmap.width() + self.pixmap2.width() + 100, 50 + self.pixmap.height()  + 50)
        self.center()
        self.vl = QLabel("Исходное изображение", self)
        self.vl.move( + self.pixmap.width()//2 , 25)
        self.vm = QLabel("Декодированное изображение", self)
        self.vm.move(50 + self.pixmap.width() + self.pixmap2.width() // 2, 25)




        self.setWindowTitle('Center')
        self.show()


    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()



    sys.exit(app.exec_())