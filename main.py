import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget
import math
class Calculator(QWidget):
    def __init__(self):
        self.start()
        self.set()

        self.temp=""
        self.t=0

    def start(self):
        self.ui=uic.loadUi(r"C:\Users\polop\OneDrive\Документы\Python\calculator\cal.ui")
        self.ui.show()

    def set(self):
        self.ui.btn_0.clicked.connect(lambda:self.click(num=0))
        self.ui.btn_1.clicked.connect(lambda:self.click(num=1))
        self.ui.btn_2.clicked.connect(lambda:self.click(num=2))
        self.ui.btn_3.clicked.connect(lambda:self.click(num=3))
        self.ui.btn_4.clicked.connect(lambda:self.click(num=4))
        self.ui.btn_5.clicked.connect(lambda:self.click(num=5))
        self.ui.btn_6.clicked.connect(lambda:self.click(num=6))
        self.ui.btn_7.clicked.connect(lambda:self.click(num=7))
        self.ui.btn_8.clicked.connect(lambda:self.click(num=8))
        self.ui.btn_9.clicked.connect(lambda:self.click(num=9))
        
        self.ui.btn_clear.clicked.connect(lambda:self.clear())
        self.ui.btn_d.clicked.connect(lambda:self.share())
        self.ui.btn_eq.clicked.connect(lambda:self.equally())
        self.ui.btn_min.clicked.connect(lambda:self.minus())
        self.ui.btn_plus.clicked.connect(lambda:self.plus())
        self.ui.btn_x.clicked.connect(lambda:self.multiplay())
        self.ui.btn_square.clicked.connect(lambda:self.square())
        self.ui.btn_3square.clicked.connect(lambda:self.triplesquare())
        self.ui.sin.clicked.connect(lambda:self.sin())
        self.ui.cos.clicked.connect(lambda:self.cos())


    def click(self,num=1):
        self.display(text=num)
    def clear(self):
        self.ui.label.setText('0')
    def display(self,text='0'):
        obj=self.ui.label
        text_old=obj.text()
        if text_old=="0":
            text_old=""
        text="%s%s" %(text_old,text)
        obj.setText(text)

    def plus (self):
        self.temp=int(self.ui.label.text())
        self.ui.label.setText(' ')
        self.t=1

    def minus (self):
        self.temp=int(self.ui.label.text())
        self.ui.label.setText(' ')
        self.t=2

    def multiplay (self):
        self.temp=int(self.ui.label.text())
        self.ui.label.setText(' ')
        self.t=3

    def share (self):
        self.temp=int(self.ui.label.text())
        self.ui.label.setText(' ')
        self.t=4

    def square (self):
        self.temp=int(self.ui.label.text())
        self.ui.label.setText(' ')
        self.t=5

    def triplesquare (self):
        self.temp=int(self.ui.label.text())
        self.ui.label.setText(' ')
        self.t=6

    def sin(self):
        self.temp=int(self.ui.label.text())
        self.ui.label.setText(' ')
        self.t=7
    def cos(self):
        self.temp=int(self.ui.label.text())
        self.ui.label.setText(' ')
        self.t=8

    def equally(self):
        if self.t==1:
            eq=self.temp+int(self.ui.label.text())
            self.ui.label.setText(str(eq))
        if self.t==2:
            eq=self.temp-int(self.ui.label.text())
            self.ui.label.setText(str(eq))
        if self.t==3:
            eq=self.temp*int(self.ui.label.text())
            self.ui.label.setText(str(eq))
        if self.t==4:
            eq=self.temp/int(self.ui.label.text())
            self.ui.label.setText(str(eq))
        if self.t==5:
            eq=self.temp**2
            self.ui.label.setText(str(eq))
        if self.t==6:
            eq=self.temp**3
            self.ui.label.setText(str(eq))
        if self.t==7:
            eq=math.sin(self.temp)
            self.ui.label.setText(str(eq))
        if self.t==8:
            eq=math.cos(self.temp)
            self.ui.label.setText(str(eq))

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Calculator()
    app.exec_()
    
        
