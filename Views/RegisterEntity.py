# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterEntity.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterWindowEntity(object):
    def setupUi(self, RegisterWindowEntity):
        RegisterWindowEntity.setObjectName("RegisterWindowEntity")
        RegisterWindowEntity.resize(368, 379)
        self.centralwidget = QtWidgets.QWidget(RegisterWindowEntity)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, -1)
        self.verticalLayout_3.setSpacing(21)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.RegisterLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.RegisterLabel.setFont(font)
        self.RegisterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RegisterLabel.setObjectName("RegisterLabel")
        self.verticalLayout_3.addWidget(self.RegisterLabel)
        self.RegWindow = QtWidgets.QHBoxLayout()
        self.RegWindow.setObjectName("RegWindow")
        self.Labels = QtWidgets.QVBoxLayout()
        self.Labels.setSpacing(3)
        self.Labels.setObjectName("Labels")
        self.Type = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Type.setFont(font)
        self.Type.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Type.setObjectName("Type")
        self.Labels.addWidget(self.Type)
        self.Name = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Name.setFont(font)
        self.Name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Name.setObjectName("Name")
        self.Labels.addWidget(self.Name)
        self.Adress = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Adress.setFont(font)
        self.Adress.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Adress.setObjectName("Adress")
        self.Labels.addWidget(self.Adress)
        self.Email = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Email.setFont(font)
        self.Email.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Email.setObjectName("Email")
        self.Labels.addWidget(self.Email)
        self.PhoneNumber = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PhoneNumber.setFont(font)
        self.PhoneNumber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.PhoneNumber.setObjectName("PhoneNumber")
        self.Labels.addWidget(self.PhoneNumber)
        self.UNP = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.UNP.setFont(font)
        self.UNP.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.UNP.setObjectName("UNP")
        self.Labels.addWidget(self.UNP)
        self.Login = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Login.setFont(font)
        self.Login.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Login.setObjectName("Login")
        self.Labels.addWidget(self.Login)
        self.Password = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Password.setFont(font)
        self.Password.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Password.setObjectName("Password")
        self.Labels.addWidget(self.Password)
        self.RepeatPassword = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RepeatPassword.setFont(font)
        self.RepeatPassword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RepeatPassword.setObjectName("RepeatPassword")
        self.Labels.addWidget(self.RepeatPassword)
        self.RegWindow.addLayout(self.Labels)
        self.Lines = QtWidgets.QVBoxLayout()
        self.Lines.setSpacing(3)
        self.Lines.setObjectName("Lines")
        self.LineType = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LineType.setFont(font)
        self.LineType.setObjectName("LineType")
        self.Lines.addWidget(self.LineType)
        self.LineName = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LineName.setFont(font)
        self.LineName.setObjectName("LineName")
        self.Lines.addWidget(self.LineName)
        self.LineAdress = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LineAdress.setFont(font)
        self.LineAdress.setObjectName("LineAdress")
        self.Lines.addWidget(self.LineAdress)
        self.LineEmail = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LineEmail.setFont(font)
        self.LineEmail.setObjectName("LineEmail")
        self.Lines.addWidget(self.LineEmail)
        self.LinePhoneNumber = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LinePhoneNumber.setFont(font)
        self.LinePhoneNumber.setObjectName("LinePhoneNumber")
        self.Lines.addWidget(self.LinePhoneNumber)
        self.LineUNP = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LineUNP.setFont(font)
        self.LineUNP.setObjectName("LineUNP")
        self.Lines.addWidget(self.LineUNP)
        self.LineLogin = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LineLogin.setFont(font)
        self.LineLogin.setObjectName("LineLogin")
        self.Lines.addWidget(self.LineLogin)
        self.LinePassword = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LinePassword.setFont(font)
        self.LinePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LinePassword.setObjectName("LinePassword")
        self.Lines.addWidget(self.LinePassword)
        self.LineRepeatPassword = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.LineRepeatPassword.setFont(font)
        self.LineRepeatPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LineRepeatPassword.setObjectName("LineRepeatPassword")
        self.Lines.addWidget(self.LineRepeatPassword)
        self.RegWindow.addLayout(self.Lines)
        self.verticalLayout_3.addLayout(self.RegWindow)
        self.BottomButtons = QtWidgets.QHBoxLayout()
        self.BottomButtons.setContentsMargins(15, -1, 15, -1)
        self.BottomButtons.setSpacing(30)
        self.BottomButtons.setObjectName("BottomButtons")
        self.CanselButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.CanselButton.setFont(font)
        self.CanselButton.setObjectName("CanselButton")
        self.BottomButtons.addWidget(self.CanselButton)
        self.ConfirmButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ConfirmButton.setFont(font)
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.BottomButtons.addWidget(self.ConfirmButton)
        self.verticalLayout_3.addLayout(self.BottomButtons)
        RegisterWindowEntity.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegisterWindowEntity)
        QtCore.QMetaObject.connectSlotsByName(RegisterWindowEntity)

    def retranslateUi(self, RegisterWindowEntity):
        _translate = QtCore.QCoreApplication.translate
        RegisterWindowEntity.setWindowTitle(_translate("RegisterWindowEntity", "BelBank"))
        self.RegisterLabel.setText(_translate("RegisterWindowEntity", "Регистрация"))
        self.Type.setText(_translate("RegisterWindowEntity", "Тип предприятия"))
        self.Name.setText(_translate("RegisterWindowEntity", "Название предприятия"))
        self.Adress.setText(_translate("RegisterWindowEntity", "Юридический адрес"))
        self.Email.setText(_translate("RegisterWindowEntity", "Элетронная почта"))
        self.PhoneNumber.setText(_translate("RegisterWindowEntity", "Номер телефона"))
        self.UNP.setText(_translate("RegisterWindowEntity", "УНП"))
        self.Login.setText(_translate("RegisterWindowEntity", "Логин"))
        self.Password.setText(_translate("RegisterWindowEntity", "Пароль"))
        self.RepeatPassword.setText(_translate("RegisterWindowEntity", "Повторите пароль"))
        self.CanselButton.setText(_translate("RegisterWindowEntity", "Отмена"))
        self.ConfirmButton.setText(_translate("RegisterWindowEntity", "Потвердить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisterWindowEntity = QtWidgets.QMainWindow()
    ui = Ui_RegisterWindowEntity()
    ui.setupUi(RegisterWindowEntity)
    RegisterWindowEntity.show()
    sys.exit(app.exec_())
