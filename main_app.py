import pandas as pd
import talib as ta
import csv
import warnings
import numpy as np
import time
warnings.filterwarnings('ignore')

marketData = pd.read_csv('TRY_DATA.csv',index_col=['timestamp'])
df = pd.DataFrame(marketData)
pd.set_option('display.max_columns', None)

df['ENGULFING'] = ta.CDLENGULFING(df['Open'], df['High'], df['Low'], df['Close'])
df['HAMMER'] = ta.CDLHAMMER(df['Open'], df['High'], df['Low'], df['Close'])
df['SHOOTINGSTAR'] = ta.CDLSHOOTINGSTAR(df['Open'], df['High'], df['Low'], df['Close'])
df['DRAGONFLYDOJI'] = ta.CDLDRAGONFLYDOJI(df['Open'], df['High'], df['Low'], df['Close'])
df['DOJI'] = ta.CDLDOJI(df['Open'], df['High'], df['Low'], df['Close'])

print(df.head(50))

#
# print(df.head(49))
#
#
#













# while True:
#     engalfing = ta.CDLENGULFING(df['Open'], df['High'], df['Low'], df['Close'])
#     hammer = ta.CDLHAMMER(df['Open'], df['High'], df['Low'], df['Close'])
#     shooting_star = ta.CDLSHOOTINGSTAR(df['Open'], df['High'], df['Low'], df['Close'])
#     if engalfing[-1] == 0:
#         print("False")
#     else:
#         print('True')
#     time.sleep(1)
#



















