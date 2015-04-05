# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'web2pdf.ui'
#
# Created: Sat Apr 04 21:59:14 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

global filename
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.window = MainWindow
        self.filename=""
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(480, 200)
        MainWindow.setMinimumSize(QtCore.QSize(480, 200))
        MainWindow.setMaximumSize(QtCore.QSize(480, 200))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/web2pdf/filetype_pdf.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox_3 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.comboBox_3)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout.addWidget(self.progressBar, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("pressed()")), MainWindow.close)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("pressed()")), self.save_file)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("pressed()")), self.Download)
        self.web = QWebView()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Web2Pdf--By Anurag Goel", None))
        self.label.setText(_translate("MainWindow", "URL :", None))
        self.lineEdit.setText(_translate("MainWindow", "http://www.google.co.in", None))
        self.label_2.setText(_translate("MainWindow", "Page Size :", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "A0", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "A1", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "A2", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "A3", None))
        self.comboBox.setItemText(4, _translate("MainWindow", "A4", None))
        self.comboBox.setItemText(5, _translate("MainWindow", "A5", None))
        self.comboBox.setItemText(6, _translate("MainWindow", "A6", None))
        self.comboBox.setItemText(7, _translate("MainWindow", "A7", None))
        self.comboBox.setItemText(8, _translate("MainWindow", "A8", None))
        self.comboBox.setItemText(9, _translate("MainWindow", "A9", None))
        self.comboBox.setItemText(10, _translate("MainWindow", "B0", None))
        self.comboBox.setItemText(11, _translate("MainWindow", "B1", None))
        self.comboBox.setItemText(12, _translate("MainWindow", "B2", None))
        self.comboBox.setItemText(13, _translate("MainWindow", "B3", None))
        self.comboBox.setItemText(14, _translate("MainWindow", "B4", None))
        self.comboBox.setItemText(15, _translate("MainWindow", "B5", None))
        self.comboBox.setItemText(16, _translate("MainWindow", "B6", None))
        self.comboBox.setItemText(17, _translate("MainWindow", "B7", None))
        self.comboBox.setItemText(18, _translate("MainWindow", "B8", None))
        self.comboBox.setItemText(19, _translate("MainWindow", "B9", None))
        self.comboBox.setItemText(20, _translate("MainWindow", "B10", None))
        self.comboBox.setItemText(21, _translate("MainWindow", "C5E", None))
        self.comboBox.setItemText(22, _translate("MainWindow", "Comm10E", None))
        self.comboBox.setItemText(23, _translate("MainWindow", "DLE", None))
        self.comboBox.setItemText(24, _translate("MainWindow", "Executive", None))
        self.comboBox.setItemText(25, _translate("MainWindow", "Folio", None))
        self.comboBox.setItemText(26, _translate("MainWindow", "Ledger", None))
        self.comboBox.setItemText(27, _translate("MainWindow", "Legal", None))
        self.comboBox.setItemText(28, _translate("MainWindow", "Letter", None))
        self.comboBox.setItemText(29, _translate("MainWindow", "Tabloid", None))
        self.label_3.setText(_translate("MainWindow", "Color Mode : ", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Color", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Grayscale", None))
        self.label_4.setText(_translate("MainWindow", "Orientation :", None))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Portrait", None))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Landscape", None))
        self.label_5.setText(_translate("MainWindow", "Choose a name to Save", None))
        self.pushButton_3.setText(_translate("MainWindow", "Save As", None))
        self.pushButton_2.setText(_translate("MainWindow", "Download ", None))
        self.pushButton.setText(_translate("MainWindow", "Exit", None))
        self.comboBox.setCurrentIndex(4)
    def save_file(self):
        self.filename = str(QtGui.QFileDialog.getSaveFileName(self.window,str(self.label_5.text())))
        self.var=len(str(self.filename).split('/'))
        self.file_name_abs = str(self.filename).split('/')[self.var-1]
        self.label_5.setText(self.file_name_abs+".pdf")
    def Download(self):
        url=self.lineEdit.text()
        http = "http://"
        www = "www."
        if www in url and http not in url:
            url = http + url

        elif "." not in url:
            url = "http://www.google.com/search?q="+url

        elif http in url and www not in url:
            url = url[:7] + www + url[7:]

        elif http and www not in url:
            url = http + www + url

        self.url=url
        self.web = QWebView(loadProgress = self.progressBar.setValue)
        self.web.load(QUrl(url))
        #web.show()
        QObject.connect(self.web, SIGNAL("loadFinished(bool)"), self.convert)

    def convert(self):
        page_size=[QPrinter.A0,QPrinter.A1,QPrinter.A2,QPrinter.A3,QPrinter.A4,QPrinter.A5,QPrinter.A5,QPrinter.A6,QPrinter.A7,QPrinter.A8,
                  QPrinter.A8,QPrinter.A9,QPrinter.B0,QPrinter.B1,QPrinter.B2,QPrinter.B3,QPrinter.B4,QPrinter.B5,QPrinter.B6,QPrinter.B7,
                  QPrinter.B8,QPrinter.B9,QPrinter.B10,QPrinter.C5E,QPrinter.Comm10E,QPrinter.DLE,QPrinter.Executive,QPrinter.Folio,QPrinter.Ledger,
                  QPrinter.Legal,QPrinter.Ledger,QPrinter.Tabloid]
        page_color=[QPrinter.Color,QPrinter.GrayScale]
        page_or =[QPrinter.Portrait,QPrinter.Landscape]
        ind1= self.comboBox.currentIndex()
        ind2= self.comboBox_2.currentIndex()
        ind3= self.comboBox_3.currentIndex()
        self.url=self.url.split(".")[1]
        self.printer = QPrinter()
        self.printer.setPageSize(page_size[ind1])
        self.printer.setOutputFormat(QPrinter.PdfFormat)
        self.printer.setColorMode(page_color[ind2])
        self.printer.setOrientation(page_or[ind3])
        if self.filename != "":
            self.printer.setOutputFileName(self.filename+".pdf")
        else:
            self.printer.setOutputFileName(self.url+".pdf")
        self.web.print_(self.printer)
        print "Downloaded!"


import web2pdf_qrc_rc
import sys
if __name__ == '__main__' :
    app = QtGui.QApplication(sys.argv)

mainWindow = QtGui.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
sys.exit(app.exec_())