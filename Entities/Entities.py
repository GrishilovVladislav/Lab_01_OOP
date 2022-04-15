

class User():
    def __init__(self, user_data):
        self.id = user_data[0]
        self.name = user_data[1]
        self.passport_seria = user_data[2]
        self.passport_number = user_data[3]
        self.identification_number = user_data[4]
        self.phone_number = user_data[5]
        self.email = user_data[6]
        self.login = user_data[7]
        self.password = user_data[8]
        self.approved = user_data[9]


class Entity():
    def __init__(self, data):
        self.id = data[0]
        self.type = data[1]
        self.name = data[2]
        self.main_address = data[3]
        self.UNP_number = data[4]
        self.login = data[5]
        self.password = data[6]
        self.approved = data[7]


class AMO():
    def __init__(self, data):
        self.id = data[0]
        self.name = "AMO"
        self.login = data[2]
        self.password = data[3]


class Operator(AMO):
    def __init__(self, data):
        super().__init__(data)
        self.name = "Оператор"


class Manager(AMO):
    def __init__(self, data):
        super().__init__(data)
        self.name = "Менеджер"


class Admin(AMO):
    def __init__(self, data):
        super().__init__(data)
        self.name = "Админ"


class Bank():
    def __init__(self, data):
        self.id = data[0]
        self.name = data[1]
        self.identify_code = data[2]
        self.credits_list = data[3]
        self.deposits_list = data[4]

class BankAccount():
    def __init__(self, data):
        self.id = data[0]
        self.client_id = data[1]
        self.bank_id = data[2]
        self.number = data[3]
        self.type = "Счет"
        self.money = data[5]
        self.name = data[6]
        self.approved = data[7]

class BankAccountCredit(BankAccount):
    def __init__(self, data):
        super().__init__(data)
        self.money = abs(self.money) * (-1)
        self.type = "Кредит"
        self.percent = data[7]
        self.days = data[8]

class BankAccountDeposit(BankAccount):
    def __init__(self, data):
        super().__init__(data)
        self.type = "Депозит"
        self.percent = data[7]
        self.days = data[8]

class Credit():
    def __init__(self, data):
        self.id = data[0]
        self.bank_id = data[1]
        self.percent = data[2]
        self.days = data[3]

class Deposit():
    def __init__(self, data):
        self.id = data[0]
        self.bank_id = data[1]
        self.percent = data[2]
        self.days = data[3]

class Operation():
    def __init__(self, data):
        self.id = data[0]
        self.client_id = data[1]
        self.money = data[2]
        self.approved = data[3]


class Salary(Operation):
    def __init__(self, data):
        super().__init__(data)
        self.type = "Зарплата"
        self.to_client_id = data[4]


class Transaction(Operation):
    def __init__(self, data):
        super().__init__(data)
        self.type = "Перевод"
        self.to_client_id = data[4]

class Log():
    def __init__(self, data):
        self.id = data[0]
        self.time = data[1]
        self.info = data[2]




