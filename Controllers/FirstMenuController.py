from Views import FirstMenu
from Models import FirstMenuModel


class FirstMenuController():
    def __init__(self):
        self.view = FirstMenu.Ui_FirstMenu()
        self.model = FirstMenuModel.FirstMenuModel(self.view)
        self.press_button()

    def press_button(self):
        self.view.User.clicked.connect(lambda: self.model.press_user_button())
        self.view.Entity.clicked.connect(lambda: self.model.press_entity_button())
        self.view.AMO.clicked.connect(lambda: self.model.press_AMO_button())



