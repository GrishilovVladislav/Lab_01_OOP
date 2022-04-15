from PyQt5 import QtWidgets
from DataBases import DataBase
from Controllers import MainMenuUserController
from Entities import Entities, Actions


class RegisterUserModel():
    def __init__(self, obj):
        self.window = QtWidgets.QMainWindow()
        obj.setupUi(self.window)
        self.window.show()

    def press_cancel_button(self):
        self.window = MainMenuUserController.MainMenuUserController()

    def press_confirm_button(self, user_data):
        self.user = Entities.User(user_data)
        self.register_request = Actions.RegisterRequest(f"{self.user.name} {self.user.phone_number} {self.user.passport_seria}{self.user.passport_number} {self.user.login}")
        self.wb = DataBase.WorkWithDB()
        self.wb.add_request(self.register_request)
        self.wb.add_user(self.user)
        self.window = MainMenuUserController.MainMenuUserController()

    def create_new_account(self, user_data):
        self.user = Entities.User(user_data)
        self.wb = DataBase.WorkWithDB()
        self.wb.add_user(self.user)
