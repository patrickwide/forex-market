import ccxt, yfinance
import pandas_ta as ta
import pandas as pd

exchange = ccxt.binance()

bars = pd.read_csv('usd.csv')#exchange.fetch_ohlcv('ETH/USDT', timeframe='5m', limit=500)

df = pd.DataFrame(bars, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])

print(df)

adx = ta.adx(df['High'], df['Low'], df['Close'])

adx = df.ta.adx()

macd = df.ta.macd(fast=14, slow=28)

print(macd)

rsi = df.ta.rsi()

df = pd.concat([df, adx, macd, rsi], axis=1)

print(df)

df = df[df['RSI_14'] < 30]

print(df)

# ticker = yfinance.Ticker("TSLA")
# df = ticker.history(period="1y")

# print(df)