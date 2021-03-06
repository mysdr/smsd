import sys
from PyQt4 import QtCore, QtGui, uic

class PowerDetailsDialog(QtGui.QDialog):

    def __init__(self, pwrDict):
        super(PowerDetailsDialog, self).__init__()

        # import ui from Qt file
        uic.loadUi('table_dialog.ui', self)

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["System", "Rating"])
        
        self.updateTable(pwrDict)
        
        self.setWindowTitle(QtGui.QApplication.translate("PowerDialog", "Power Usage", None, QtGui.QApplication.UnicodeUTF8))

    def updateTable(self,  pwrDict):
        self.tableWidget.setRowCount(len(pwrDict))
        
        line=0
        for key in pwrDict:
            item = QtGui.QTableWidgetItem()
            item.setText(QtGui.QApplication.translate("PowerDialog", key, None, QtGui.QApplication.UnicodeUTF8))
            self.tableWidget.setItem(line,0,item)
            item1 = QtGui.QTableWidgetItem()
            item1.setText(QtGui.QApplication.translate("PowerDialog", "%0.2f" % pwrDict[key], None, QtGui.QApplication.UnicodeUTF8))
            self.tableWidget.setItem(line,1,item1)
            line += 1

