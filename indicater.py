# import ccxt
# #import config
# import schedule
# import panda_learn
import warnings
import numpy as np
from datetime import datetime
import time
import pandas as pd
pd.set_option('display.max_columns', None)
warnings.filterwarnings('ignore')
bars = pd.read_csv('TRY_DATA.csv')











# df = pd.DataFrame(bars[:-1], columns=['timestamp','Open','High','Low','Close','Volume'])

# df['Pivot'] = (df['High'] + df['Low']+ df['Close'])/3

# last_day = df.tail(1).copy()
#
# last_day['Pivot'] = (float(last_day['High']) + float(last_day['Low'])+ float(last_day['Close']))/3
#
# last_day['R1'] = 2*last_day['Pivot'] - last_day['Low']
# last_day['S1'] = 2 * last_day['Pivot'] - last_day['High']
# last_day['R2'] = last_day['Pivot'] + (last_day['High'] - last_day['Low'])
# last_day['S2'] = last_day['Pivot'] - (last_day['High'] - last_day['Low'])
# last_day['R3'] = last_day['Pivot'] + 2*(last_day['High'] - last_day['Low'])
# last_day['S3'] = last_day['Pivot'] - 2*(last_day['High'] - last_day['Low'])
#
# print(last_day)
#
# df.to_csv('bit_s_s.csv', index=False)

