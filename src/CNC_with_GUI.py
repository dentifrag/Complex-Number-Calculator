from CNC_GUI_Final import *
import sys
import cmath
from PyQt5 import QtCore, QtGui, QtWidgets



def get_numbers(self):
    global a,b,c,d
    a = int(self.a_input_value.text())
    b = int(self.b_input_value.text())
    c = int(self.c_input_value.text())
    d = int(self.d_input_value.text())
    return a,b,c,d

def complex_number_add(self):
    get_numbers(self)
    answer = complex(a,b) + complex(c,d)
    answer = str(answer)
    self.textBrowser.setText(answer.replace('j', 'i').strip('()'))

def complex_number_sub(self):
    get_numbers(self)
    answer = complex(a,b) - complex(c,d)
    answer = str(answer)
    self.textBrowser.setText(answer.replace('j', 'i').strip('()'))

def complex_number_multi(self):
    get_numbers(self)
    answer = complex(a,b) * complex(c,d)
    answer = str(answer)
    self.textBrowser.setText(answer.replace('j', 'i').strip('()'))

def complex_number_div(self):
    get_numbers(self)
    answer = complex(a,b) / complex(c,d)
    answer = str(answer)
    self.textBrowser.setText(answer.replace('j', 'i').strip('()'))
    


class App(Ui_mainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self):
        choice = self.comboBox.currentText()

        if choice == 'Addition':
            complex_number_add(self)

        elif choice == 'Subtraction':
            complex_number_sub(self)
        
        elif choice == 'Multiplication':
            complex_number_multi(self)
        
        elif choice == 'Division':
            complex_number_div(self)
        
        
            
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = App(MainWindow)

MainWindow.show()
app.exec_()
