from Views import MainMenuEntity, DialogWith1Button
from Models import MainMenuEntityModel

class MainMenuEntityController():
    def __init__(self):
        self.view = MainMenuEntity.Ui_MainMenuEntity()
        self.wrong_info_view = DialogWith1Button.Ui_DialogWindow()
        self.model = MainMenuEntityModel.MainMenuEntityModel(self.view)
        self.press_button()

    def press_button(self):
        self.view.RegisterButton.clicked.connect(lambda: self.model.press_register_button())
        self.view.EnterButton.clicked.connect(lambda: self.press_enter_button())

    def press_enter_button(self):
        self.model.press_enter_button(self.view.LoginLine.text(), self.view.PasswordLine.text(), self.wrong_info_view)
        try:
            self.press_wrong_info_button()
        except:
            pass

    def press_wrong_info_button(self):
        self.wrong_info_view.OkButton.clicked.connect(lambda: self.model.press_ok_button())