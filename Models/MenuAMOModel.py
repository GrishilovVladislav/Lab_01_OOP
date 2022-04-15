from PyQt5 import QtWidgets
from DataBases import DataBase
from Entities import Entities
from Controllers import MenuAMOController

class MenuAMOModel():
    def __init__(self, obj):
        self.data_base = DataBase.WorkWithDB()
        self.logs = self.data_base.get_logs()
        self.not_approved_requests = self.data_base.get_requests(0)

        self.window = QtWidgets.QMainWindow()
        obj.setupUi(self.window, self.logs)
        self.window.show()

    def requests_button(self, obj):
        self.not_approved_requests = self.data_base.get_requests(0)
        self.window_requests = QtWidgets.QDialog()
        obj.setupUi(self.window_requests, self.not_approved_requests)
        self.window_requests.show()

    def exit_button(self):
        self.window_requests.close()

    def approve_button(self, data):
        for req in self.not_approved_requests:
            if data.split(" || ")[0] == req.type and data.split(" || ")[1] == req.info:
                self.data_base.confirm_request(req)

