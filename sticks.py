import talib

import requests
import pandas as pd

# link for Bitcoin Data
link = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=365&aggregate=1"

# API request historical
historical_get = requests.get(link)

# access the content of historical api request
historical_json = historical_get.json()

# extract json data as dictionary
historical_dict = historical_json['Data']

# extract Final historical df
df = pd.DataFrame(historical_dict,
                             columns=['close', 'high', 'low', 'open', 'time', 'volumefrom', 'volumeto'],
                             dtype='float64')

# time column is converted to "YYYY-mm-dd hh:mm:ss" ("%Y-%m-%d %H:%M:%S")
posix_time = pd.to_datetime(df['time'], unit='s')

# append posix_time
df.insert(0, "Date", posix_time)

# drop unix time stamp
df.drop("time", axis = 1, inplace = True)

candle_names = talib.get_function_groups()['Pattern Recognition']


import numpy as np

a = "---------------------------------------------------"

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
        for pattern in patterns:
            if row[pattern] > 0:
                container.append(pattern + '_Bull')
            else:
                container.append(pattern + '_Bear')
        rank_list = [candle_rankings[p] for p in container]
        if len(rank_list) == len(container):
            rank_index_best = rank_list.index(min(rank_list))
            df.loc[index, 'candlestick_pattern'] = container[rank_index_best]
            df.loc[index, 'candlestick_match_count'] = len(container)
# clean up candle columns
df.drop(candle_names, axis=1, inplace=True)














#
# # def load_data(directory):
# #     result = []
# #     for filename in ["positives.txt", "negatives.txt"]:
# #         with open(os.path.join(directory, filename)) as f:
# #             result.append([
# #                 extract_words(line)
# #                 for line in f.read().splitlines()
# #             ])
# #     return result
# import os
# import ccxt
# import config
# import schedule
# # import panda_learn as pd
# import pandas as pd
# pd.set_option('display.max_rows', None)
# import talib as ta
# import warnings
#
# warnings.filterwarnings('ignore')
#
#
# data = pd.read_csv('countries.csv')
# cdl = pd.DataFrame(data)
# #
# # print(cdl['candle'])
# candle = cdl['candle']
#
# bars = pd.read_csv('usd.csv')
# df = pd.DataFrame(bars)
# df['ENGULFING'] = ta.CDLBELTHOLD(df['Open'], df['High'], df['Low'], df['Close'])
#
# print(df['ENGULFING'])