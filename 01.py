from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic
from random import *



class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)

    def btnEx(self):
        for i in range(6):
            c = randint(1,90)
            self.lbl.setText(self.lbl , QStringListModel(c) )


   


app=QApplication([])
window=Ui()
window.show()
app.exec_()
