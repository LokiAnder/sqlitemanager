# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ControlDialog(object):
    def setupUi(self, ControlDialog):
        ControlDialog.setObjectName("ControlDialog")
        ControlDialog.resize(783, 143)
        self.comboBox = QtWidgets.QComboBox(ControlDialog)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 161, 51))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(ControlDialog)
        self.lineEdit.setGeometry(QtCore.QRect(540, 30, 231, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(ControlDialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 751, 41))
        self.pushButton.setObjectName("pushButton")
        self.rule = QtWidgets.QComboBox(ControlDialog)
        self.rule.setGeometry(QtCore.QRect(390, 30, 131, 51))
        self.rule.setObjectName("rule")
        self.rule.addItem("")
        self.rule.addItem("")
        self.target = QtWidgets.QLineEdit(ControlDialog)
        self.target.setGeometry(QtCore.QRect(190, 30, 191, 51))
        self.target.setObjectName("target")
        self.label = QtWidgets.QLabel(ControlDialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ControlDialog)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 72, 15))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ControlDialog)
        self.label_3.setGeometry(QtCore.QRect(390, 10, 72, 15))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ControlDialog)
        self.label_4.setGeometry(QtCore.QRect(540, 10, 72, 15))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(ControlDialog)
        QtCore.QMetaObject.connectSlotsByName(ControlDialog)

    def retranslateUi(self, ControlDialog):
        _translate = QtCore.QCoreApplication.translate
        ControlDialog.setWindowTitle(_translate("ControlDialog", "窗口"))
        self.pushButton.setText(_translate("ControlDialog", "none"))
        self.rule.setItemText(0, _translate("ControlDialog", "包含"))
        self.rule.setItemText(1, _translate("ControlDialog", "等于"))
        self.label.setText(_translate("ControlDialog", "表"))
        self.label_2.setText(_translate("ControlDialog", "列"))
        self.label_3.setText(_translate("ControlDialog", "规则"))
        self.label_4.setText(_translate("ControlDialog", "值"))