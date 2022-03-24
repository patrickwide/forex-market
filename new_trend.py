# import ccxt
# #import config
# import schedule
# import panda_learn
import warnings
import numpy as np
from datetime import datetime
import time
import pandas as pd
pd.set_option('display.max_rows', None)
warnings.filterwarnings('ignore')
bars = pd.read_csv('TRY_DATA.csv')

df = pd.DataFrame(bars[:-1], columns=['timestamp','open','high','low','close','volume'])
df['timestamp'] = pd.to_datetime(df['Date'])































#
#
# #
# def tr(data):
#     data['previous_close'] = data['close'].shift(1)
#     data['high-low'] = abs(data['high'] - data['Low'])
#     data['high-pc'] = abs(data['high'] - data['previous_close'])
#     data['low-pc'] = abs(data['low'] - data['previous_close'])
#
#     tr = data[['high-low', 'high-pc', 'low-pc']].max(axis=1)
#
#     return tr
#
#
# def atr(data, period):
#     data['tr'] = tr(data)
#     atr = data['tr'].rolling(period).mean()
#
#     return atr
#
#
#
# def supertrend(df, period=7, atr_multiplier=3):
#     hl2 = (df['high'] + df['low']) / 2
#     df['atr'] = atr(df, period)
#     df['upperband'] = hl2 + (atr_multiplier * df['atr'])
#     df['lowerband'] = hl2 - (atr_multiplier * df['atr'])
#
#     for current in range(1 , len(df.index)):
#         print(current)
#
#
#
# supertrend(df)
