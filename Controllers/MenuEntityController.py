from Views import MenuEntity, DialogWithOpenAccount, DialogWithOpenCredit, DialogWithOpenDeposit, DialogWithTrancsaction
from Models import MenuEntityModel


class MenuEntityController():
    def __init__(self, data):
        self.data = data
        self.view = MenuEntity.Ui_MenuEntity()
        self.view_open_account = DialogWithOpenAccount.Ui_OpenNewAccount()
        self.view_open_credit = DialogWithOpenCredit.Ui_OpenNewAccount()
        self.view_open_deposit = DialogWithOpenDeposit.Ui_OpenNewAccount()
        self.view_transactions = DialogWithTrancsaction.Ui_Dialog()

        self.model = MenuEntityModel.MenuEntityModel(self.view, self.data)

        self.press_buttons()

    def press_buttons(self):
        self.view.OpenAccount.clicked.connect(lambda: self.dialog_open_account())
        self.view.MakeCredit.clicked.connect(lambda: self.dialog_open_credit())
        self.view.MakeDeposit.clicked.connect(lambda: self.dialog_open_deposit())
        self.view.MoneyTransfer.clicked.connect(lambda: self.dialog_open_transaction())

#################################################################################################################

    def dialog_open_account(self):
        self.model.press_open_account_window(self.view_open_account)
        self.press_buttons_open_account()

    def press_buttons_open_account(self):
        self.view_open_account.confirm_buuton.clicked.connect(lambda: self.press_confirm_open_account())
        self.view_open_account.cancel_button.clicked.connect(lambda: self.press_cancel_dialog())

    def press_confirm_open_account(self):
        self.model.press_confirm_open_account_button(self.view_open_account.BankChoice.currentText(),
                                                         self.view_open_account.LineName.text())

#########################################################################################################

    def dialog_open_credit(self):
        self.model.press_open_credit_window(self.view_open_credit)
        self.press_buttons_open_credit()

    def press_buttons_open_credit(self):
        self.view_open_credit.confirm_buuton.clicked.connect(lambda: self.press_confirm_open_credit())
        self.view_open_credit.cancel_button.clicked.connect(lambda: self.press_cancel_dialog())
        self.view_open_credit.BankChoice.currentTextChanged.connect(lambda: self.change_bank_credit())
        self.view_open_credit.CreditSum.textChanged.connect(lambda: self.change_result_credit())

    def change_bank_credit(self):
        self.view_open_credit.set_credits_choice(self.view_open_credit.BankChoice.currentText())

    def change_result_credit(self):
        self.view_open_credit.set_result()

    def press_confirm_open_credit(self):
        try:
            self.model.press_confirm_open_credit(self.view_open_credit.BankChoice.currentText(),
                                                 self.view_open_credit.CreditChoice.currentText(),
                                                 int(self.view_open_credit.Result.text()))
        except:
            pass

#########################################################################################################

    def dialog_open_deposit(self):
        self.model.press_open_deposit_window(self.view_open_deposit)
        self.press_buttons_open_deposit()

    def press_buttons_open_deposit(self):
        self.view_open_deposit.confirm_buuton.clicked.connect(lambda: self.press_confirm_open_deposit())
        self.view_open_deposit.cancel_button.clicked.connect(lambda: self.press_cancel_dialog())
        self.view_open_deposit.BankChoice.currentTextChanged.connect(lambda: self.change_bank_deposit())
        self.view_open_deposit.DepositSum.textChanged.connect(lambda: self.change_result_deposit())

    def change_bank_deposit(self):
        self.view_open_deposit.set_deposits_choice(self.view_open_deposit.BankChoice.currentText())

    def change_result_deposit(self):
        self.view_open_deposit.set_result()

    def press_confirm_open_deposit(self):

            self.model.press_confirm_open_deposit(self.view_open_deposit.BankChoice.currentText(),
                                                  self.view_open_deposit.DepositChoice.currentText(),
                                                  int(self.view_open_deposit.Result.text()))

            pass

#########################################################################################################

    def dialog_open_transaction(self):
        self.model.press_open_transaction_window(self.view_transactions)
        self.press_transactions_buttons()

    def press_transactions_buttons(self):
        self.view_transactions.cancel_button.clicked.connect(lambda: self.press_cancel_dialog())
        self.view_transactions.confirm_button.clicked.connect(lambda: self.press_confirm_transaction())

    def press_confirm_transaction(self):
        try:
            if int(self.view_transactions.my_accounts.currentText().split(" | ")[1]) >= int(
                    self.view_transactions.sum.text()):
                name_acc = self.view_transactions.my_accounts.currentText().split(" | ")[0]
                self.model.press_confirm_transaction(name_acc,
                                                     self.view_transactions.to_client_account.text(),
                                                     int(self.view_transactions.sum.text())
                                                     )
            self.dialog_open_transaction()
        except:
            pass

#########################################################################################################
    def press_cancel_dialog(self):
        self.model.press_cancel_button()
