# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AddJob.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(432, 403)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(70, 350, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 121, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.jobTitleBox = QtGui.QLineEdit(Dialog)
        self.jobTitleBox.setGeometry(QtCore.QRect(60, 40, 351, 31))
        self.jobTitleBox.setObjectName(_fromUtf8("jobTitleBox"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 121, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.IndustryBox = QtGui.QLineEdit(Dialog)
        self.IndustryBox.setGeometry(QtCore.QRect(60, 100, 351, 31))
        self.IndustryBox.setObjectName(_fromUtf8("IndustryBox"))
        self.LevelBox = QtGui.QLineEdit(Dialog)
        self.LevelBox.setGeometry(QtCore.QRect(60, 160, 351, 31))
        self.LevelBox.setObjectName(_fromUtf8("LevelBox"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 121, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(160, 270, 61, 27))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 131, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 310, 71, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.SalaryBox = QtGui.QLineEdit(Dialog)
        self.SalaryBox.setGeometry(QtCore.QRect(60, 220, 351, 31))
        self.SalaryBox.setObjectName(_fromUtf8("SalaryBox"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 200, 121, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setGeometry(QtCore.QRect(103, 310, 191, 31))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add Job", None))
        self.label.setText(_translate("Dialog", "JobTitle", None))
        self.label_2.setText(_translate("Dialog", "Industry", None))
        self.label_3.setText(_translate("Dialog", "Level", None))
        self.label_4.setText(_translate("Dialog", "Age requirement", None))
        self.label_5.setText(_translate("Dialog", "Deadline", None))
        self.label_6.setText(_translate("Dialog", "Salary", None))

