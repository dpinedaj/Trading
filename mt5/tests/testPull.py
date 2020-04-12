import sys
import os
import pandas as pd
from datetime import datetime
import MetaTrader5 as mt5

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from modules.admin import Admin
from modules.puller import Puller as pull
from modules.constants import Constants
from modules.trader import Trader as trad

cts = Constants()
adm = Admin()
adm.login()


#print(adm.acc_info())
all_symbols = pull.all_symbols()
names = [s.name for s in all_symbols]
print(names)
print(pull.last_tick(names[0]))
#init_date = datetime.now(cts.TIMEZONE)
#rates = pull.get_bars("EURUSD",mt5.TIMEFRAME_M1, init_date)
#print(rates)

print(help(trad.num_orders))
#ask = pull.last_tick(names[0]).ask
#print('ask: ',ask)
#lot = 0.1
#symbol = names[0]
#action = mt5.ORDER_TYPE_SELL

#print(trad.check_margin(action,symbol, lot, ask))
trad.num_orders()
adm.close()
