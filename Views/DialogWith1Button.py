# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogWith1Button.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogWindow(object):
    def setupUi(self, DialogWindow, text):
        DialogWindow.setObjectName("DialogWindow")
        DialogWindow.resize(388, 210)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Text = QtWidgets.QLabel(DialogWindow)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.Text.setFont(font)
        self.Text.setAlignment(QtCore.Qt.AlignCenter)
        self.Text.setObjectName("Text")
        self.verticalLayout_3.addWidget(self.Text)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(100, -1, 100, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.OkButton = QtWidgets.QPushButton(DialogWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.OkButton.setFont(font)
        self.OkButton.setObjectName("OkButton")
        self.verticalLayout_2.addWidget(self.OkButton)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(DialogWindow, text)
        QtCore.QMetaObject.connectSlotsByName(DialogWindow)

    def retranslateUi(self, DialogWindow, text):
        _translate = QtCore.QCoreApplication.translate
        DialogWindow.setWindowTitle(_translate("DialogWindow", "BelBank"))
        self.Text.setText(_translate("DialogWindow", text))
        self.OkButton.setText(_translate("DialogWindow", "Продолжить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogWindow = QtWidgets.QDialog()
    ui = Ui_DialogWindow()
    ui.setupUi(DialogWindow)
    DialogWindow.show()
    sys.exit(app.exec_())
