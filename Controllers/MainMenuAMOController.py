from Views import MainMenuAMO
from Models import MainMenuAMOModel

class MainMenuAMOController():
    def __init__(self):
        self.view = MainMenuAMO.Ui_MainMenuAMO()
        self.model = MainMenuAMOModel.MainMenuAMOModel(self.view)
        self.press_button()

    def press_button(self):
        self.view.EnterButton.clicked.connect(lambda: self.press_enter_button())

    def press_enter_button(self):
        self.model.press_enter_button(self.view.LoginLine.text(), self.view.PasswordLine.text())



