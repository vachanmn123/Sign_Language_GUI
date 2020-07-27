# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import PyQt4

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 463)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.translate = QtWidgets.QPushButton(self.centralwidget)
        self.translate.setGeometry(QtCore.QRect(370, 10, 87, 29))
        self.translate.setObjectName("translate")
        self.input = QtWidgets.QTextEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(70, 10, 291, 91))
        self.input.setObjectName("input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 54, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 101, 17))
        self.label_2.setObjectName("label_2")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(13, 136, 541, 241))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("../sign_language_converter_python/signs/all_alphabets.jpg"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.prev = QtWidgets.QPushButton(self.centralwidget)
        self.prev.setGeometry(QtCore.QRect(60, 390, 87, 29))
        self.prev.setObjectName("prev")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(400, 390, 87, 29))
        self.next.setObjectName("next")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQUIT = QtWidgets.QAction(MainWindow)
        self.actionQUIT.setObjectName("actionQUIT")
        self.menuFile.addAction(self.actionQUIT)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.translate.setText(_translate("MainWindow", "Translate!!"))
        self.label.setText(_translate("MainWindow", "English"))
        self.label_2.setText(_translate("MainWindow", "Sign Language"))
        self.prev.setText(_translate("MainWindow", "prev."))
        self.next.setText(_translate("MainWindow", "next"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQUIT.setText(_translate("MainWindow", "QUIT"))
    def translate(self) :
        self.image.setPixmap(QtGui.QPixmap("../sign_language_converter_python/signs/a.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

