from PyQt5 import QtWidgets
from DataBases import DataBase
from Entities import Entities, Actions
from Controllers import MenuEntityController


class MenuEntityModel():
    def __init__(self, obj, entity):
        self.data_base = DataBase.WorkWithDB()
        self.entity = entity
        self.entity_id = entity.id
        self.entity_accounts = self.data_base.get_accounts_data_by_client_id(self.entity.id)
        self.bank_list = self.data_base.get_bank_list()

        self.window = QtWidgets.QMainWindow()
        obj.setupUi(self.window, self.entity, self.entity_accounts, self.bank_list)
        self.window.show()
        self.bank_list = self.data_base.get_bank_list()

#######################################################################################################################

    def press_open_account_window(self, obj):
        self.window = QtWidgets.QDialog()
        obj.setupUi(self.window, self.bank_list)
        self.window.show()

    def press_confirm_open_account_button(self, bank, name):
        data = (0,
                self.entity.id,
                self.data_base.get_bank_info_by_name(bank).id,
                0,
                "",
                0,
                name,
                0)
        self.new_account = Entities.BankAccount(data)
        self.data_base.add_account(self.new_account)
        self.request = Actions.CreateAccountRequest(f"{self.entity.name} | ({self.entity.id}) | {bank} | {name}")
        self.data_base.add_request(self.request)
        self.window = MenuEntityController.MenuEntityController(self.entity)

####################################################################################################################

    def press_open_credit_window(self, obj):
        self.window = QtWidgets.QDialog()
        obj.setupUi(self.window, self.bank_list)
        self.window.show()

    def press_confirm_open_credit(self, bank_name, credit_info, sum):
        bank = self.data_base.get_bank_info_by_name(bank_name)
        credit = Entities.Credit
        for x in self.data_base.get_bank_credit_list(bank.id):
            if x.days == int(credit_info.split()[0]):
                credit = x
        data = (0,
                self.entity.id,
                self.data_base.get_bank_info_by_name(bank_name).id,
                0,
                "",
                sum,
                f"{credit_info}",
                0,
                credit.percent,
                credit.days)
        self.new_account = Entities.BankAccountCredit(data)
        self.request = Actions.CreditRequest(f"{self.entity.name} | ({self.entity.id}) | {bank_name} | {credit_info} | {sum}")
        self.data_base.add_request(self.request)
        self.data_base.add_account(self.new_account)
        self.window = MenuEntityController.MenuEntityController(self.entity)

####################################################################################################################

    def press_open_deposit_window(self, obj):
        self.window = QtWidgets.QDialog()
        obj.setupUi(self.window, self.bank_list)
        self.window.show()

    def press_confirm_open_deposit(self, bank_name, deposit_info, sum):
        print(bank_name)
        bank = self.data_base.get_bank_info_by_name(bank_name)
        deposit = Entities.Deposit
        for x in self.data_base.get_bank_credit_list(bank.id):
            if x.days == int(deposit_info.split()[0]):
                deposit = x
        data = (0,
            self.entity.id,
            self.data_base.get_bank_info_by_name(bank_name).id,
                0,
                "??????????????",
                sum,
                f"{deposit_info}",
                0,
                deposit.percent,
                deposit.days)
        self.new_account = Entities.BankAccountDeposit(data)
        self.request = Actions.DepositRequest(f"{self.entity.name} | ({self.entity.id}) | {bank_name} | {deposit_info} | {sum}")
        self.data_base.add_request(self.request)
        self.data_base.add_account(self.new_account)
        self.window = MenuEntityController.MenuEntityController(self.entity)

####################################################################################################################

    def press_open_transaction_window(self, obj):
        self.window = QtWidgets.QDialog()
        only_acc = []
        for x in self.entity_accounts:
            if x.type == "????????":
                only_acc.append(x)
        obj.setupUi(self.window, only_acc)
        self.window.show()

    def press_confirm_transaction(self, name_acc_from, num_acc_to, sum):
        acc_to = self.data_base.get_account_data_by_number(num_acc_to)
        if acc_to.type == "????????":
            for acc_from in self.entity_accounts:
                if acc_from.name == name_acc_from:
                    acc_from.money = acc_from.money - sum
                    acc_to.money = acc_to.money + sum
                    self.data_base.update_account_data(acc_to)
                    self.data_base.update_account_data(acc_from)

####################################################################################################################

    def press_cancel_button(self):
        self.window = MenuEntityController.MenuEntityController(self.entity)