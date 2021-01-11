from __future__ import division
import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
import time

qtCreatorFile = "main_correct.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.translate.clicked.connect(self.translate1)
        self.image.setPixmap(QtGui.QPixmap("./signs/all_alphabets.jpg"))
    
    def translate1(self):
        inp = str(self.iuy.text())
        length = len(inp)
        i = 0
        while i <= length - 1:
            if (inp[i]) == 'a' :
                self.image.setPixmap(QtGui.QPixmap("./signs/a.jpg"))
            elif (inp[i]) == 'b' :
                self.image.setPixmap(QtGui.QPixmap("./signs/b.jpg"))
            elif (inp[i]) == 'c' :
                self.image.setPixmap(QtGui.QPixmap("./signs/c.jpg"))
            elif (inp[i]) == 'd':
                self.image.setPixmap(QtGui.QPixmap("./signs/d.jpg"))
            elif (inp[i]) == 'e':
                self.image.setPixmap(QtGui.QPixmap("./signs/e.jpg"))
            elif (inp[i]) == 'f':
                self.image.setPixmap(QtGui.QPixmap("./signs/f.jpg"))
            elif (inp[i]) == 'g':
                self.image.setPixmap(QtGui.QPixmap("./signs/g.jpg"))
            elif (inp[i]) == 'h':
                self.image.setPixmap(QtGui.QPixmap("./signs/h.jpg"))
            elif (inp[i]) == 'i':
                self.image.setPixmap(QtGui.QPixmap("./signs/i.jpg"))
            elif (inp[i]) == 'j':
                self.image.setPixmap(QtGui.QPixmap("./signs/j.jpg"))
            elif (inp[i]) == 'k':
                self.image.setPixmap(QtGui.QPixmap("./signs/k.jpg"))
            elif (inp[i]) == 'l':
                self.image.setPixmap(QtGui.QPixmap("./signs/l.jpg"))
            elif (inp[i]) == 'm':
                self.image.setPixmap(QtGui.QPixmap("./signs/m.jpg"))
            elif (inp[i]) == 'n':
                self.image.setPixmap(QtGui.QPixmap("./signs/n.jpg"))
            elif (inp[i]) == 'o':
                self.image.setPixmap(QtGui.QPixmap("./signs/o.jpg"))
            elif (inp[i]) == 'p':
                self.image.setPixmap(QtGui.QPixmap("./signs/p.jpg"))
            elif (inp[i]) == 'q':
                self.image.setPixmap(QtGui.QPixmap("./signs/q.jpg"))
            elif (inp[i]) == 'r':
                self.image.setPixmap(QtGui.QPixmap("./signs/r.jpg"))
            elif (inp[i]) == 's':
                self.image.setPixmap(QtGui.QPixmap("./signs/s.jpg"))
            elif (inp[i]) == 't':
                self.image.setPixmap(QtGui.QPixmap("./signs/t.jpg"))
            elif (inp[i]) == 'u':
                self.image.setPixmap(QtGui.QPixmap("./signs/u.jpg"))
            elif (inp[i]) == 'v':
                self.image.setPixmap(QtGui.QPixmap("./signs/v.jpg"))
            elif (inp[i]) == 'w':
                self.image.setPixmap(QtGui.QPixmap("./signs/w.jpg"))
            elif (inp[i]) == 'x':
                self.image.setPixmap(QtGui.QPixmap("./signs/x.jpg"))
            elif (inp[i]) == 'y':
                self.image.setPixmap(QtGui.QPixmap("./signs/y.jpg"))
            elif (inp[i]) == 'z':
                self.image.setPixmap(QtGui.QPixmap("./signs/z.jpg"))
            else:
                self.image.setPixmap(QtGui.QPixmap("./signs/all_alphabets.jpg"))

            i = i + 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
