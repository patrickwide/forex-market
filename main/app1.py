import talib
candle_names = talib.get_function_groups()['Pattern Recognition']

import requests
import pandas as pd
import numpy as np
import talib
from plotly.offline import plot
import plotly.graph_objs as go

from itertools import compress
from candle_rankings import candle_rankings
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# # link for Bitcoin Data
# link = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=365&aggregate=1"
#
# # API request historical
# historical_get = requests.get(link)
#
# # access the content of historical api request
# historical_json = historical_get.json()
#
# # extract json data as dictionary
# historical_dict = historical_json['Data']
#
# # extract Final historical df
# df = pd.DataFrame(historical_dict,
#                              columns=['close', 'high', 'low', 'open', 'time', 'volumefrom', 'volumeto'],
#                              dtype='float64')
#
# # time column is converted to "YYYY-mm-dd hh:mm:ss" ("%Y-%m-%d %H:%M:%S")
# posix_time = pd.to_datetime(df['time'], unit='s')
#
# # append posix_time
# df.insert(0, "Date", posix_time)
#
# # drop unix time stamp
# df.drop("time", axis = 1, inplace = True)
#
historical_dict = pd.read_csv('data.csv')


df = pd.DataFrame(historical_dict[:-1], columns=['time','close', 'high', 'low', 'open'])

last_row_index = len(df.index) - 1
previous_row_index = last_row_index - 1

# extract OHLC
op = df['open']
hi = df['high']
lo = df['low']
cl = df['close']
# create columns for each pattern

for candle in candle_names:
    # below is same as;
    # df["CDL3LINESTRIKE"] = talib.CDL3LINESTRIKE(op, hi, lo, cl)
    df[candle] = getattr(talib, candle)(op, hi, lo, cl)



# patterns not found in the patternsite.com
exclude_items = ('CDLCOUNTERATTACK',
                 'CDLLONGLINE',
                 'CDLSHORTLINE',
                 'CDLSTALLEDPATTERN',
                 'CDLKICKINGBYLENGTH')
candle_names = [candle for candle in candle_names if candle not in exclude_items]



df['candlestick_pattern'] = np.nan
df['candlestick_match_count'] = np.nan
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
            # print('1 buy found')
        # bear pattern -100 or -200
        else:
            pattern = list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0] + '_Bear'
            df.loc[index, 'candlestick_pattern'] = pattern
            df.loc[index, 'candlestick_match_count'] = 1
            # print('1 sell found')

    # multiple patterns matched -- select best performance
    else:
        # print('many')

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
                bear += 1
                container.append(pattern + '_Bear')

        rank_list = [candle_rankings[p] for p in container]
        if len(rank_list) == len(container):
            rank_index_best = rank_list.index(min(rank_list))
            df.loc[index, 'candlestick_pattern'] = container[rank_index_best]
            df.loc[index, 'candlestick_match_count'] = len(container)

# clean up candle columns
df.drop(candle_names, axis=1, inplace=True)

if df.candlestick_match_count[last_row_index] == 0:

    print('0 candles')

elif df.candlestick_match_count[last_row_index] == 1:

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





























# print(df.tail(5))
            # if len(rank_list) == len(container):
            #     rank_index_best = rank_list.index(min(rank_list))
            #     df.loc[index, 'candlestick_pattern'] = container[rank_index_best]
            #     df.loc[index, 'candlestick_match_count'] = len(container)
    # clean up candle columns
# cols_to_drop = candle_names + list(exclude_items)
# df.drop(cols_to_drop, axis = 1, inplace = True)
#
# print(df)
#
#
#
# o = df['open'].astype(float)
# h = df['high'].astype(float)
# l = df['low'].astype(float)
# c = df['close'].astype(float)
#
# trace = go.Candlestick(
#             open=o,
#             high=h,
#             low=l,
#             close=c)
# data = [trace]
#
# #plot(data, filename='go_candle1.html')
#
#
# layout = {
#     'title': '2019 Feb - 2020 Feb Bitcoin Candlestick Chart',
#     'yaxis': {'title': 'Price'},
#     'xaxis': {'title': 'Index Number'},
#
# }
# fig = dict(data=data, layout=layout)
# plot(fig, filename='btc_candles')

#
#































