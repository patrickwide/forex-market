import smtplib
import time
fromaddr = 'patkia911@gmail.com'
toaddrs  = 'patkia911@gmail.com'
msg = ""

username = 'patkia911@gmail.com'
password = 'police911.4089'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
print('done')




















# # Python code to illustrate Sending mail from
# # your Gmail account
# import smtplib
#
# # creates SMTP session
# s = smtplib.SMTP('smtp.gmail.com', 587)
#
# # start TLS for security
# s.starttls()
#
# # Authentication
# s.login("patkia911@gmail.com", "police911.4089")
#
# # message to be sent
# message = "Message_you_need_to_send"
#
# # sending the mail
# s.sendmail("patkia911@gmail.com", "patkia911@gmail.com", message)
#
# # terminating the session
# s.quit()














# # from __future__ import (absolute_import, division, print_function,
# #                         unicode_literals)
# #
# # import backtrader as bt
# #
# # if __name__ == '__main__':
# #     cerebro = bt.Cerebro()
# #
# #     print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
# #
# #     cerebro.run()
# #
# #     print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # #from talib import SMA, T3  # move this up to the top with other modules
# # # #import panda_learn
# # # #import talib
# # # #import csv
# # # import pandas as pd
# # # data = pd.read_csv('usd.csv',index_col='Date')
# # # print(data[:40])
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# #
# import talib
# csv_file_list = 'TRY_DATA.csv'
#
# #for csv_file in csv_file_list:
# df = pd.read_csv('TRY_DATA.csv')
#
# Symbol = df['Symbol']
# Date = df['Date']
# Open = df['Open']
# High = df['High']
# Low = df['Low']
# Close = df['Close']
# Volume = df['Volume']
#
# df['SMA'] = SMA(df['Close'], timeperiod=5)  # create column in df automatically
# df['Mornging star'] = talib.CDLMORNINGSTAR(df['Open'], df['High'], df['Low'], df['Close'])
# df['T3'] = T3(df['Close'], timeperiod=5, vfactor=0)  # create column in df automatically
# df['Engalfing'] = talib.CDLENGULFING(df['Open'], df['High'], df['Low'], df['Close'])
#
# #df is already built from above, so don't need next line
# total_df = pd.concat([Symbol, Date, Open, High, Low, Close, Volume, SMA, T3])
# print(df.head(60))
# Symbol = df.Symbol[0]
# fn = Symbol
# df.to_csv(fn)