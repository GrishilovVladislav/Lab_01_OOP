from PyQt5 import QtWidgets

import DataBases.DataBase
import Entities.Entities
from Controllers import FirstMenuController
import sys
import sqlite3

class Program():
    def start(self):

        self.app = QtWidgets.QApplication(sys.argv)
        self.Test = FirstMenuController.FirstMenuController()
        sys.exit(self.app.exec_())

    def show_window(self):
        pass



if __name__ == "__main__":
    Program.start(Program())



