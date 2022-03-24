import csv

header = ['name','candle']
data = ['ENGULFING','CDLENGULFING']

with open('countries.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    writer.writerow(data)



# import ccxt
# import config
# import schedule
# # import panda_learn as pd
#
# import pandas as pd
# pd.set_option('display.max_rows', None)
#
# import warnings
#
# warnings.filterwarnings('ignore')
# def file():
#     data = pd.read_csv('TRY_DATA.csv')
#     return data
#
#
# def candlesticks(data):
#     print(data)
#
#
#
# print(candlesticks(file()))