import sys
from PyQt4 import QtCore, QtGui

from ui_table_dialog import Ui_TableDialog

class ControlPointDetailsDialog(QtGui.QDialog, Ui_TableDialog):

    def __init__(self, ctrlDict):
        super(ControlPointDetailsDialog, self).__init__()
        
        self.setupUi(self)
        
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["System", "Rating"])
        
        self.updateTable(ctrlDict)
        
        self.setWindowTitle(QtGui.QApplication.translate("ControlPointDialog", "Control Points", None, QtGui.QApplication.UnicodeUTF8))

    def updateTable(self, cntrlDict):
        self.tableWidget.setRowCount(len(cntrlDict))
        
        line=0
        for key in cntrlDict:
            item = QtGui.QTableWidgetItem()
            item.setText(QtGui.QApplication.translate("ControlPointDialog", key, None, QtGui.QApplication.UnicodeUTF8))
            self.tableWidget.setItem(line,0,item)
            item1 = QtGui.QTableWidgetItem()
            item1.setText(QtGui.QApplication.translate("ControlPointDialog", "%0.2f" % cntrlDict[key], None, QtGui.QApplication.UnicodeUTF8))
            self.tableWidget.setItem(line,1,item1)
            line += 1
