from Views import RegisterEntity
from Models import RegisterEntityModel

class RegisterEntityController():
    def __init__(self):
        self.view = RegisterEntity.Ui_RegisterWindowEntity()
        self.model = RegisterEntityModel.RegisterEntityModel(self.view)
        self.press_button()

    def press_button(self):
        self.view.CanselButton.clicked.connect(lambda: self.press_cancel_button())
        self.view.ConfirmButton.clicked.connect(lambda: self.press_confirm_button())

    def press_cancel_button(self):
        self.model.cancel_button()

    def press_confirm_button(self):
        if self.view.LinePassword.text() == self.view.LineRepeatPassword.text():
            data = (0,
                    self.view.LineType.text(),
                    self.view.LineName.text(),
                    self.view.LineAdress.text(),
                    self.view.LineUNP.text(),
                    self.view.LineLogin.text(),
                    self.view.LinePassword.text(),
                    0)
            self.model.confirm_button(data)