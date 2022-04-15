import random
import sqlite3
import datetime
from Entities import Entities, Actions
DATA_BASE_NAME = "DataBases/Entities.db"


class WorkWithDB():

    def __init__(self):
        self.data_base = sqlite3.connect(DATA_BASE_NAME)
        self.cursor = self.data_base.cursor()
        try:
            self.last_user_id = self.cursor.execute("""SELECT id FROM users ORDER BY id DESC LIMIT 1""").fetchone()[0]
        except:
            self.last_user_id = 0
        try:
            self.last_entity_id = self.cursor.execute("""SELECT id FROM entities ORDER BY id DESC LIMIT 1""").fetchone()[0]
        except:
            self.last_entity_id = 0
        if self.last_entity_id > self.last_user_id:
            self.last_client_id = self.last_entity_id
        else:
            self.last_client_id = self.last_user_id
        try :
            self.last_request_id = self.cursor.execute("""SELECT id FROM requests ORDER BY id DESC LIMIT 1""").fetchone()[0]
        except:
            self.last_request_id = 0
        try:
            self.last_action_id = self.cursor.execute("""SELECT id FROM operations ORDER BY id DESC LIMIT 1""").fetchone()[0]
        except:
            self.last_action_id = 0
        try:
             self.last_account_id = self.cursor.execute("""SELECT id FROM accounts ORDER BY id DESC LIMIT 1""").fetchone()[0]
        except:
             self.last_account_id = 0
        try:
            self.last_log_id = self.cursor.execute("""SELECT id FROM logs ORDER BY id DESC LIMIT 1""").fetchone()[0]
        except:
            self.last_log_id = 0

    def get_info(self, obj):
        self.dict = obj.__dict__
        self.tuple_info = tuple(self.dict.values())

#######################################################################################################################3

    def add_request(self, obj):
        self.get_info(obj)
        self.cursor.execute(f"""INSERT INTO requests VALUES(
                                    '{self.last_request_id + 1}',
                                    '{self.tuple_info[1]}',
                                    '{self.tuple_info[2]}',
                                    '{self.tuple_info[3]}',
                                    '{self.tuple_info[4]}'
                                    )""")
        self.data_base.commit()
        log_data = (0, str(datetime.datetime.now().strftime("%Y %m %d %H:%M:%S")), f"Added request: {self.tuple_info[1]} {self.tuple_info[3].split()[0]} {self.tuple_info[3].split()[1]} {self.tuple_info[3].split()[2]}")
        self.add_log(Entities.Log(log_data))

    def confirm_request(self, obj):
        self.get_info(obj)
        self.cursor.execute(f"""UPDATE requests SET
                                        approved = '{1}'
                                WHERE id = {self.tuple_info[0]}
                            """)
        self.data_base.commit()
        log_data = (0, str(datetime.datetime.now().strftime("%Y %m %d %H:%M:%S")), f"Confirmed request: {self.tuple_info[1]} {self.tuple_info[3]}")
        self.add_log(Entities.Log(log_data))
        self.get_info(obj)
        if self.tuple_info[1] == Actions.RegisterRequest("").type:
            self.confirm_user(self.tuple_info[3].split()[5])
        if self.tuple_info[1] == Actions.EntityRegisterRequest("").type:
            self.confirm_entity(self.tuple_info[3].split()[2])
        if self.tuple_info[1] == Actions.DepositRequest("").type or self.tuple_info[1] == Actions.CreditRequest("").type or self.tuple_info[1] == Actions.CreateAccountRequest("").type:
            accounts = self.get_accounts_data_by_client_id(int(self.tuple_info[3].split(" | ")[1][1:-1]), 0)
            for account in accounts:
                if self.tuple_info[3].split(" | ")[3] == account.name:
                    self.confirm_account(account.id)
        if self.tuple_info[1] == Actions.TransactionRequest("").type:
            pass


########################################################################################################################

    def add_user(self, obj):
        self.get_info(obj)
        self.cursor.execute(f"""INSERT INTO users VALUES(
                            '{self.last_client_id + 1}',
                            '{self.tuple_info[1]}',
                            '{self.tuple_info[2]}',
                            '{self.tuple_info[3]}',
                            '{self.tuple_info[4]}',
                            '{self.tuple_info[5]}',
                            '{self.tuple_info[6]}',
                            '{self.tuple_info[7]}',
                            '{self.tuple_info[8]}',
                            '{self.tuple_info[9]}'
                            )""")
        self.data_base.commit()

    def confirm_user(self, login):
        self.cursor.execute(f"""UPDATE users SET 
                                            approved = '{1}'
                                        WHERE login = '{login}'
                                            """)
        self.data_base.commit()

    def update_user_data(self, obj):
        self.get_info(obj)
        self.cursor.execute(f"""UPDATE users SET 
                                    name = '{self.tuple_info[1]}',
                                    passport_seria = '{self.tuple_info[2]}',
                                    passport_number = '{self.tuple_info[3]}',
                                    identification_number = '{self.tuple_info[4]}',
                                    phone_number = '{self.tuple_info[5]}',
                                    email = '{self.tuple_info[6]}',
                                    login = '{self.tuple_info[7]}',
                                    password = '{self.tuple_info[8]}' 
                                WHERE id = '{self.tuple_info[0]}'
                                    """)
        self.data_base.commit()

    def get_user_data(self, id):
        self.cursor.execute(f"""SELECT * FROM users WHERE id = {id}""")
        self.user = Entities.User(self.cursor.fetchall()[0])
        return self.user

    def get_user_enter_data(self, login):
        try:
            self.cursor.execute(f"""SELECT * FROM users WHERE login = '{login}'""")
            self.user = Entities.User(self.cursor.fetchall()[0])
            return self.user
        except:
            return None


########################################################################################################################

    def add_entity(self, obj):
        self.get_info(obj)
        self.cursor.execute(f"""INSERT INTO entities VALUES(
                            '{self.last_client_id + 1}',
                            '{self.tuple_info[1]}',
                            '{self.tuple_info[2]}',
                            '{self.tuple_info[3]}',
                            '{self.tuple_info[4]}',
                            '{self.tuple_info[5]}',
                            '{self.tuple_info[6]}',
                            '{self.tuple_info[7]}'
                            )""")
        self.data_base.commit()

    def confirm_entity(self, login):
        self.cursor.execute(f"""UPDATE entities SET 
                                            approved = '{1}'
                                        WHERE login = '{login}'
                                            """)
        self.data_base.commit()

    def update_entity_data(self, obj):
        self.get_info(obj)
        self.cursor.execute(f"""UPDATE entities SET 
                                    type = '{self.tuple_info[1]}',
                                    name = '{self.tuple_info[2]}',
                                    main_adress = '{self.tuple_info[3]}',
                                    UNP_number = '{self.tuple_info[4]}',
                                    login = '{self.tuple_info[5]}',
                                    password = '{self.tuple_info[6]}'
                                WHERE id = '{self.tuple_info[0]}'
                                    """)
        self.data_base.commit()

    def get_entity_data(self, id):
        self.cursor.execute(f"""SELECT * FROM entities WHERE id = {id}""")
        entity = Entities.Entity(self.cursor.fetchall()[0])
        return entity

    def get_entity_enter_data(self, login):
        try:
            self.cursor.execute(f"""SELECT * FROM entities WHERE login = '{login}'""")
            entity = Entities.Entity(self.cursor.fetchall()[0])
            return entity
        except:
            return None

########################################################################################################################

    def add_account(self, obj):
        self.get_info(obj)
        self.cursor.execute(f"""INSERT INTO accounts VALUES(
                                            '{self.last_account_id + 1}',
                                            '{self.tuple_info[1]}',
                                            '{self.tuple_info[2]}',
                                            '{random.randint(10000000, 99999999)}',
                                            '{self.tuple_info[4]}',
                                            '{self.tuple_info[5]}',
                                            '{self.tuple_info[6]}',
                                            '{self.tuple_info[7]}'
                                            )""")

        self.data_base.commit()

    def confirm_account(self, id):
        self.cursor.execute(f"""UPDATE accounts SET 
                                            approved = '{1}'
                                        WHERE id = '{id}'
                                            """)
        self.data_base.commit()

    def update_account_data(self, obj):
        self.get_info(obj)
        self.cursor.execute(f"""UPDATE accounts SET 
                                            money = '{self.tuple_info[5]}',
                                            name = '{self.tuple_info[6]}'
                                        WHERE id = '{self.tuple_info[0]}'
                                            """)
        self.data_base.commit()
        log_data = (0, str(datetime.datetime.now().strftime("%Y %m %d %H:%M:%S")),
                    f"Updated account: {self.tuple_info[3]} | {self.tuple_info[6]} | {self.tuple_info[5]}")
        self.add_log(Entities.Log(log_data))

    def get_account_data(self, id):
        try:
            self.cursor.execute(f"""SELECT type FROM accounts WHERE id = '{id}'""")
            type = self.cursor.fetchall()[0][0]
            if type == "Счет":
                self.cursor.execute(f"""SELECT * FROM accounts WHERE id = '{id}'""")
                return Entities.BankAccount(self.cursor.fetchall()[0])
            elif type == "Кредит":
                self.cursor.execute(f"""SELECT * FROM accounts WHERE id = '{id}'""")
                data = []
                for x in self.cursor.fetchall()[0]:
                    data.append(x)
                data.append(int(x[6].split()[2][1:-2]))
                data.append(int(x[6].split()[0]))
                return Entities.BankAccountCredit(data)
            elif type == "Депозит":
                self.cursor.execute(f"""SELECT * FROM accounts WHERE id = '{id}'""")
                data = []
                for x in self.cursor.fetchall()[0]:
                    data.append(x)
                data.append(int(x[6].split()[2][1:-2]))
                data.append(int(x[6].split()[0]))
                return Entities.BankAccountDeposit(data)
        except:
            return None

    def get_account_data_by_number(self, number):
        try:
            self.cursor.execute(f"""SELECT type FROM accounts WHERE number = '{number}'""")
            type = self.cursor.fetchall()[0][0]
            if type == "Счет":
                self.cursor.execute(f"""SELECT * FROM accounts WHERE number = '{number}'""")
                return Entities.BankAccount(self.cursor.fetchall()[0])
            elif type == "Кредит":
                self.cursor.execute(f"""SELECT * FROM accounts WHERE number = '{number}'""")
                data = []
                for x in self.cursor.fetchall()[0]:
                    data.append(x)
                data.append(int(x[6].split()[2][1:-2]))
                data.append(int(x[6].split()[0]))
                return Entities.BankAccountCredit(data)
            elif type == "Депозит":
                self.cursor.execute(f"""SELECT * FROM accounts WHERE number = '{number}'""")
                data = []
                for x in self.cursor.fetchall()[0]:
                    data.append(x)
                data.append(int(x[6].split()[2][1:-2]))
                data.append(int(x[6].split()[0]))
                return Entities.BankAccountDeposit(data)
        except:
            return None

    def get_accounts_data_by_client_id(self, client_id, approved = 1):
        self.cursor.execute(f"""SELECT * FROM accounts WHERE client_id = {client_id} AND 
                                                             approved = {approved}
                            """)
        accounts_list = self.cursor.fetchall()
        accounts = []
        for account in accounts_list:
            if account[4] == "Счет":
                accounts.append(Entities.BankAccount(account))
            elif account[4] == "Кредит":
                temp_account =[]
                for x in account:
                    temp_account.append(x)
               # temp_account[4] = f"{temp_account[4]} до {1}"
                temp_account.append(int(account[6].split()[2][1:-2]))
                temp_account.append(int(account[6].split()[0]))
                accounts.append(Entities.BankAccountCredit(temp_account))
            elif account[4] == "Депозит":
                temp_account = []
                for x in account:
                    temp_account.append(x)
                temp_account.append(int(account[6].split()[2][1:-2]))
                temp_account.append(int(account[6].split()[0]))
                accounts.append(Entities.BankAccountDeposit(temp_account))
        return accounts

###################################################################################################

    def get_bank_info(self, id):
        try:
            self.cursor.execute(f"""SELECT * FROM banks WHERE id = '{id}'""")
            bank = Entities.Bank(self.cursor.fetchall()[0])
            return bank
        except:
            return None

    def get_bank_info_by_name(self, name):

        self.cursor.execute(f"""SELECT * FROM banks WHERE name = '{name}'""")
        x = self.cursor.fetchall()[0]
        credit_list = self.get_bank_credit_list(x[0])
        deposit_list = self.get_bank_deposit_list(x[0])
        data_for_bank = []
        for element in x:
            data_for_bank.append(element)
        data_for_bank.append(credit_list)
        data_for_bank.append(deposit_list)
        bank = Entities.Bank(data_for_bank)
        return bank

    def get_bank_list(self):
        self.cursor.execute(f"""SELECT * FROM banks""")
        self.bank_list = []
        i = 0
        for x in self.cursor.fetchall():
            credit_list = self.get_bank_credit_list(x[0])
            deposit_list = self.get_bank_deposit_list(x[0])
            data_for_bank = []
            for element in x:
                data_for_bank.append(element)
            data_for_bank.append(credit_list)
            data_for_bank.append(deposit_list)
            self.bank_list.append(Entities.Bank(data_for_bank))
            i += 1
        return self.bank_list

#####################################################################################################

    def get_bank_credit_list(self, bank_id):
        try:
            self.cursor.execute(f"""SELECT * FROM credits WHERE bank_id = {bank_id}""")
            credit_list = []
            for x in self.cursor.fetchall():
                credit_list.append(Entities.Credit(x))
            return credit_list
        except:
            return None

    def get_bank_deposit_list(self, bank_id):
        try:
            self.cursor.execute(f"""SELECT * FROM deposits WHERE bank_id = {bank_id}""")
            deposit_list = []
            for x in self.cursor.fetchall():
                deposit_list.append(Entities.Deposit(x))
            return deposit_list
        except:
            return None

######################################################################################################

    def add_log(self, log):
        self.get_info(log)
        self.cursor.execute(f"""INSERT INTO logs VALUES(
                                    '{self.last_log_id + 1}',
                                    '{self.tuple_info[1]}',
                                    '{self.tuple_info[2]}'
                                    )""")
        self.data_base.commit()

#####################################################################################################

    def get_logs(self):
        self.cursor.execute(f"""SELECT * FROM logs""")
        list = []
        for x in self.cursor.fetchall():
            list.append(Entities.Log(x))
        return list

    def get_users(self):
        self.cursor.execute(f"""SELECT * FROM users""")
        list = []
        for x in self.cursor.fetchall():
            list.append(Entities.User(x))
        return list

    def get_entities(self):
        self.cursor.execute(f"""SELECT * FROM entities""")
        list = []
        for x in self.cursor.fetchall():
            list.append(Entities.User(x))
        return list

    def get_accounts(self):
        self.cursor.execute(f"""SELECT * FROM accounts WHERE type = 'Счет'""")
        list = []
        for x in self.cursor.fetchall():
            list.append(Entities.BankAccount(x))
        self.cursor.execute(f"""SELECT * FROM accounts WHERE type = 'Кредит'""")
        for x in self.cursor.fetchall():
            temp_x = []
            for e in x:
                temp_x.append(e)
            temp_x.append(int(x[6].split()[2][1:-2]))
            temp_x.append(int(x[6].split()[0]))
            list.append(Entities.BankAccountCredit(temp_x))
        self.cursor.execute(f"""SELECT * FROM accounts WHERE type = 'Депозит'""")
        for x in self.cursor.fetchall():
            temp_x = []
            for e in x:
                temp_x.append(e)
            temp_x.append(int(x[6].split()[2][1:-2]))
            temp_x.append(int(x[6].split()[0]))
            list.append(Entities.BankAccountDeposit(temp_x))
        return list

    def get_requests(self, approved):
        self.cursor.execute(f"""SELECT * FROM requests WHERE approved = '{approved}'""")
        list = []
        for x in self.cursor.fetchall():
            list.append(Actions.RequestWithoutAutoTime(x))
        return list
