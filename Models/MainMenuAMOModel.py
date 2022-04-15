from PyQt5 import QtWidgets
from Controllers import MenuAMOController

class MainMenuAMOModel():
    def __init__(self, obj):
        self.window = QtWidgets.QMainWindow()
        obj.setupUi(self.window)
        self.window.show()

    def press_enter_button(self, login, password):
        if login == "admin" and password == "admin":
            self.window = MenuAMOController.MenuAMOController(login)
        elif login == "manager" and password == "manager":
            self.window = MenuAMOController.MenuAMOController(login)
        elif login == "operator" and password == "operator":
            self.window = MenuAMOController.MenuAMOController(login)