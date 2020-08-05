import sys
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox, QFileDialog, QDialog, QPushButton, QTableView, QComboBox, QTableWidgetItem
from PyQt5.QtCore import QAbstractTableModel, Qt
from MainWindow import *
from select import *
from ResultDialog import *
from SqliteMethods import SqliteMethods as sm

def ShowDatas(datas):
    dlg = QDialog()
    dlg.resize(800, 600)
    table1 = QTableView(dlg)
    table1.resize(800, 600)
    model = PandasModel(datas)
    table1.setModel(model)
    dlg.setWindowTitle("查询结果")
    dlg.setWindowModality(Qt.ApplicationModal)
    dlg.exec_()

class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        self.open_file_btn.clicked.connect(self.OpenFileEvent)
        self.listView.clicked.connect(self.ChangeTable)
        self.command_input.clicked.connect(self.SendCommand)
        self.select_btn.clicked.connect(self.SelectEvent)
        self.delete_btn.clicked.connect(self.DeleteEvent)
        self.insert_btn.clicked.connect(self.InsertEvent)


    def OpenFoldEvent(self):
        self.fold_path = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "./")

    def OpenFileEvent(self):
        self.file_path, file_type = QFileDialog.getOpenFileName(self,
                                                'Open file',
                                                './',
                                                "数据库 (*.db *.sqlite3)"
                                                )
        self.ReadDatabase(self.file_path)
        self.EnableBtns()

    def EnableBtns(self):
        self.select_btn.setEnabled(1)
        self.delete_btn.setEnabled(1)
        self.update_btn.setEnabled(1)
        self.insert_btn.setEnabled(1)
        self.command_input.setEnabled(1)

# 将数据库内的数据读取
    def ReadDatabase(self,file_path):
        self.db = sm(file_path)
        table_list = self.db.ReadTableList()
        self.table_list = table_list["name"]
        datas = []
        for i in table_list["name"]:
            datas.append(self.db.SelectWholeTable(i))
        self.dataset = datas
        data = self.db.SelectWholeTable(table_list["name"][0])
        model = PandasModel(data)
        self.tableView.setModel(model)
        self.UpdateTableList(table_list)


    def UpdataTableview(self,table_name):
        data = self.db.SelectWholeTable(table_name)
        model = PandasModel(data)
        self.tableView.setModel(model)


# 将数据库内多个表名更新到表列表中
    def UpdateTableList(self,table_list):
        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in table_list["name"]:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

    def ChangeTable(self,index):
        selected_table = index.data()
        self.current_table = selected_table
        self.UpdataTableview(selected_table)
#TODO 多标签显示

#TODO 接入表格操作函数
    def SendCommand(self):
        command = self.lineEdit.text()
        result = self.db.SqlConsole(command)
        for row in result:
            print(row)

    def SelectEvent(self):
        dlg = ControlDialog(self.file_path,0)
        dlg.comboBox.addItems(self.table_list)
        dlg.pushButton.setText("查询")
        #dlg.pushButton.clicked.connect(dlg.Input(self.file_path))
        dlg.exec_()

    def DeleteEvent(self):
        dlg = ControlDialog(self.file_path,1)
        dlg.comboBox.addItems(self.table_list)
        dlg.pushButton.setText("删除")
        dlg.exec_()

    def InsertEvent(self):
        current_table = self.current_table
        dlg = ResultDialog()
        dlg.set_db_path(self.file_path)
        dlg.set_table_name(current_table)
        dlg.set_db(self.db)
        data_columns = self.db.ColumnsList(current_table)
        columns_len = len(data_columns)
        data = np.zeros((1,columns_len))
        datas = pd.DataFrame(data)
        dlg.tableWidget.setRowCount(1)
        dlg.tableWidget.setColumnCount(columns_len)
        for i in range(columns_len):
            dlg.tableWidget.setItem(0,i,QTableWidgetItem("0"))
        dlg.tableWidget.setHorizontalHeaderLabels(data_columns)
        dlg.exec_()




    def ControlResult(self,data):
        dlg = QDialog()
        dlg.resize(800,600)
        table1 = QTableView(dlg)
        table1.resize(800,600)
        model = PandasModel(data)
        table1.setModel(model)
        dlg.setWindowTitle("查询结果")
        dlg.setWindowModality(Qt.ApplicationModal)
        dlg.exec_()



#表格显示
class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]))
        return QtCore.QVariant()

class ControlDialog(QDialog,Ui_ControlDialog):
    def __init__(self, path, mode, parent=None):
        super(ControlDialog, self).__init__(parent)
        self.setupUi(self)
        self.path = path
        self.mode = mode
        self.pushButton.clicked.connect(self.EventManager)


# 两种弹窗（select、delete）,及分配任务的eventmanager
    def EventManager(self):
        if self.mode == 0:
            self.Select()
        elif self.mode == 1:
            self.Delete()

    def Select(self):
        db = sm(self.path)
        selected_table = self.comboBox.currentText()
        column = self.target.text()
        object = self.lineEdit.text()
        rule = self.rule.currentIndex()
        if rule == 0:
            set_rule = "select * from {} where FIND_IN_SET('{}',{})".format(selected_table, object, column)
        else:
            set_rule = "select * from {} where {}={}".format(selected_table, column, object)
        datas = db.SelectInColumns(selected_table,column,object)
        dlg = ResultDialog()
        dlg.PrintResult(datas)
        dlg.exec_()

    def Delete(self):
        db = sm(self.path)
        selected_table = self.comboBox.currentText()
        column = self.target.text()
        object = self.lineEdit.text()
        rule = self.rule.currentIndex()
        if rule == 0:
            set_rule = "{} LIKE '%{}%'".format(column, object)
        else:
            set_rule = "{}={} ".format(object, column)
        datas = db.DeleteRowByRule(selected_table, set_rule)
        msg = QMessageBox()
        msg.setText("Delete Successfully")
        msg.exec_()


#TODO 当发生删除、插入、更新事件时，将被更新的内容显示在弹窗中
# 简单表型弹窗
class ResultDialog(QDialog,Ui_ResultDialog):
    def __init__(self, parent=None):
        super(ResultDialog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.InsertEvent)

    def PrintResult(self,datas):
        model = PandasModel(datas)
        self.tableView.setModel(model)

    def set_table_name(self, table_name):
        self.table_name = table_name

    def set_db_path(self,path):
        self.db_path = path

    def set_db(self,db):
        self.db = db

    def InsertEvent(self):
        print("")
        #data = self.db.SelectWholeTable(self.table_name)
        columns_list = self.db.ColumnsList(self.table_name)
        columns_len = len(columns_list)
        data = list(range(columns_len))
        for i in range(columns_len):
            item_data = self.tableWidget.item(0,i).text()
            data[i] = item_data
        datas_ruled = str(data)[1:-1]
        #self.db.InsertRowByRule(self.table_name,datas_ruled)
        #db = sm(self.path)
        #data = self.tableWidget.currentItem().text()
        #data = db.SelectWholeTable(self.table_name)
        print(datas_ruled)
        #print(data)
        #db.cursor.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())