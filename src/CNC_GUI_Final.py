# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CNC_GUI_Updated.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(640, 509)
        font = QtGui.QFont()
        font.setPointSize(8)
        mainWindow.setFont(font)
        mainWindow.setStyleSheet("background-color:#dae5f0;\n"
"border-style:outset;\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CNC_label = QtWidgets.QLabel(self.centralwidget)
        self.CNC_label.setGeometry(QtCore.QRect(10, 10, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.CNC_label.setFont(font)
        self.CNC_label.setStyleSheet("border: 3px outset #000000;\n"
"border-radius: 13px;\n"
"box-shadow: 4px 4px 15px 1px #000000;\n"
"text-transform: uppercase;")
        self.CNC_label.setObjectName("CNC_label")
        self.com_num_1_label = QtWidgets.QLabel(self.centralwidget)
        self.com_num_1_label.setGeometry(QtCore.QRect(20, 90, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.com_num_1_label.setFont(font)
        self.com_num_1_label.setStyleSheet("text-transform: uppercase;")
        self.com_num_1_label.setObjectName("com_num_1_label")
        self.com_num_2_label = QtWidgets.QLabel(self.centralwidget)
        self.com_num_2_label.setGeometry(QtCore.QRect(380, 90, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.com_num_2_label.setFont(font)
        self.com_num_2_label.setStyleSheet("text-transform: uppercase;")
        self.com_num_2_label.setObjectName("com_num_2_label")
        self.what_is_a_label = QtWidgets.QLabel(self.centralwidget)
        self.what_is_a_label.setGeometry(QtCore.QRect(20, 150, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.what_is_a_label.setFont(font)
        self.what_is_a_label.setObjectName("what_is_a_label")
        self.a_input_value = QtWidgets.QLineEdit(self.centralwidget)
        self.a_input_value.setGeometry(QtCore.QRect(90, 150, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.a_input_value.setFont(font)
        self.a_input_value.setStyleSheet("background-color:#f0f5fa;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;")
        self.a_input_value.setText("")
        self.a_input_value.setObjectName("a_input_value")
        self.what_is_b_label = QtWidgets.QLabel(self.centralwidget)
        self.what_is_b_label.setGeometry(QtCore.QRect(20, 210, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.what_is_b_label.setFont(font)
        self.what_is_b_label.setObjectName("what_is_b_label")
        self.b_input_value = QtWidgets.QLineEdit(self.centralwidget)
        self.b_input_value.setGeometry(QtCore.QRect(90, 210, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.b_input_value.setFont(font)
        self.b_input_value.setStyleSheet("background-color:#f0f5fa;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;")
        self.b_input_value.setText("")
        self.b_input_value.setObjectName("b_input_value")
        self.what_is_c_label = QtWidgets.QLabel(self.centralwidget)
        self.what_is_c_label.setGeometry(QtCore.QRect(430, 150, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.what_is_c_label.setFont(font)
        self.what_is_c_label.setObjectName("what_is_c_label")
        self.what_is_d_label = QtWidgets.QLabel(self.centralwidget)
        self.what_is_d_label.setGeometry(QtCore.QRect(430, 210, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.what_is_d_label.setFont(font)
        self.what_is_d_label.setObjectName("what_is_d_label")
        self.d_input_value = QtWidgets.QLineEdit(self.centralwidget)
        self.d_input_value.setGeometry(QtCore.QRect(500, 210, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.d_input_value.setFont(font)
        self.d_input_value.setStyleSheet("background-color:#f0f5fa;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;")
        self.d_input_value.setText("")
        self.d_input_value.setObjectName("d_input_value")
        self.c_input_value = QtWidgets.QLineEdit(self.centralwidget)
        self.c_input_value.setGeometry(QtCore.QRect(500, 150, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.c_input_value.setFont(font)
        self.c_input_value.setStyleSheet("background-color:#f0f5fa;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;")
        self.c_input_value.setText("")
        self.c_input_value.setObjectName("c_input_value")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 270, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:#f0f5fa;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 310, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#5b90c2;\n"
"color:#212529;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"border-color:#6995c2;\n"
"text-transform: uppercase;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(200, 360, 256, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color:#f0f5fa;\n"
"font-size: 20px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:5px;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 130, 231, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(380, 130, 231, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 360, 191, 71))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.what_is_b_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.what_is_b_label_2.setGeometry(QtCore.QRect(210, 210, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.what_is_b_label_2.setFont(font)
        self.what_is_b_label_2.setObjectName("what_is_b_label_2")
        self.what_is_b_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.what_is_b_label_3.setGeometry(QtCore.QRect(620, 210, 16, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.what_is_b_label_3.setFont(font)
        self.what_is_b_label_3.setObjectName("what_is_b_label_3")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 20))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Complex Number Calculator"))
        self.CNC_label.setText(_translate("mainWindow", "Complex Number Calculator"))
        self.com_num_1_label.setText(_translate("mainWindow", "Complex Number 1:"))
        self.com_num_2_label.setText(_translate("mainWindow", "Complex Number 2:"))
        self.what_is_a_label.setText(_translate("mainWindow", "a = "))
        self.what_is_b_label.setText(_translate("mainWindow", "b ="))
        self.what_is_c_label.setText(_translate("mainWindow", "c ="))
        self.what_is_d_label.setText(_translate("mainWindow", "d ="))
        self.comboBox.setItemText(0, _translate("mainWindow", "Addition"))
        self.comboBox.setItemText(1, _translate("mainWindow", "Subtraction"))
        self.comboBox.setItemText(2, _translate("mainWindow", "Multiplication"))
        self.comboBox.setItemText(3, _translate("mainWindow", "Division"))
        self.pushButton.setText(_translate("mainWindow", "Calculate"))
        self.textBrowser.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:32pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> For division problems go to <span style=\" color:#0055ff;\">\'https://www.mathsisfun.com/converting-decimals-fractions-solver.html</span><span style=\" color:#000000;\">\'</span> input decimals and \'approxmate \'</p></body></html>"))
        self.what_is_b_label_2.setText(_translate("mainWindow", "i"))
        self.what_is_b_label_3.setText(_translate("mainWindow", "i"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

