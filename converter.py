from PyQt5 import QtWidgets, uic

def Convert():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit.text())*1.23))
    



app = QtWidgets.QApplication([])
dlg = uic.loadUi("convert.ui")

dlg.pushButton.clicked.connect(Convert)

dlg.show()
app.exec()