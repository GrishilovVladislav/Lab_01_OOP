from Views import RegisterUser
from Models import RegisterUserModel

class RegisterUserController():
    def __init__(self):
        self.view = RegisterUser.Ui_RegisterWindowUser()
        self.model = RegisterUserModel.RegisterUserModel(self.view)
        self.press_button()

    def press_button(self):
        self.view.CanselButton.clicked.connect(lambda: self.model.press_cancel_button())
        self.view.ConfirmButton.clicked.connect(lambda: self.if_good_input())

    def if_good_input(self):
        if (self.view.LineFirstName.text().isalpha() and
            self.view.LineSecondName.text().isalpha() and
            self.view.LineFathersName.text().isalpha() and
            self.view.LinePassportSeria.text().isalpha() and
            self.view.LinePassportNumber.text().isdigit() and
            self.view.LinePassword.text() == self.view.LineRepeatPassword.text()
        ):
            self.user_data = (0,
                              self.view.LineFirstName.text() + " " + self.view.LineSecondName.text() + " " + self.view.LineFathersName.text(),
                              self.view.LinePassportSeria.text(),
                              self.view.LinePassportNumber.text(),
                              self.view.LineIdentificationNumber.text(),
                              self.view.LinePhoneNumber.text(),
                              self.view.LineEmail.text(),
                              self.view.LineLogin.text(),
                              self.view.LinePassword.text(),
                              0
                              )
            self.model.press_confirm_button(self.user_data)
        else:
            print("Error")
            return 0
