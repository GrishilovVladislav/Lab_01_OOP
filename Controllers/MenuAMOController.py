from Views import MenuAdmin, MenuManager, MenuOperator, DialogRequests
from Models import MenuAMOModel

class MenuAMOController():
    def __init__(self, A_M_O):
        if A_M_O == "admin":
            self.view_admin = MenuAdmin.Ui_MenuAdmin("Администратор")
        if A_M_O == "manager":
            self.view_admin = MenuAdmin.Ui_MenuAdmin("Менеджер")
        if A_M_O == "operator":
            self.view_admin = MenuAdmin.Ui_MenuAdmin("Оператор")

        self.view_manager = MenuManager.Ui_MenuManager()
        self.view_operator = MenuOperator.Ui_MenuOperator()
        self.view_requests = DialogRequests.Ui_Dialog()

        self.model = MenuAMOModel.MenuAMOModel(self.view_admin)
        self.press_button()

    def press_button(self):
        self.view_admin.requests.clicked.connect(lambda: self.press_requests_button())

    def press_requests_button(self):
        self.model.requests_button(self.view_requests)
        self.press_button_requests()

####################################################################################################

    def press_button_requests(self):
        self.view_requests.exit_button.clicked.connect(lambda: self.press_exit_requests())
        self.view_requests.approve.clicked.connect(lambda: self.press_approve_requests())

    def press_exit_requests(self):
        self.model.exit_button()

    def press_approve_requests(self):
        self.model.approve_button(self.view_requests.req_choice.currentText())
        self.press_requests_button()