from PyQt5 import QtWidgets
from Controllers import RegisterEntityController, MenuEntityController
from DataBases import DataBase

class MainMenuEntityModel():
    def __init__(self, obj):
        self.window = QtWidgets.QMainWindow()
        obj.setupUi(self.window)
        self.window.show()

    def press_register_button(self):
        self.window = RegisterEntityController.RegisterEntityController()

    def press_enter_button(self, login, password, error_window):
        self.wb = DataBase.WorkWithDB()
        if self.wb.get_entity_enter_data(login) != None:
            self.entity = self.wb.get_entity_enter_data(login)
            self.password = self.entity.password
            if self.password == password:
                self.window = MenuEntityController.MenuEntityController(self.entity)
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