from __future__ import division
import sys
from PyQt4 import QtCore, QtGui, uic
import time

qtCreatorFile = "main_correct.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.translate.clicked.connect(self.translate1)
        self.image.setPixmap(QtGui.QPixmap("./signs/all_alphabets.jpg"))
    
    def translate1(self):
        inp = str(self.iuy.toPlainText())
        length = len(inp)
        i = 0
        while i <= length - 1:
            if (inp[i]) == 'a' :
                
                self.image.setPixmap(QtGui.QPixmap("./signs/a.jpg"))
            elif (inp[i]) == 'b' :
                
                self.image.setPixmap(QtGui.QPixmap("./signs/b.jpg"))
            elif (inp[i]) == 'c' :
                
                self.image.setPixmap(QtGui.QPixmap("./signs/c.jpg"))
            
            i = i + 1

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
