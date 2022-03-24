



# from plotly.offline import plot
# import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('./new.csv')

o = df['open'].astype(float)
h = df['high'].astype(float)
l = df['low'].astype(float)
c = df['close'].astype(float)

trace = go.Candlestick(
            open=o,
            high=h,
            low=l,
            close=c)
data = [trace]

#plot(data, filename='go_candle1.html')


layout = {
    'title': '2019 Feb - 2020 Feb Bitcoin Candlestick Chart',
    'yaxis': {'title': 'Price'},
    'xaxis': {'title': 'Index Number'},
}
fig = dict(data=data, layout=layout)
plot(fig, filename='btc_candles')





















# import talib
# candle_names = talib.get_function_groups()['Pattern Recognition']
#
# import requests
# import pandas as pd
# import numpy as np
# import talib
# from itertools import compress
# from candle_rankings import candle_rankings
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
#
#
# historical_dict = pd.read_csv('data.csv')
#
#
# df = pd.DataFrame(historical_dict,
#                              columns=['time','close', 'high', 'low', 'open', 'volumefrom', 'volumeto'])
#
# print(df.to_csv("new.csv"))