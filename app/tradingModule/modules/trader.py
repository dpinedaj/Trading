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
            >>>from trader import Trader as trad
            >>>print(trad.num_orders())
            (0)
        """
        return mt5.orders_total()

    @staticmethod
    @Utils.try_exc_none
    def get_order(symbol=None, group=None, ticket=None):
        """
        Method to get a specific order information
        Parameters:
            symbol: 
            group:
            ticket:
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
        Method to calculate the amount of money that cost a size of lot with the current ask
        Parameters:
            action:
            symbol:
            lot:
            ask:
        Usage:
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
