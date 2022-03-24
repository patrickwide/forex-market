import ccxt
import config
import schedule
# import panda_learn as pd
import pandas
pandas.set_option('display.max_rows', None)
from candle_rankings import candle_rankings

from itertools import compress
import warnings

warnings.filterwarnings('ignore')

import numpy as np
from datetime import datetime
import time

exchange = ccxt.binanceus({
    "apiKey": config.BINANCE_API_KEY,
    "secret": config.BINANCE_SECRET_KEY
})


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

    for current in range(1, len(df.index)):
        previous = current - 1

        if df['close'][current] > df['upperband'][previous]:
            df['in_uptrend'][current] = True
        elif df['close'][current] < df['lowerband'][previous]:
            df['in_uptrend'][current] = False
        else:
            df['in_uptrend'][current] = df['in_uptrend'][previous]

            if df['in_uptrend'][current] and df['lowerband'][current] < df['lowerband'][previous]:
                df['lowerband'][current] = df['lowerband'][previous]

            if not df['in_uptrend'][current] and df['upperband'][current] > df['upperband'][previous]:
                df['upperband'][current] = df['upperband'][previous]

    return df

in_position = False

import talib as ta

def check_buy_sell_signals(df):

    global in_position
    print("checking for buy and sell signals")
    print(df.tail(5))
    last_row_index = len(df.index) - 1
    previous_row_index = last_row_index - 1


    # extract OHLC
    op = df['open']
    hi = df['high']
    lo = df['low']
    cl = df['close']

    # create columns for each pattern
    candle_names = ta.get_function_groups()['Pattern Recognition']

    for candle in candle_names:
        # below is same as;
        # df["CDL3LINESTRIKE"] = talib.CDL3LINESTRIKE(op, hi, lo, cl)
        df[candle] = getattr(ta, candle)(op, hi, lo, cl)

    # patterns not found in the patternsite.com
    exclude_items = ('CDLCOUNTERATTACK',
                     'CDLLONGLINE',
                     'CDLSHORTLINE',
                     'CDLSTALLEDPATTERN',
                     'CDLKICKINGBYLENGTH')

    candle_names = [candle for candle in candle_names if candle not in exclude_items]

    for index, row in df.iterrows():
        # no pattern found
        if len(row[candle_names]) - sum(row[candle_names] == 0) == 0:
            df.loc[index, 'candlestick_pattern'] = "NO_PATTERN"
            df.loc[index, 'candlestick_match_count'] = 0
        # single pattern found
        elif len(row[candle_names]) - sum(row[candle_names] == 0) == 1:
            # bull pattern 100 or 200
            if any(row[candle_names].values > 0):
                pattern = list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0] + '_Bull'
                df.loc[index, 'candlestick_pattern'] = pattern
                df.loc[index, 'candlestick_match_count'] = 1
            # bear pattern -100 or -200
            else:
                pattern = list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0] + '_Bear'
                df.loc[index, 'candlestick_pattern'] = pattern
                df.loc[index, 'candlestick_match_count'] = 1

        # multiple patterns matched -- select best performance
        else:
            # filter out pattern names from bool list of values
            patterns = list(compress(row[candle_names].keys(), row[candle_names].values != 0))
            container = []
            bull = int()
            bear = int()

            for pattern in patterns:
                if row[pattern] > 0:
                    container.append(pattern + '_Bull')
                    bull += 1
                else:
                    container.append(pattern + '_Bear')
                    bear += 1
            rank_list = [candle_rankings[p] for p in container]
            if len(rank_list) == len(container):
                rank_index_best = rank_list.index(min(rank_list))
                df.loc[index, 'candlestick_pattern'] = container[rank_index_best]
                df.loc[index, 'candlestick_match_count'] = len(container)
    # clean up candle columns
    df.drop(candle_names, axis=1, inplace=True)

    if not df['in_uptrend'][previous_row_index] and df['in_uptrend'][last_row_index]:
        print("changed to uptrend!")
        print("Checking for any signals")

        if df.candlestick_match_count[last_row_index] == 0:
            print('No candle match')

        elif df.candlestick_match_count[last_row_index] == 1:
            print('1 candle')
            if any(row[candle_names].values > 0):
                print(list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0])
                print('buy signal')
            else:
                print(list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0])
                print('sell signal')

        else:
            print('multiple candles:')
            if bull > bear:
                print(f'{bull}/{len(container)}')
                print('Buy signal')

            elif bull < bear:
                print(f'{bear}/{len(container)}')
                print('Sell signal')
            else:
                print(f'Bull = {bull}/{len(container)}')
                print(f'Bear = {bear}/{len(container)}')
                print('Unpredictable signal')



    elif df['in_uptrend'][last_row_index]:  # UP TREND
        print("In uptrend!")
        print("Checking for any signals")
        print(df['timestamp'][last_row_index])

        if df.candlestick_match_count[last_row_index] == 0:
            print('0 candles')

    if df['in_uptrend'][previous_row_index] and not df['in_uptrend'][last_row_index]:
        print("Change to downtrend!")
        print('Checking for any signals')
        print(df['timestamp'][last_row_index])

        if df.candlestick_match_count[last_row_index] == 0:
            print('0 candles')

        elif df.candlestick_match_count[last_row_index] == 1:
            print('1 candle')
            if any(row[candle_names].values > 0):
                print(list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0])
                print('buy signal')
            else:
                print(list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0])
                print('sell signal')

        else:
            print('multiple candles:')
            if bull > bear:
                print(f'{bull}/{len(container)}')
                print('Buy signal')

            elif bull < bear:
                print(f'{bear}/{len(container)}')
                print('Sell signal')
            else:
                print(f'Bull = {bull}/{len(container)}')
                print(f'Bear = {bear}/{len(container)}')
                print('Unpredictable signal')



    elif not df['in_uptrend'][last_row_index]:
        print("In downtrend!")
        print('Checking for any signals')

        if df.candlestick_match_count[last_row_index] == 0:
            print('0 candles')

        elif df.candlestick_match_count[last_row_index] == 1:
            print('1 candle')
            if any(row[candle_names].values > 0):
                print(list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0])
                print('buy signal')
            else:
                print(list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0])
                print('sell signal')

        else:
            print('multiple candles:')
            if bull > bear:
                print(f'{bull}/{len(container)}')
                print('Buy signal')

            elif bull < bear:
                print(f'{bear}/{len(container)}')
                print('Sell signal')
            else:
                print(f'Bull = {bull}/{len(container)}')
                print(f'Bear = {bear}/{len(container)}')
                print('Unpredictable signal')


def run_bot():
    print(f"Fetching new bars for {datetime.now().isoformat()}")
    bars = exchange.fetch_ohlcv('BTC/USD', timeframe='1m', limit=100)
    df = pandas.DataFrame(bars[:-1], columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pandas.to_datetime(df['timestamp'], unit='ms')

    supertrend_data = supertrend(df)
    check_buy_sell_signals(supertrend_data)


schedule.every(60).seconds.do(run_bot)


while True:
    schedule.run_pending()
    time.sleep(1)










    # if in_position:
    #     order = exchange.create_market_sell_order('ETH/USD', 0.05)
    #     print(order)
    #     in_position = False
    # else:
    #     print("You aren't in position, nothing to sell")

    # if not in_position:
        #     order = exchange.create_market_buy_order('ETH/USD', 0.05)
        #     print(order)
        #     in_position = True
        # else:
        #     print("already in position, nothing to do")
    # from here starting here check for sell signals
