import sys
import os
import MetaTrader5 as mt5
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from libraries.utils import Utils
# TODO IMPLEMENT LOGS


class Puller:

    @staticmethod
    @Utils.try_exc_none
    def last_tick(symbol):
        """
        Method to take the value of the last candlestick of a specific symbol
        Parameters:
            symbol: Market symbol like 'EURUSD', 'EURJPY', 'AUDJPY'
        Usage:
            >>>from modules.puller import Puller as pull
            >>>print(pull.last_tick('EURUSD'))
        """
        selected = mt5.symbol_select(symbol, True)
        if not selected:
            print("Failed to select {}, error: {}".format(
                symbol, mt5.last_error()))
        else:
            return mt5.symbol_info_tick(symbol)

    @staticmethod
    @Utils.try_exc_none
    def all_symbols(symbol=None):
        """
        Method to get the info from all the actual symbols of from an specific one.
        Parameters:
            symbol:Market symbol like 'EURUSD', 'EURJPY', 'AUDJPY' or None for all of them.
        Usage:
            >>>from modules.puller import Puller as pull
            >>>print(pull.all_symbols())
        """
        if symbol == None:
            symbols = mt5.symbols_get()
        else:
            symbols = mt5.symbols_get(symbol)

        return symbols

    @staticmethod
    @Utils.try_exc_none
    def get_bars(symbol, timeframe, init_time, num_bars=99999):
        """
        Method to get a number of candlesticks until the defined init_time.
        Parameters:
            symbol:Market symbol like 'EURUSD', 'EURJPY', 'AUDJPY'
            timeframe:Timeframe like 'TIMEFRAME_M1', 'TIMEFRAME_H1', 'TIMEFRAME_D1'
            init_time:datetime type with timezone
            num_bars:amount of bars searching for.
        Usage:
            >>>from modules.puller import Puller as pull
            >>>from datetime import datetime
            >>>from libraries.constants import Constants
            >>>import MetaTrader5 as mt5
            >>>cts = Constants()
            >>>init_date = datetime.now(cts.TIMEZONE)
            >>>print(pull.get_bars("EURUSD",mt5.TIMEFRAME_M1, init_date))
        """
        selected = mt5.symbol_select(symbol, True)
        if not selected:
            print("Failed to select {}, error: {}".format(
                symbol, mt5.last_error()))
        else:
            rates = mt5.copy_rates_from(symbol, timeframe, init_time, num_bars)
            rates_frame = pd.DataFrame(rates)
            rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

            return rates_frame
