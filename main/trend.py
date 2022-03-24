# import  talib as ta
# import pandas as pd
# pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)
#
# bars = 'TRY_DATA.csv'
# data = pd.read_csv(bars)
# df = pd.DataFrame(data)
#
# #IF CURRENT CLOSE IS THE SAME WITH THE NEXT WE HOLD WITH A [0]
# df.loc[df['Close'] == df['Close'].shift(-1),'foo'] = "0"
#
# #IF CURRENT CLOSE IS LESS THAN THE NEXT WE BUY WITH A [1]
# df.loc[df['Close'] < df['Close'].shift(-1),'foo'] = "1"
#
# #IF CURRENT CLOSE IS MORE THAN THE NEXT WE SELL WITH A [-1]
# df.loc[df['Close'] > df['Close'].shift(-1),'foo'] = "-1"
#
# print(df)

data = 1

a = data.apply(lambda x: 'found' if x == 1 else 'not found')




















#
# df = pd.DataFrame(bars[:-1], columns=['timestamp','Open','High','Low','Close','Volume'])
#
# df['Pivot'] = (df['High'] + df['Low']+ df['Close'])/3
#
# df = df.tail(1).copy()
#
# df['Pivot'] = (float(df['High']) + float(df['Low'])+ float(df['Close']))/3
#
# df['R1'] = 2*df['Pivot'] - df['Low']
# df['S1'] = 2 * df['Pivot'] - df['High']
# df['R2'] = df['Pivot'] + (df['High'] - df['Low'])
# df['S2'] = df['Pivot'] - (df['High'] - df['Low'])
# df['R3'] = df['Pivot'] + 2*(df['High'] - df['Low'])
# df['S3'] = df['Pivot'] - 2*(df['High'] - df['Low'])
#


# df.to_csv('bit_s_s.csv', index=False)

