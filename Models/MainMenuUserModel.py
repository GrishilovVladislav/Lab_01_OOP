from PyQt5 import QtWidgets
from Controllers import RegisterUserController, MenuUserController
from DataBases import DataBase

class MainMenuModelUser():
    def __init__(self, obj):
        self.window = QtWidgets.QMainWindow()
        obj.setupUi(self.window)
        self.window.show()

    def press_register_button(self):
        self.window = RegisterUserController.RegisterUserController()

    def press_enter_button(self, login, password, error_window):
        self.wb = DataBase.WorkWithDB()
        if self.wb.get_user_enter_data(login) != None:
            self.user = self.wb.get_user_enter_data(login)
            if self.user.approved == 0:
                self.error_window = QtWidgets.QDialog()
                error_window.setupUi(self.error_window, "Ваша заявка\nещё на рассмотрении")
                self.error_window.show()
                return None
            self.password = self.user.password
            if self.password == password:
                self.window = MenuUserController.MenuUserController(self.user)
            else:
                self.error_window = QtWidgets.QDialog()
                error_window.setupUi(self.error_window, "Неверный пароль")
                self.error_window.show()
        else:
            self.error_window = QtWidgets.QDialog()
            error_window.setupUi(self.error_window, "Неверный логин")
            self.error_window.show()

    def press_ok_button(self):
        self.error_window.close()
