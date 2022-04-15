# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuUser.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuUser(object):
    def setupUi(self, MenuUser, user, user_accounts, banks):
        MenuUser.setObjectName("MenuUser")
        MenuUser.resize(824, 593)
        self.CentaralWidget = QtWidgets.QWidget(MenuUser)
        self.CentaralWidget.setObjectName("CentaralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.CentaralWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.TopTable = QtWidgets.QVBoxLayout()
        self.TopTable.setObjectName("TopTable")
        self.Top = QtWidgets.QHBoxLayout()
        self.Top.setObjectName("Top")
        self.Name = QtWidgets.QVBoxLayout()
        self.Name.setContentsMargins(10, 3, 10, 3)
        self.Name.setObjectName("Name")
        self.SecondName = QtWidgets.QLabel(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SecondName.setFont(font)
        self.SecondName.setObjectName("SecondName")
        self.Name.addWidget(self.SecondName)
        self.FirstName = QtWidgets.QLabel(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FirstName.setFont(font)
        self.FirstName.setObjectName("FirstName")
        self.Name.addWidget(self.FirstName)
        self.FarthersName = QtWidgets.QLabel(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FarthersName.setFont(font)
        self.FarthersName.setObjectName("FarthersName")
        self.Name.addWidget(self.FarthersName)
        self.Top.addLayout(self.Name)
        self.ACDOButtons = QtWidgets.QVBoxLayout()
        self.ACDOButtons.setSpacing(0)
        self.ACDOButtons.setObjectName("ACDOButtons")
        self.ACDButtons = QtWidgets.QHBoxLayout()
        self.ACDButtons.setSpacing(0)
        self.ACDButtons.setObjectName("ACDButtons")
        self.Credits = QtWidgets.QPushButton(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(31)
        self.Credits.setFont(font)
        self.Credits.setObjectName("Credits")
        self.ACDButtons.addWidget(self.Credits)
        self.Accounts = QtWidgets.QPushButton(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(31)
        self.Accounts.setFont(font)
        self.Accounts.setObjectName("Accounts")
        self.ACDButtons.addWidget(self.Accounts)
        self.Deposits = QtWidgets.QPushButton(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(31)
        self.Deposits.setFont(font)
        self.Deposits.setObjectName("Deposits")
        self.ACDButtons.addWidget(self.Deposits)
        self.ACDOButtons.addLayout(self.ACDButtons)
        self.Operations = QtWidgets.QPushButton(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.Operations.setFont(font)
        self.Operations.setObjectName("Operations")
        self.ACDOButtons.addWidget(self.Operations)
        self.Top.addLayout(self.ACDOButtons)
        self.TopTable.addLayout(self.Top)
        self.Table = QtWidgets.QTableWidget(self.CentaralWidget)
        self.Table.setFrameShape(QtWidgets.QFrame.Box)
        self.Table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Table.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Table.setShowGrid(True)
        self.Table.setRowCount(len(user_accounts))
        self.Table.setColumnCount(5)
        self.Table.setObjectName("Table")
        for i in range(len(user_accounts)):
            item = QtWidgets.QTableWidgetItem()
            self.Table.setVerticalHeaderItem(i, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Table.setHorizontalHeaderItem(4, item)
        for i in range(len(user_accounts)):
            for j in range(5):
                item = QtWidgets.QTableWidgetItem()
                self.Table.setItem(i, j, item)
        self.Table.horizontalHeader().setCascadingSectionResizes(True)
        self.Table.horizontalHeader().setDefaultSectionSize(160)
        self.Table.horizontalHeader().setSortIndicatorShown(False)
        self.Table.verticalHeader().setVisible(False)
        self.TopTable.addWidget(self.Table)
        self.verticalLayout_2.addLayout(self.TopTable)
        self.BottomButtons = QtWidgets.QHBoxLayout()
        self.BottomButtons.setObjectName("BottomButtons")
        self.OpenAccount = QtWidgets.QPushButton(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.OpenAccount.setFont(font)
        self.OpenAccount.setObjectName("OpenAccount")
        self.BottomButtons.addWidget(self.OpenAccount)
        self.MoneyTransfer = QtWidgets.QPushButton(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MoneyTransfer.setFont(font)
        self.MoneyTransfer.setObjectName("MoneyTransfer")
        self.BottomButtons.addWidget(self.MoneyTransfer)
        self.Freeze = QtWidgets.QPushButton(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Freeze.setFont(font)
        self.Freeze.setObjectName("Freeze")
        self.BottomButtons.addWidget(self.Freeze)
        self.MakeCredit = QtWidgets.QPushButton(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MakeCredit.setFont(font)
        self.MakeCredit.setObjectName("MakeCredit")
        self.BottomButtons.addWidget(self.MakeCredit)
        self.MakeDeposit = QtWidgets.QPushButton(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.MakeDeposit.setFont(font)
        self.MakeDeposit.setObjectName("MakeDeposit")
        self.BottomButtons.addWidget(self.MakeDeposit)
        self.CloseAccount = QtWidgets.QPushButton(self.CentaralWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.CloseAccount.setFont(font)
        self.CloseAccount.setObjectName("CloseAccount")
        self.BottomButtons.addWidget(self.CloseAccount)
        self.verticalLayout_2.addLayout(self.BottomButtons)
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

        self.retranslateUi(MenuUser, user, user_accounts, banks)
        QtCore.QMetaObject.connectSlotsByName(MenuUser)

    def retranslateUi(self, MenuUser, user, user_accounts, banks):
        _translate = QtCore.QCoreApplication.translate
        MenuUser.setWindowTitle(_translate("MenuUser", "BelBank"))
        self.SecondName.setText(_translate("MenuUser", user.name.split()[0]))
        self.FirstName.setText(_translate("MenuUser", user.name.split()[1]))
        self.FarthersName.setText(_translate("MenuUser", user.name.split()[2]))
        self.Credits.setText(_translate("MenuUser", "Кредиты"))
        self.Accounts.setText(_translate("MenuUser", "Счета"))
        self.Deposits.setText(_translate("MenuUser", "Депозиты"))
        self.Operations.setText(_translate("MenuUser", "Операции"))
        for i in range(len(user_accounts)):
            item = self.Table.verticalHeaderItem(i)
            item.setText(_translate("MenuUser", f"{i}"))
        item = self.Table.horizontalHeaderItem(0)
        item.setText(_translate("MenuUser", "Банк"))
        item = self.Table.horizontalHeaderItem(1)
        item.setText(_translate("MenuUser", "Имя счета"))
        item = self.Table.horizontalHeaderItem(2)
        item.setText(_translate("MenuUser", "Номер счета"))
        item = self.Table.horizontalHeaderItem(3)
        item.setText(_translate("MenuUser", "Количество средств"))
        item = self.Table.horizontalHeaderItem(4)
        item.setText(_translate("MenuUser", "Состояние счета"))
        __sortingEnabled = self.Table.isSortingEnabled()
        self.Table.setSortingEnabled(False)
        for i in range(len(user_accounts)):
            item = self.Table.item(i, 0)
            item.setText(_translate("MenuUser", f"{banks[user_accounts[i].bank_id].name}"))
            item = self.Table.item(i, 1)
            item.setText(_translate("MenuUser", f"{user_accounts[i].name}"))
            item = self.Table.item(i, 2)
            item.setText(_translate("MenuUser", f"{user_accounts[i].number}"))
            item = self.Table.item(i, 3)
            item.setText(_translate("MenuUser", f"{user_accounts[i].money}"))
            item = self.Table.item(i, 4)
            item.setText(_translate("MenuUser", f"{user_accounts[i].type}"))
        self.Table.setSortingEnabled(__sortingEnabled)
        self.OpenAccount.setText(_translate("MenuUser", "Открыть новый счет"))
        self.MoneyTransfer.setText(_translate("MenuUser", "Перевод средств"))
        self.Freeze.setText(_translate("MenuUser", "Заморозка счета"))
        self.MakeCredit.setText(_translate("MenuUser", "Оформить кредит"))
        self.MakeDeposit.setText(_translate("MenuUser", "Оформить депозит"))
        self.CloseAccount.setText(_translate("MenuUser", "Закрыть счет"))
        self.menu.setTitle(_translate("MenuUser", "Меню"))
        self.SystemExit.setText(_translate("MenuUser", "Выйти из системы"))
        self.AccountExit.setText(_translate("MenuUser", "Выйти из аккаунта"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuUser = QtWidgets.QMainWindow()
    ui = Ui_MenuUser()
    ui.setupUi(MenuUser)
    MenuUser.show()
    sys.exit(app.exec_())