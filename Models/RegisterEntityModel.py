from PyQt5 import QtWidgets
from DataBases import DataBase
from Controllers import MainMenuEntityController
from Entities import Entities, Actions

class RegisterEntityModel():
    def __init__(self, obj):
        self.data_base = DataBase.WorkWithDB()
        self.window = QtWidgets.QMainWindow()
        obj.setupUi(self.window)
        self.window.show()

    def cancel_button(self):
        self.window = MainMenuEntityController.MainMenuEntityController()

    def confirm_button(self, data):
        self.entity = Entities.Entity(data)
        self.request = Actions.EntityRegisterRequest(f"{self.entity.type} {self.entity.name} {self.entity.login}")
        self.data_base.add_request(self.request)
        self.data_base.add_entity(self.entity)
        self.window = MainMenuEntityController.MainMenuEntityController()
