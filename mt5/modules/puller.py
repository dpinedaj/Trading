import sys
import os
import MetaTrader5 as mt5
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from libraries.utils import Utils
# TODO IMPLEMENT LOGS, DOCS


class Puller:

    @staticmethod
    @Utils.try_exc_none
    def last_tick(symbol):
        """
        Method to take the values of the last candlestick of a specific symbol
        Parameters:
            symbol:
        Usage:
            >>>
            >>>
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
        
        """
        if symbol == None:
            symbols = mt5.symbols_get()
        else:
            symbols = mt5.symbols_get(symbol)

        return symbols

    @staticmethod
    @Utils.try_exc_none
    def get_bars(symbol, timeframe, init_time, num_bars=99999):

        selected = mt5.symbol_select(symbol, True)
        if not selected:
            print("Failed to select {}, error: {}".format(
                symbol, mt5.last_error()))
        else:
            rates = mt5.copy_rates_from(symbol, timeframe, init_time, num_bars)
            rates_frame = pd.DataFrame(rates)
            rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

            return rates_frame
