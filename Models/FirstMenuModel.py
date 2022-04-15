from PyQt5 import QtWidgets
from Controllers import MainMenuUserController, MainMenuEntityController, MainMenuAMOController

class FirstMenuModel():
    def __init__(self, obj):
        self.window = QtWidgets.QMainWindow()
        obj.setupUi(self.window)
        self.window.show()

    def press_user_button(self):
        self.window = MainMenuUserController.MainMenuUserController()

    def press_entity_button(self):
        self.window = MainMenuEntityController.MainMenuEntityController()

    def press_AMO_button(self):
        self.window = MainMenuAMOController.MainMenuAMOController()

