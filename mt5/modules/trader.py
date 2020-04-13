import sys
import os
import MetaTrader5 as mt5
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from libraries.utils import Utils

# TODO IMPLEMENT LOGS, DOCS


class Trader:

    @staticmethod
    @Utils.try_exc_none
    def num_orders():
        """
        Method to extract the number of the total of opened orders.
        Usage:
            >>>from modules.trader import Trader as trad
            >>>print(trad.num_orders())
            (0)
        """
        return mt5.orders_total()

    @staticmethod
    @Utils.try_exc_none
    def get_order(symbol=None, group=None, ticket=None):
        """
        Method to get a specific order information from a symbol, a group
        of symbols or an specific ticket
        Parameters:
            symbol: Market symbol like 'EURUSD', 'EURJPY', 'AUDJPY'
            group: A group of symbols like 'EUR*', '*USD'
            ticket: A specific order id or ticket.
        Usage:
            >>>from modules.trader import Trader as trad
            >>>print(trad.get_order(symbol='EURUSD'))
        """
        if symbol != None:
            orders = mt5.orders_get(symbol=symbol)
            name = symbol
        elif group != None:
            orders = mt5.orders_get(group=group)
            name = group
        elif ticket != None:
            orders = mt5.orders_get(ticket=ticket)
            name = ticket
        else:
            orders = mt5.orders_get()
            name = 'any'
        if orders != None:
            return orders
        else:
            print("No orders for {}, error code={}".format(
                name, mt5.last_error()))

    @staticmethod
    @Utils.try_exc_none
    def check_margin(action, symbol, lot, ask):
        """
        Method to calculate the amount of money that cost a size of 
        lot with the current ask
        Parameters:
            action:Order type
            symbol: Market symbol like 'EURUSD', 'EURJPY', 'AUDJPY'
            lot: A float with the amount of the lot to order.
            ask: Ask value from the symbol candlestick
        Usage:
            >>>
            >>>
            >>>
        """
        selected = mt5.symbol_select(symbol, True)
        if not selected:
            print("Failed to select {}, error: {}".format(
                symbol, mt5.last_error()))
        else:
            margin = mt5.order_calc_margin(action, symbol, lot, ask)
            if margin != None:
                return margin
            else:
                print("order_calc_margin failed,  error code: ", mt5.last_error())
