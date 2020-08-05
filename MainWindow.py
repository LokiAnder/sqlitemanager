# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1089, 848)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(240, 10, 821, 581))
        self.groupBox.setObjectName("groupBox")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setGeometry(QtCore.QRect(20, 20, 781, 551))
        self.tableView.setObjectName("tableView")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 221, 651))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listView = QtWidgets.QListView(self.groupBox_2)
        self.listView.setGeometry(QtCore.QRect(10, 30, 201, 611))
        self.listView.setObjectName("listView")
        self.open_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_file_btn.setGeometry(QtCore.QRect(10, 680, 171, 101))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.open_file_btn.setFont(font)
        self.open_file_btn.setObjectName("open_file_btn")
        self.select_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_btn.setEnabled(False)
        self.select_btn.setGeometry(QtCore.QRect(260, 600, 131, 61))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.select_btn.setFont(font)
        self.select_btn.setObjectName("select_btn")
        self.insert_btn = QtWidgets.QPushButton(self.centralwidget)
        self.insert_btn.setEnabled(False)
        self.insert_btn.setGeometry(QtCore.QRect(490, 600, 131, 61))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.insert_btn.setFont(font)
        self.insert_btn.setObjectName("insert_btn")
        self.update_btn = QtWidgets.QPushButton(self.centralwidget)
        self.update_btn.setEnabled(False)
        self.update_btn.setGeometry(QtCore.QRect(700, 600, 131, 61))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.update_btn.setFont(font)
        self.update_btn.setObjectName("update_btn")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setEnabled(False)
        self.delete_btn.setGeometry(QtCore.QRect(910, 600, 131, 61))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.delete_btn.setFont(font)
        self.delete_btn.setObjectName("delete_btn")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(190, 670, 871, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.command_input = QtWidgets.QPushButton(self.groupBox_3)
        self.command_input.setEnabled(False)
        self.command_input.setGeometry(QtCore.QRect(660, 20, 191, 81))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.command_input.setFont(font)
        self.command_input.setObjectName("command_input")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 641, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1089, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.actionclose)
        self.menu.addSeparator()
        self.menu.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.actionexit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据库管理工具"))
        self.groupBox.setTitle(_translate("MainWindow", "表格"))
        self.groupBox_2.setTitle(_translate("MainWindow", "表"))
        self.open_file_btn.setText(_translate("MainWindow", "打开文件夹"))
        self.select_btn.setText(_translate("MainWindow", "查询"))
        self.insert_btn.setText(_translate("MainWindow", "插入"))
        self.update_btn.setText(_translate("MainWindow", "修改"))
        self.delete_btn.setText(_translate("MainWindow", "删除"))
        self.groupBox_3.setTitle(_translate("MainWindow", "命令行操作"))
        self.command_input.setText(_translate("MainWindow", "输入"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
