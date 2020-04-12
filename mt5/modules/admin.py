from libraries.utils import Utils
import sys
import os
import MetaTrader5 as mt5
import pandas as pd
from .constants import Constants
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# TODO IMPLEMENT LOGS, DOCS


class Admin:
    """
    Module to manage connections and interface with metatrader 5.
    """

    def __init__(self):
        self.__initialize()
        self.cts = Constants()

    @Utils.try_exc
    def __initialize(self):
        """
        Method to initialize the service of mt5, for intern usage.
        """
        if not mt5.initialize():
            print("initialize() failed, error code =", mt5.last_error())

    @Utils.try_exc_none
    def login(self, usr=None, pwd=None):
        """
        Method to login in the mt5_terminal.
        Parameters:
            usr: integer with the login user of the demo account
            pwd: string with the password of the respective usr login.
        Return: Returns True if the service is correctly logged in, in other case return False.
        Usage:
            >>>from admin import Admin
            >>>adm = admin()
            >>>adm.login(23451321, 'asdfjkh')
            (True)

        """
        if usr == None:
            usr = self.cts.USR

        if pwd == None:
            pwd = self.cts.PWD
        self.connected = mt5.login(login=usr, password=pwd)
        return self.connected

    @Utils.try_exc
    def close(self):
        """
        Method to close the connection with mt5 terminal.
        Is important to close the connection in the end of every Script
        Usage:
            >>>from admin import Admin
            >>>adm = admin()
            >>>adm.login(23451321, 'asdfjkh')
            >>>adm.close()
        """
        mt5.shutdown()

    @Utils.try_exc_none
    def acc_info(self):
        """
        Returns a dataframe with all the account information
        Usage:
            >>>from admin import Admin
            >>>adm = admin()
            >>>adm.login(23451321, 'asdfjkh')
            >>>print(adm.acc_info())
            >>>adm.close()
            (Pandas Dataframe)
        """

        if self.connected:
            acc_dict = mt5.account_info()._asdict()
            df = pd.DataFrame(list(acc_dict.items()),
                              columns=['property', 'value'])
            return df
        else:
            print("The account isn't connected")

    @Utils.try_exc
    def terminal_info(self):
        """
        Returns a dataframe with all the terminal information
        Usage:
            >>>from admin import Admin
            >>>adm = admin()
            >>>adm.login(23451321, 'asdfjkh')
            >>>print(adm.terminal_info())
            >>>adm.close()
            (Pandas Dataframe)
        """
        if self.connected:
            terminal_info_dict = mt5.terminal_info()._asdict()
            df = pd.DataFrame(list(terminal_info_dict.items()),
                              columns=['property', 'value'])
            return df
        else:
            print("The account isn't connected")
