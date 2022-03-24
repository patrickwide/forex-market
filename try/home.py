# import ccxt
# import config
# import schedule
# import panda_learn as pd
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
from candle_rankings import candle_rankings
from itertools import compress
import warnings
warnings.filterwarnings('ignore')
import numpy as np
from datetime import datetime
import time
import talib as ta


data = pd.read_csv('tesla.csv')

def tr(data):
    data['previous_close'] = data['close'].shift(1)
    data['high-low'] = abs(data['high'] - data['low'])
    data['high-pc'] = abs(data['high'] - data['previous_close'])
    data['low-pc'] = abs(data['low'] - data['previous_close'])
    tr = data[['high-low', 'high-pc', 'low-pc']].max(axis=1)

    return tr


def atr(data, period):
    data['tr'] = tr(data)
    atr = data['tr'].rolling(period).mean()

    return atr


def supertrend(df, period=7, atr_multiplier=3):
    hl2 = (df['high'] + df['low']) / 2
    df['atr'] = atr(df, period)
    df['upperband'] = hl2 + (atr_multiplier * df['atr'])
    df['lowerband'] = hl2 - (atr_multiplier * df['atr'])
    df['in_uptrend'] = True

    # we loop over the data
    for current in range(1, len(df.index)):
        previous = current - 1

        # if current close is grater than previous upperband then it's in uptrend
        if df['close'][current] > df['upperband'][previous]:
            df['in_uptrend'][current] = True

        # if current close is less then the previous lowerband then not in uptrend
        elif df['close'][current] < df['lowerband'][previous]:
            df['in_uptrend'][current] = False

        else:
            df['in_uptrend'][current] = df['in_uptrend'][previous]

            if df['in_uptrend'][current] and df['lowerband'][current] < df['lowerband'][previous]:
                df['lowerband'][current] = df['lowerband'][previous]

            if not df['in_uptrend'][current] and df['upperband'][current] > df['upperband'][previous]:
                df['upperband'][current] = df['upperband'][previous]

    # return df


def technical_analisis(df):
    # extract OHLC
    op = df['open']
    hi = df['high']
    lo = df['low']
    cl = df['close']

    # create columns for each pattern
    global candle_names
    candle_names = ta.get_function_groups()['Pattern Recognition']
    for candle in candle_names:
        # below is same as;
        # df["CDL3LINESTRIKE"] = talib.CDL3LINESTRIKE(op, hi, lo, cl)
        df[candle] = getattr(ta, candle)(op, hi, lo, cl)

    # patterns not found in the patternsite.com
    global exclude_items
    exclude_items = ('CDLCOUNTERATTACK',
                     'CDLLONGLINE',
                     'CDLSHORTLINE',
                     'CDLSTALLEDPATTERN',
                     'CDLKICKINGBYLENGTH')

    return candle_names , exclude_items

candle_names , exclude_items = technical_analisis(df=data)

def pattern(df, candle_names = candle_names):

    technical_analisis(data)
    candle_names = [candle for candle in candle_names if candle not in exclude_items]

    for index, row in df.iterrows():
        # no pattern found
        if len(row[candle_names]) - sum(row[candle_names] == 0) == 0:

            # print('no pattern found')
            df.loc[index, 'pattern'] = '0'

        # single pattern found
        elif len(row[candle_names]) - sum(row[candle_names] == 0) == 1:

            # bull pattern 100 or 200
            if any(row[candle_names].values > 0):
                # print("BULL")
                df.loc[index, 'pattern'] = '1'

            # bear pattern -100 or -200
            else:
                # print("BEAR")
                df.loc[index, 'pattern'] = '-1'

        # multiple patterns matched -- select best performance
        else:
            # print('multiple')
            df.loc[index, 'pattern'] = '2'



def label(df):
    df = df
    # WE CHECK THE PATTERN
    # IF THE PATTERN IS 0:
    #   LABEL = 0 #
    df.loc[df['pattern'] == '0', 'label'] = '0'

    # IF THE PATTERN IS 1 AND CLOSE < CLOSE.SHIFT = 1#
    df.loc[(df['pattern'] == '1') & (df['close'] < df['close'].shift(-1)), 'label'] = "1"
    df.loc[(df['pattern'] == '1') & (df['close'] >= df['close'].shift(-1)), 'label'] = "0"

    # IF THE PATTERN IS -1 AND CLOSE > CLOSE.SHIFT = -1#
    df.loc[(df['pattern'] == '-1') & (df['close'] > df['close'].shift(-1)), 'label'] = "-1"
    df.loc[(df['pattern'] == '-1') & (df['close'] <= df['close'].shift(-1)), 'label'] = "0"

    # IF THE PATTERN IS 2 AND CLOSE < CLOSE.SHIFT = 1#
    df.loc[(df['pattern'] == '2') & (df['close'] < df['close'].shift(-1)), 'label'] = "1"

    # IF THE PATTERN IS 2 AND CLOSE > CLOSE.SHIFT = -1#
    df.loc[(df['pattern'] == '2') & (df['close'] > df['close'].shift(-1)), 'label'] = "-1"

    return df







def run(df=data):
    df=df
    supertrend(df)
    technical_analisis(df)
    pattern(df)
    label(df)
    df.to_csv('final_3.csv')
    return df

print(run(data))












