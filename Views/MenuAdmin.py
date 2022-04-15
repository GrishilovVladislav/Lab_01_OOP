# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuAdmin(object):
    def __init__(self, A_M_O):
        self.A_M_O = A_M_O

    def setupUi(self, MenuUser, logs):
        MenuUser.setObjectName("MenuUser")
        MenuUser.resize(824, 593)
        self.CentaralWidget = QtWidgets.QWidget(MenuUser)
        self.CentaralWidget.setObjectName("CentaralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.CentaralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.admin = QtWidgets.QLabel(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.admin.setFont(font)
        self.admin.setAlignment(QtCore.Qt.AlignCenter)
        self.admin.setObjectName("admin")
        self.horizontalLayout_2.addWidget(self.admin)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.requests = QtWidgets.QPushButton(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.requests.setFont(font)
        self.requests.setObjectName("requests")
        self.horizontalLayout.addWidget(self.requests)
        self.cancel_operations = QtWidgets.QPushButton(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cancel_operations.setFont(font)
        self.cancel_operations.setObjectName("cancel_operations")
        self.horizontalLayout.addWidget(self.cancel_operations)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.Table = QtWidgets.QTableWidget(self.CentaralWidget)
        self.Table.setFrameShape(QtWidgets.QFrame.Box)
        self.Table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Table.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Table.setShowGrid(True)
        self.Table.setRowCount(len(logs))
        self.Table.setColumnCount(2)
        self.Table.setObjectName("Table")
        for i in range(len(logs)):
            item = QtWidgets.QTableWidgetItem()
            self.Table.setVerticalHeaderItem(i, item)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.Table.setHorizontalHeaderItem(1, item)
        for i in range(len(logs)):
            for j in range(2):
                item = QtWidgets.QTableWidgetItem()
                self.Table.setItem(i, j, item)
        self.Table.horizontalHeader().setCascadingSectionResizes(True)
        self.Table.horizontalHeader().setDefaultSectionSize(401)
        self.Table.horizontalHeader().setSortIndicatorShown(False)
        self.Table.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.Table)
        MenuUser.setCentralWidget(self.CentaralWidget)
        self.MenuBar = QtWidgets.QMenuBar(MenuUser)
        self.MenuBar.setGeometry(QtCore.QRect(0, 0, 824, 22))
        self.MenuBar.setObjectName("MenuBar")
        self.menu = QtWidgets.QMenu(self.MenuBar)
        self.menu.setObjectName("menu")
        MenuUser.setMenuBar(self.MenuBar)
        self.SystemExit = QtWidgets.QAction(MenuUser)
        self.SystemExit.setObjectName("SystemExit")
        self.AccountExit = QtWidgets.QAction(MenuUser)
        self.AccountExit.setObjectName("AccountExit")
        self.menu.addAction(self.AccountExit)
        self.menu.addAction(self.SystemExit)
        self.MenuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MenuUser, logs)
        QtCore.QMetaObject.connectSlotsByName(MenuUser)

    def retranslateUi(self, MenuUser, logs):
        _translate = QtCore.QCoreApplication.translate
        MenuUser.setWindowTitle(_translate("MenuUser", "BelBank"))
        self.admin.setText(_translate("MenuUser", self.A_M_O))
        self.requests.setText(_translate("MenuUser", "Запросы"))
        self.cancel_operations.setText(_translate("MenuUser", "Отмена операций"))
        for i in range(len(logs)):
            item = self.Table.verticalHeaderItem(i)
            item.setText(_translate("MenuUser", f"{i+1}"))
        item.setText(_translate("MenuUser", "Время"))
        item = self.Table.horizontalHeaderItem(1)
        item.setText(_translate("MenuUser", "Информация"))
        __sortingEnabled = self.Table.isSortingEnabled()
        self.Table.setSortingEnabled(False)
        for i in range(len(logs)):
                item = self.Table.item(i, 0)
                item.setText(_translate("MenuUser", f"{logs[i].time}"))
                item = self.Table.item(i, 1)
                item.setText(_translate("MenuUser", f"{logs[i].info}"))
        self.Table.setSortingEnabled(__sortingEnabled)
        self.menu.setTitle(_translate("MenuUser", "Меню"))
        self.SystemExit.setText(_translate("MenuUser", "Выйти из системы"))
        self.AccountExit.setText(_translate("MenuUser", "Выйти из аккаунта"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuUser = QtWidgets.QMainWindow()
    ui = Ui_MenuAdmin()
    ui.setupUi(MenuUser)
    MenuUser.show()
    sys.exit(app.exec_())
