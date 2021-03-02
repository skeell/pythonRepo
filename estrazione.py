#!/usr/bin/env pythonS

from PyQt5 import QtWidgets, uic
from random import *


def estrazione ():
    c = []
    for i in range(6):
        num = randint(1,90)
        if num not in c:
            c.append(num)
            c.sort()
    dlg.label.setText(str(c))
    
def cancella():
    dlg.label.setText("")

    


app = QtWidgets.QApplication([])
dlg = uic.loadUi("estrazione.ui")

dlg.btn.clicked.connect(estrazione)
dlg.btn_2.clicked.connect(cancella)

dlg.show()
app.exec()