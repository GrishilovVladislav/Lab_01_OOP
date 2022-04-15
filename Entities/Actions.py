import datetime

class RequestWithoutAutoTime():
    def __init__(self, data):
        self.id = data[0]
        self.type = data[1]
        self.time = data[2]
        self.info = data[3]
        self.approved = data[4]

class Request():
    def __init__(self, data):
        self.id = 0
        self.type = data[0]
        self.time = str(datetime.datetime.now())
        self.info = data[1]
        self.approved = 0

class RegisterRequest(Request):
    def __init__(self, info):
        super().__init__(("Запрос на регистрацию физ-лица", info))

class EntityRegisterRequest(Request):
    def __init__(self, info):
        super().__init__(("Запрос на регистрацию юр-лица", info))

class CreateAccountRequest(Request):
    def __init__(self, info):
        super().__init__(("Запрос на создание счета", info))

class SalaryRequest(Request):
    def __init__(self, info):
        super().__init__(("Запрос на зачисление зарплаты", info))

class TransactionRequest(Request):
    def __init__(self, info):
        super().__init__(("Запрос на перевод", info))

class CreditRequest(Request):
    def __init__(self, info):
        super().__init__(("Запрос на кредит", info))

class DepositRequest(Request):
    def __init__(self, info):
        super().__init__(("Запрос на депозит", info))


