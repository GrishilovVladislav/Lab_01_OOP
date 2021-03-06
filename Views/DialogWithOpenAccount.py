# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogWithOpenAccount.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OpenNewAccount(object):
    def setupUi(self, OpenNewAccount, banks):
        OpenNewAccount.setObjectName("OpenNewAccount")
        OpenNewAccount.resize(450, 250)
        self.verticalLayout = QtWidgets.QVBoxLayout(OpenNewAccount)
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.text = QtWidgets.QLabel(OpenNewAccount)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.text.setFont(font)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.text.setObjectName("text")
        self.verticalLayout_3.addWidget(self.text)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(75, 10, 75, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.BankChoice = QtWidgets.QComboBox(OpenNewAccount)
        self.BankChoice.setEditable(False)
        self.BankChoice.setMaxCount(2147483637)
        self.BankChoice.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.BankChoice.setMinimumContentsLength(0)
        self.BankChoice.setObjectName("BankChoice")
        self.BankChoice.addItem("")
        self.BankChoice.addItem("")
        self.BankChoice.addItem("")
        self.verticalLayout_2.addWidget(self.BankChoice)
        self.LineName = QtWidgets.QLineEdit(OpenNewAccount)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LineName.setFont(font)
        self.LineName.setAlignment(QtCore.Qt.AlignCenter)
        self.LineName.setObjectName("LineName")
        self.verticalLayout_2.addWidget(self.LineName)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(30, 10, 30, -1)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_button = QtWidgets.QPushButton(OpenNewAccount)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.confirm_buuton = QtWidgets.QPushButton(OpenNewAccount)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.confirm_buuton.setFont(font)
        self.confirm_buuton.setObjectName("confirm_buuton")
        self.horizontalLayout.addWidget(self.confirm_buuton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(OpenNewAccount, banks)
        self.BankChoice.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OpenNewAccount)

    def retranslateUi(self, OpenNewAccount, banks):
        _translate = QtCore.QCoreApplication.translate
        OpenNewAccount.setWindowTitle(_translate("OpenNewAccount", "BelBank"))
        self.text.setText(_translate("OpenNewAccount", "???????????????? ??????????"))
        self.BankChoice.setCurrentText(_translate("OpenNewAccount", banks[0].name))
        for self.i in range(len(banks)):
            self.BankChoice.setItemText(self.i, _translate("OpenNewAccount", banks[self.i].name))
        self.LineName.setPlaceholderText(_translate("OpenNewAccount", "?????? ??????????"))
        self.cancel_button.setText(_translate("OpenNewAccount", "????????????"))
        self.confirm_buuton.setText(_translate("OpenNewAccount", "?????????????? ????????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OpenNewAccount = QtWidgets.QDialog()
    ui = Ui_OpenNewAccount()
    ui.setupUi(OpenNewAccount)
    OpenNewAccount.show()
    sys.exit(app.exec_())
